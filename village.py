# Assignment 1 main file
# Feel free to add additional modules/files as you see fit.

# -- HOW TO RUN -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #
# Ensure that you are flying when you run the file.
# When you run the file, houses will be placed at random positions in a +z+x direction
# 
# path generation is a little slow, and may take a while to produce paths to houses if 
# some are far away (on my device at least).
#
# ALSO: Since the time of recording, a change was made to the pathfinder to teleport the
#       player to one of the doors to be used as the starting point for the path. This 
#       allows the algorithm to run faster, as it effectively has to make one less path
#       while also making the village seem much more together, as the paths no longer 
#       converge on one point outside of the village
# -- -- -- -- -- -- -- -- -- -- -- -- --- --- -- -- -- -- -- -- -- -- -- -- -- -- -- -- #

from mcpi.minecraft import Minecraft
from houseClass import house 
import random
from villageAesthetics import villageAesthetics
import math
from mcpi import block
from terraforming import platform

mc = Minecraft.create()
x,y,z = mc.player.getTilePos()

# Teleporting player to start position
ground_height = mc.getHeight(x,z)
new_pos = (x, ground_height + 5, z)
mc.player.setTilePos(new_pos)
x,y,z = mc.player.getTilePos()

# Building all houses
depths = [7, 9, 11]
heights = [3, 5, 7, 13]
widths = [11, 15, 19]
door_positions = []

# Spawning the houses
houseCount = random.randint(3,3)
for i in range(houseCount):
    y = y
    width = random.choice(widths)
    depth = random.choice(depths)
    height = random.choice(heights)

    house1 = house(y,width,height,depth)
    
    xCor = x + (random.random() * 50)
    zCor = z + (random.random() * 50)
    formation1 = platform(xCor, zCor)

    stage = formation1.terraform(mc)
    house1.build(xCor + width//2, stage ,zCor + depth//2)
    print("House spawned: ", int(xCor), int(zCor))

    door_positions.append(house1.door_pos)


# -- Pathing between houses (generational data is displayed in the VS Code terminal) -- #

mc = Minecraft.create()

user = mc.getPlayerEntityId

print(f"Door positions (end-points): {door_positions}")

# Teleporting the player to one of the doors, as to make the village seem more together with the paths
mc.doCommand(f"tp @s {door_positions[0][0]} {door_positions[0][1]} {door_positions[0][2]}")
x,y,z = mc.player.getTilePos()
print( "Generating road...")

# Declaring blocks which are to be avoided when producing the path to avoid paths going through buildings, i.e. what the buildings are made of.
disallowed_block_ids = [block.STONE_BRICK.id, block.GLASS_PANE.id, block.BRICK_BLOCK.id, block.WOOD_PLANKS.id, block.SANDSTONE.id, block.GLASS_PANE.id, block.OBSIDIAN.id, block.WOOL.id]

# Defining the start and end positions
start_pos = (x, y, z)
end_positions = [door_positions[0], door_positions[1], door_positions[2]]

# Helper Function to calculate the distance between two points
def distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2 + (pos1[2] - pos2[2]) ** 2)

# Helper function to get the neighboring nodes of a given node
def get_neighbors(pos):
    x, y, z = pos
    neighbors = [(x + dx, y, z + dz) for dx in [-1, 0, 1] for dz in [-1, 0, 1] if dx != 0 or dz != 0]
    return [(nx, ny, nz) for (nx, ny, nz) in neighbors if mc.getBlock(nx, ny, nz) not in disallowed_block_ids]


# Function for searching for multiple paths
def find_multiple_paths(start_pos, end_positions):
    paths = []
    for end_pos in end_positions:
        came_from = {}
        path = find_path(start_pos, end_pos, came_from)
        if path:
            paths.append(path)

    return paths

