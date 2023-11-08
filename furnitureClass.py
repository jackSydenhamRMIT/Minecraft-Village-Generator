from mcpi.minecraft import Minecraft
from mcpi import block
from paletteClass import Palette
import random

class Furniture:
    def __init__(self, width, depth, height):
        self.width = width
        self.depth = depth
        self.height = height

    def arrangeFurniture(self, x, y, z):
        mc = Minecraft.create()
        
        # Furniture blocks
        bookshelf = block.BOOKSHELF.id
        glowstone = block.GLOWSTONE_BLOCK.id
        chest = block.CHEST.id
        furnace = 61
        crafting = 58
        jukebox = 84
        anvil = 145
        enchant = 116
        cauldron = 118

        # Lighting
        if self.height == 5:
            mc.setBlock(x+1, y+(self.height+1)//2, z+1, glowstone)
            mc.setBlock(x+self.width-1, y+(self.height+1)//2, z+1, glowstone)
            mc.setBlock(x+self.width-1, y+(self.height+1)//2, z+self.depth-1, glowstone)
            mc.setBlock(x+1, y+(self.height+1)//2, z+self.depth-1, glowstone)
            mc.setBlocks(x+self.width//2, y+(self.height+1)//2, z+1, x+self.width//2+1, y+(self.height+1)//2, z+1, glowstone)
            # Ceiling lights
            mc.setBlock(x+1, y+self.height+1, z+1, glowstone)
            mc.setBlock(x+self.width-1, y+self.height+1, z+1, glowstone)
            mc.setBlock(x+self.width-1, y+self.height+1, z+self.depth-1, glowstone)
            mc.setBlock(x+1, y+self.height+1, z+self.depth-1, glowstone)
            mc.setBlocks(x+self.width//2, y+self.height+1, z+1, x+self.width//2+1, y+self.height+1, z+1, glowstone)
        elif self.height == 7:
            mc.setBlock(x+1, y+(self.height+1)//2, z+1, glowstone)
            mc.setBlock(x+self.width-1, y+(self.height+1)//2, z+1, glowstone)
            mc.setBlock(x+1, y+(self.height+1)//2, z+self.depth-1, glowstone)
            mc.setBlocks(x+self.width//2, y+(self.height+1)//2, z+1, x+self.width//2+1, y+(self.height+1)//2, z+1, glowstone)
            # Ceiling lights
            mc.setBlock(x+1, y+self.height+1, z+1, glowstone)
            mc.setBlock(x+self.width-1, y+self.height+1, z+1, glowstone)
            mc.setBlock(x+self.width-1, y+self.height+1, z+self.depth-1, glowstone)
            mc.setBlock(x+1, y+self.height+1, z+self.depth-1, glowstone)
            mc.setBlocks(x+self.width//2, y+self.height+1, z+1, x+self.width//2+1, y+self.height+1, z+1, glowstone)
        elif self.height == 13:
            # First floor lights
            mc.setBlock(x+1, y+4, z+1, glowstone)
            mc.setBlock(x+self.width-1, y+4, z+1, glowstone)
            mc.setBlock(x+1, y+4, z+self.depth-1, glowstone)
            mc.setBlocks(x+self.width//2, y+4, z+1, x+self.width//2+1, y+4, z+1, glowstone)
            # Second floor lights
            mc.setBlock(x+1, y+9, z+1, glowstone)
            mc.setBlock(x+self.width-1, y+9, z+1, glowstone)
            mc.setBlock(x+self.width-1, y+9, z+self.depth-1, glowstone)
            mc.setBlocks(x+self.width//2, y+9, z+1, x+self.width//2+1, y+9, z+1, glowstone)
            # Ceiling lights
            mc.setBlock(x+1, y+self.height+1, z+1, glowstone)
            mc.setBlock(x+self.width-1, y+self.height+1, z+1, glowstone)
            mc.setBlock(x+self.width-1, y+self.height+1, z+self.depth-1, glowstone)
            mc.setBlock(x+1, y+self.height+1, z+self.depth-1, glowstone)
            mc.setBlocks(x+self.width//2, y+self.height+1, z+1, x+self.width//2+1, y+self.height+1, z+1, glowstone)
        elif self.height == 3:
            mc.setBlock(x+1, y+self.height+1, z+1, glowstone)
            mc.setBlock(x+self.width-1, y+self.height+1, z+1, glowstone)
            mc.setBlock(x+self.width-1, y+self.height+1, z+self.depth-1, glowstone)
            mc.setBlock(x+1, y+self.height+1, z+self.depth-1, glowstone)

        # Library or chest
        rand_G = [1, 2]
        G = random.choice(rand_G)
        # Ground floor furniture
        if G == 1:
            mc.setBlocks(x+self.width-1, y, z+1, x+self.width-1, y+2, z+3, bookshelf)
        else:
            mc.setBlock(x+self.width-1, y, z+1, furnace)
            mc.setBlock(x+self.width-1, y, z+2, crafting)
            mc.setBlock(x+self.width-1, y, z+3, anvil)

        # First floor furniture
        rand_F = [1, 2]
        F = random.choice(rand_F)
        if F == 1:
            if self.height == 5:
                mc.setBlock(x+1, y+(self.height+1)//2+1, z+1, chest)
                mc.setBlock(x+self.width-1, y+(self.height+1)//2+1, z+1, enchant)
            elif self.height == 7:
                mc.setBlock(x+1, y+(self.height+1)//2+1, z+1, chest)
                mc.setBlock(x+self.width-1, y+(self.height+1)//2+1, z+1, enchant)
            elif self.height == 13:
                mc.setBlock(x+1, y+4, z+1, chest)
                mc.setBlock(x+self.width-1, y+4, z+1, enchant)

        else:
            if self.height == 5:
                mc.setBlock(x+1, y+(self.height+1)//2+1, z+1, jukebox)
                mc.setBlock(x+self.width-1, y+(self.height+1)//2+1, z+1, chest)
            elif self.height == 7:
                mc.setBlock(x+1, y+(self.height+1)//2+1, z+1, jukebox)
                mc.setBlock(x+self.width-1, y+(self.height+1)//2+1, z+1, chest)
            elif self.height == 13:
                mc.setBlock(x+1, y+4, z+1, jukebox)
                mc.setBlock(x+self.width-1, y+4, z+1, chest)

        # Second floor furniture
        rand_S = [1, 2]
        S = random.choice(rand_S)
        if S == 1:
            if self.height == 13:
                mc.setBlocks(x+self.width-1, y+10, z+1, x+self.width-1, y+12, z+2, bookshelf)
                mc.setBlock(x+self.width-1, y+10, z+3, enchant)
        else:
            if self.height == 13:
                mc.setBlock(x+self.width-1, y+10, z+1, cauldron)
                mc.setBlock(x+self.width-1, y+10, z+3, enchant)
