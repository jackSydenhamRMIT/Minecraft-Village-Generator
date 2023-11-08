# File for generating houses
from mcpi.minecraft import Minecraft
from mcpi import block
from paletteClass import Palette
from furnitureClass import Furniture
import random

class house:

    def __init__(self, y, width, height, depth):
        self.playerY = y
        self.depth = depth
        self.width = width
        self.height = height
        self.door_pos = None

    def build(self, x, y, z):
        mc = Minecraft.create()
        
        # Randomly selecting a palette 
        palette = Palette()
        selections = [1, 2, 3, 4]
        s = random.choice(selections)

        if s == 1:
            palette.beigePalette()
        elif s == 2:
            palette.stonePalette()
        elif s == 3:
            palette.sandPalette()
        elif s == 4:
            palette.brickPalette()

        # Build four walls
        # Front wall
        mc.setBlocks(x, y, z, x+self.width, y+self.height, z, palette.wall, palette.data_wall)
        # Right wall
        mc.setBlocks(x, y, z, x, y+self.height, z+self.depth, palette.wall, palette.data_wall)
        # Left wall
        mc.setBlocks(x+self.width, y, z, x+self.width, y+self.height, z+self.depth, palette.wall, palette.data_wall)
        # Back wall
        mc.setBlocks(x, y, z+self.depth, x+self.width, y+self.height, z+self.depth, palette.wall, palette.data_wall)

        # Roof 
        for i in range(1, (self.depth + 1) // 2 + 1):
            mc.setBlocks(x, y+self.height+i, z+i-1, x+self.width, y+self.height+i, z+i-1, palette.stairs, 2)
        # Other side of roof
        for i in range(1, (self.depth + 1) // 2 + 1):
            mc.setBlocks(x, y+self.height+i, z+self.depth-i+1, x+self.width, y+self.height+i, z+self.depth-i+1, palette.stairs, 3)

        # For loop, left wall
        for i in range(1, (self.depth + 1) // 2):
            mc.setBlocks(x+self.width, y+self.height+i, z+i, x+self.width, y+self.height+i, z+self.depth-i, palette.wall, palette.data_wall)
        # For loop, right wall
        for i in range(1, (self.depth + 1) // 2):
            mc.setBlocks(x, y+self.height+i, z+i, x, y+self.height+i, z+self.depth-i, palette.wall, palette.data_wall)

        # Ceiling
        mc.setBlocks(x+1, y+self.height+1, z+1, x+self.width-1, y+self.height+1, z+self.depth-1, palette.floor, palette.data_floor)

        # Windows
        # Ground floor windows
        mc.setBlocks(x+2, y+1, z, x+3, y+2, z, palette.glass_pane)
        mc.setBlocks(x+self.width-2, y+1, z, x+self.width-3, y+2, z, palette.glass_pane)
        # First floor + second floor windows
        if self.height == 13:
            mc.setBlocks(x+2, y+self.height-2, z, x+3, y+self.height-1, z, palette.glass_pane)
            mc.setBlocks(x+self.width-2, y+self.height-2, z, x+self.width-3, y+self.height-1, z, palette.glass_pane)
            mc.setBlocks(x+2, y+6, z, x+3, y+7, z, palette.glass_pane)
            mc.setBlocks(x+self.width-2, y+6, z, x+self.width-3, y+7, z, palette.glass_pane)
        # First floor windows
        elif self.height == 5 or self.height == 7: 
            mc.setBlocks(x+2, y+self.height-1, z, x+3, y+self.height, z, palette.glass_pane)
            mc.setBlocks(x+self.width-2, y+self.height-1, z, x+self.width-3, y+self.height, z, palette.glass_pane)
        # Window frames
        mc.setBlocks(x+4, y+1, z, x+4, y+2, z, palette.glass_frames, palette.data_glass_frames)
        mc.setBlocks(x+1, y+1, z, x+1, y+2, z, palette.glass_frames, palette.data_glass_frames)
        mc.setBlocks(x+self.width-1, y+1, z, x+self.width-1, y+2, z, palette.glass_frames, palette.data_glass_frames)
        mc.setBlocks(x+self.width-4, y+1, z, x+self.width-4, y+2, z, palette.glass_frames, palette.data_glass_frames)

        # Top/middle window frames
        if self.height == 13:
            mc.setBlocks(x+4, y+self.height-2, z, x+4, y+self.height-1, z, palette.glass_frames, palette.data_glass_frames)
            mc.setBlocks(x+1, y+self.height-2, z, x+1, y+self.height-1, z, palette.glass_frames, palette.data_glass_frames)
            mc.setBlocks(x+self.width-1, y+self.height-2, z, x+self.width-1, y+self.height-1, z, palette.glass_frames, palette.data_glass_frames)
            mc.setBlocks(x+self.width-4, y+self.height-2, z, x+self.width-4, y+self.height-1, z, palette.glass_frames, palette.data_glass_frames)
            # Middle
            mc.setBlocks(x+4, y+6, z, x+4, y+7, z, palette.glass_frames, palette.data_glass_frames)
            mc.setBlocks(x+1, y+6, z, x+1, y+7, z, palette.glass_frames, palette.data_glass_frames)
            mc.setBlocks(x+self.width-1, y+6, z, x+self.width-1, y+7, z, palette.glass_frames, palette.data_glass_frames)
            mc.setBlocks(x+self.width-4, y+6, z, x+self.width-4, y+7, z, palette.glass_frames, palette.data_glass_frames)
        elif self.height == 5 or self.height == 7: 
            mc.setBlocks(x+4, y+self.height-1, z, x+4, y+self.height, z, palette.glass_frames, palette.data_glass_frames)
            mc.setBlocks(x+1, y+self.height-1, z, x+1, y+self.height, z, palette.glass_frames, palette.data_glass_frames)
            mc.setBlocks(x+self.width-1, y+self.height-1, z, x+self.width-1, y+self.height, z, palette.glass_frames, palette.data_glass_frames)
            mc.setBlocks(x+self.width-4, y+self.height-1, z, x+self.width-4, y+self.height, z, palette.glass_frames, palette.data_glass_frames)

        # Floors
        # Ground floor
        mc.setBlocks(x, y-1, z, x+self.width, y-1, z+self.depth, palette.floor, palette.data_floor)
        # First floor (Adjusted for 3 floors)
        if self.height == 13:
            mc.setBlocks(x+1, y+4, z+1, x+self.width-1, y+4, z+self.depth-1, palette.floor, palette.data_floor)
            # Second floor
            mc.setBlocks(x+1, y+9, z+1, x+self.width-1, y+9, z+self.depth-1, palette.floor, palette.data_floor)
        elif self.height == 5 or self.height == 7: 
            mc.setBlocks(x+1, y+(self.height+1)//2, z+1, x+self.width-1, y+(self.height+1)//2, z+self.depth-1, palette.floor, palette.data_floor)

        # Doors
        # Hollow out door
        mc.setBlock(x+self.width//2, y, z, x+self.width//2+1, y+1, z, 0)
        # Add door
        mc.setBlock(x+self.width//2, y+1, z, palette.door, 8)
        mc.setBlock(x+self.width//2 , y, z, palette.door, 4)
        mc.setBlock(x+self.width//2 + 1, y+1, z, palette.door, 8)
        mc.setBlock(x+self.width//2 + 1, y, z, palette.door, 4)
        self.door_pos = int(x+self.width//2), self.playerY, int(z - 1)
        
        def recursiveWall(w, d, lower_h, upper_h, num_walls):
            stop = num_walls
            if stop == 2:
                return 
            else:
                if w >= d:
                    # Randomly halving the room
                    ws = [w//2 - 1, w//2 + 2]
                    W = random.choice(ws)
                    mc.setBlocks(x+W, y+lower_h, z+1, x+W, y+upper_h, z+d, palette.wall, palette.data_wall)
                    # Doorway
                    mc.setBlocks(x+W, y+lower_h, z+d-2, x+W, y+lower_h+1, z+d-2, 0)
                    recursiveWall(W, d, lower_h, upper_h, num_walls+1)
                    return
                elif d > w:
                    # Randomly halving the room
                    ds = [d//2 - 1, d//2 + 2]
                    D = random.choice(ds)
                    mc.setBlocks(x, y+lower_h, z+D, x+w, y+upper_h, z+D, palette.wall, palette.data_wall)
                    # Doorway
                    mc.setBlocks(x+w-2, y+lower_h, z+D, x+w-2, y+lower_h+1, z+D, 0)
                    recursiveWall(w, D, lower_h, upper_h, num_walls+1)
                    return       

        if self.height == 7:           
            recursiveWall(self.width, self.depth, 0, (self.height+1)//2 - 1, 0)
            recursiveWall(self.width, self.depth, (self.height+1)//2 + 1, self.height, 0)
        elif self.height == 3:
            recursiveWall(self.width, self.depth, 0, self.height, 0)
        elif self.height == 5:
            recursiveWall(self.width, self.depth, 0, (self.height+1)//2 - 1, 0)
            recursiveWall(self.width, self.depth, (self.height+1)//2 + 1, self.height, 0)
        elif self.height == 13:
            recursiveWall(self.width, self.depth, 0, 3, 0)
            recursiveWall(self.width, self.depth, 5, 8, 0)
            recursiveWall(self.width, self.depth, 10, 13, 0)
 
        # Stairs
        if self.height == 5:
            mc.setBlocks(x+self.width-1, y, z+self.depth-1, x+self.width-6, y+self.height, z+self.depth-1, 0) # Space for stairs
            mc.setBlocks(x+self.width-1, y+(self.height+1)//2, z+self.depth-1, x+self.width-1, y+(self.height+1)//2, z+self.depth-1, palette.floor, palette.data_floor)
            for i, j in zip(range(2, 6), reversed(range(4))):
                mc.setBlocks(x+self.width-i, y+j, z+self.depth-1, x+self.width-i, y+j, z+self.depth-1, palette.stairs)
 
        elif self.height >= 7: 
            mc.setBlocks(x+self.width-1, y, z+self.depth-1, x+self.width-6, y+4, z+self.depth-1, 0) # Space for stairs
            for i, j in zip(range(1, 6), reversed(range(5))):
                mc.setBlocks(x+self.width-i, y+j, z+self.depth-1, x+self.width-i, y+j, z+self.depth-1, palette.stairs)
 
        if self.height == 13: 
            mc.setBlocks(x+1, y+5, z+self.depth-1, x+6, y+9, z+self.depth-1, 0) # Space for stairs
            for i, j in zip(range(1, 6), reversed(range(5, 10))):
                mc.setBlocks(x+i, y+j, z+self.depth-1, x+i, y+j, z+self.depth-1, palette.stairs, 1)

        # Furniture
        furniture = Furniture(self.width, self.depth, self.height)
        furniture.arrangeFurniture(x, y, z)



        