# A* algorithm for pathfinding
def find_path(start_pos, end_pos, came_from):
    print("Generating next path nodes...")

    # Initializing the open and closed sets
    open_set = [start_pos]
    closed_set = set()

    # Initializing g and f scores for the start node
    g_scores = {start_pos: 0}
    f_scores = {start_pos: distance(start_pos, end_pos)}

    # Looping until the open set is empty
    while open_set:
        # Getting the node with the lowest f score
        current_pos = min(open_set, key=lambda pos: f_scores[pos])

        # Checking if we've reached the end position
        if current_pos == end_pos:
            # Reconstructing the path
            path = [current_pos]
            while current_pos in came_from:
                current_pos = came_from[current_pos]
                path.append(current_pos)
            path.reverse()
            return path

        # Moving the current node from the open set to the closed set
        open_set.remove(current_pos)
        closed_set.add(current_pos)

        # Updating the scores for the neighboring nodes
        for neighbor_pos in get_neighbors(current_pos):
            if neighbor_pos in closed_set:
                continue
            tentative_g_score = g_scores[current_pos] + distance(current_pos, neighbor_pos)
            if neighbor_pos not in open_set:
                open_set.append(neighbor_pos)
            elif tentative_g_score >= g_scores[neighbor_pos]:
                continue

            # This path is the best at this point
            came_from[neighbor_pos] = current_pos
            g_scores[neighbor_pos] = tentative_g_score
            f_scores[neighbor_pos] = g_scores[neighbor_pos] + distance(neighbor_pos, end_pos)

# Finding the paths using A* algorithm function
came_from = {}
paths = find_multiple_paths(start_pos, end_positions)

print("Building paths...")
# Creating a 3-block wide path of blocks along the ground based on nodes found using A*
for path in paths:
    for pos in path:
        x, z = pos[0], pos[2]
        y = mc.getHeight(x, z)

        # Placing the main path block
        mc.setBlock(x, y, z, block.STONE_BRICK.id)

        # Checking height differences and placing additional blocks on either side of the main path while maintaining walkability
        neighbors = [(x + dx, z + dz) for dx in [-1, 0, 1] for dz in [-1, 0, 1] if dx != 0 or dz != 0]
        for nx, nz in neighbors:
            ny = mc.getHeight(nx, nz)
            height_diff = abs(ny - y)
            if height_diff <= 1:
                mc.setBlock(nx, ny, nz, block.STONE_BRICK.id)

# Placing lanterns along the created paths
for path in paths:
    for i in range(0, len(path), 15):
        pos = path[i]
        x, z = pos[0], pos[2]
        y = mc.getHeight(x, z)

        if pos == start_pos:
            continue

        # Getting the outer blocks of the paths
        neighbors = [(x + dx, z + dz) for dx in [-2, 0, 2] for dz in [-2, 0, 2] if dx != 0 or dz != 0]
        for nx, nz in neighbors:
            ny = mc.getHeight(nx, nz)
            neighbor_pos = (nx, ny, nz)

            # Building lanterns on those blocks
            if mc.getBlock(nx, ny, nz) != block.STONE_BRICK.id:
                mc.setBlock(nx, ny, nz, block.COBBLESTONE.id)
                mc.setBlock(nx, ny + 1, nz, block.STONE_BRICK.id)
                mc.doCommand(f"setblock {nx} {ny + 2} {nz} minecraft:stone_brick_wall")
                mc.doCommand(f"setblock {nx} {ny + 3} {nz} minecraft:stone_brick_wall")
                mc.setBlock(nx, ny + 4, nz, block.STONE_BRICK.id)
                mc.doCommand(f"setblock {nx} {ny + 5} {nz} minecraft:stone_brick_slab")
                mc.doCommand(f"setblock {nx + 1} {ny + 4} {nz} minecraft:dark_oak_trapdoor")
                mc.doCommand(f"setblock {nx - 1} {ny + 4} {nz} minecraft:dark_oak_trapdoor")
                mc.doCommand(f"setblock {nx} {ny + 4} {nz + 1} minecraft:dark_oak_trapdoor")
                mc.doCommand(f"setblock {nx} {ny + 4} {nz - 1} minecraft:dark_oak_trapdoor")
                mc.doCommand(f"setblock {nx + 1} {ny + 4} {nz} minecraft:dark_oak_fence")
                mc.doCommand(f"setblock {nx - 1} {ny + 4} {nz} minecraft:dark_oak_fence")
                mc.doCommand(f"setblock {nx} {ny + 4} {nz + 1} minecraft:dark_oak_fence")
                mc.doCommand(f"setblock {nx} {ny + 4} {nz - 1} minecraft:dark_oak_fence")
                mc.doCommand(f"setblock {nx + 1} {ny + 3} {nz} minecraft:lantern")
                mc.doCommand(f"setblock {nx - 1} {ny + 3} {nz} minecraft:lantern")
                mc.doCommand(f"setblock {nx} {ny + 3} {nz + 1} minecraft:lantern")
                mc.doCommand(f"setblock {nx} {ny + 3} {nz - 1} minecraft:lantern")
                break



