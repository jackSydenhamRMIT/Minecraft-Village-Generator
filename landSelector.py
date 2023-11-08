from mcpi.minecraft import Minecraft
from mcpi import block
from House import House
from path import Path
import statistics

# This function checks the range of the array from the getHeights function (useless for now, since I switched to std deviation)
def checkRange(arr):

    if not arr:
        # If the input array is empty, return None
        return None
    
    max_val = 0
    min_val = 0
    max_val = max(arr)
    min_val = min(arr)
    range = max_val - min_val
    return range

def buildWall(x1, z1, x2, z2, y, height):
    #FIRST WALL
    mc.setBlocks(x1, y, z1, x2, y+height, z1, block.STONE)
    #SECOND WALL
    mc.setBlocks(x1, y, z1, x1, y+height, z2, block.STONE)
    #THIRD WALL
    mc.setBlocks(x2, y, z1, x2, y+height, z2, block.STONE)
    #FOURTH WALL
    mc.setBlocks(x1, y, z2, x2, y+height, z2, block.STONE)

def buildArea(quadrant, size, centre):
    # Get the player's current position
    x, y, z = centre

    x = int(x)
    y = int(y)
    z = int(z)

    # Define the size of the area and the wall
    width = size
    height = 10

    # Calculate the coordinates of the corners of the area according to the quadrant
    x1 = x
    z1 = z

    #SOUTH WEST
    if quadrant == 2:
        x2 = x - width - 1
        z2 = z + width - 1
        print("x,z = ", x, ", ", z)
        print("x2,z2 = ", x2, ", ", z2)
    #SOUTH EAST
    elif quadrant == 1:
        x2 = x + width - 1
        z2 = z + width - 1
        print("x,z = ", x, ", ", z)
        print("x2,z2 = ", x2, ", ", z2)
    #NORTH EAST
    elif quadrant == 3:
        x2 = x + width - 1
        z2 = z - width - 1
        print("x,z = ", x, ", ", z)
        print("x2,z2 = ", x2, ", ", z2)

    #NORTH WEST
    elif quadrant == 4:
        x2 = x - width - 1
        z2 = z - width - 1
        print("x,z = ", x, ", ", z)
        print("x2,z2 = ", x2, ", ", z2)
    
    buildWall(x, z, x2, z2, centre.y, 1)

#This function is desined to check which quadrant(64*64) next to the player have the least amount of deviance of height
def bestQuadrant(centre, size):
    stdDev = float('inf')


    #SOUTH EAST COORDINATE
    intDev = statistics.stdev(mc.getHeights(centre.x, centre.z, centre.x+size, centre.z+size))

    if intDev < stdDev:
        stdDev = intDev
        quadrant = 1

    #SOUTH WEST COORDINATE
    intDev = statistics.stdev(mc.getHeights(centre.x, centre.z, centre.x-size, centre.z+size))

    if intDev < stdDev:
        stdDev = intDev
        quadrant = 2

        
    # NORTH EAST COORDINATE
    intDev = statistics.stdev(mc.getHeights(centre.x, centre.z, centre.x+size, centre.z-size))

    if intDev < stdDev:
        stdDev = intDev
        quadrant = 3
        
    # NORTH WEST COORDINATE
    intDev = statistics.stdev(mc.getHeights(centre.x, centre.z, centre.x-size, centre.z-size))

    if intDev < stdDev:
        stdDev = intDev
        quadrant = 4

    if quadrant == 1:
        print("q = SE with standard deviation:", stdDev)

    elif quadrant == 2:
        print("q = SW with standard deviation:", stdDev)

    elif quadrant == 3:
        print("q = NE with standard deviation:", stdDev)

    elif quadrant == 4:
        print("q = NW with standard deviation:", stdDev)
    
    buildArea(quadrant, size, centre)

mc = Minecraft.create()
centre = mc.player.getPos()
bestQuadrant(centre, 100)