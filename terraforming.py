from mcpi.minecraft import Minecraft
from mcpi import block
from array import *
import random

class platform:
    def __init__(self, x, z):
        self.x = x
        self.z = z
    
    def terraform(self, mc):
        x1 = int(self.x)
        z1 = int(self.z)
        y = mc.getHeight(x1, z1)
        x2 = x1 + 20
        z2 = z1+ 20

        mc.doCommand(f'fill {int(x1)} {int(y-25)} {int(z1)} {x2} {int(y+20)} {z2} minecraft:air replace minecraft:oak_log')
        mc.doCommand(f'fill {int(x1)} {int(y-25)} {int(z1)} {x2} {int(y+20)} {z2} minecraft:air replace minecraft:dark_oak_log')
        mc.doCommand(f'fill {int(x1)} {int(y-25)} {int(z1)} {x2} {int(y+20)} {z2} minecraft:air replace minecraft:spruce_log')
        mc.doCommand(f'fill {int(x1)} {int(y-25)} {int(z1)} {x2} {int(y+20)} {z2} minecraft:air replace minecraft:birch_log')
        mc.doCommand(f'fill {int(x1)} {int(y-25)} {int(z1)} {x2} {int(y+20)} {z2} minecraft:air replace minecraft:jungle_log')
        mc.doCommand(f'fill {int(x1)} {int(y-25)} {int(z1)} {x2} {int(y+20)} {z2} minecraft:air replace minecraft:acacia_log')

        mc.doCommand(f'fill {int(x1)} {int(y-25)} {int(z1)} {x2} {int(y+20)} {z2} minecraft:air replace minecraft:oak_leaves')
        mc.doCommand(f'fill {int(x1)} {int(y-25)} {int(z1)} {x2} {int(y+20)} {z2} minecraft:air replace minecraft:dark_oak_leaves')
        mc.doCommand(f'fill {int(x1)} {int(y-25)} {int(z1)} {x2} {int(y+20)} {z2} minecraft:air replace minecraft:spruce_leaves')
        mc.doCommand(f'fill {int(x1)} {int(y-25)} {int(z1)} {x2} {int(y+20)} {z2} minecraft:air replace minecraft:birch_leaves')
        mc.doCommand(f'fill {int(x1)} {int(y-25)} {int(z1)} {x2} {int(y+20)} {z2} minecraft:air replace minecraft:jungle_leaves')
        mc.doCommand(f'fill {int(x1)} {int(y-25)} {int(z1)} {x2} {int(y+20)} {z2} minecraft:air replace minecraft:acacia_leaves')


        terrain = mc.getBlock(x1, mc.getHeight(x1, z1), z1)
        if terrain == 0 or terrain == 3:
            terrain = 2
        
        if terrain == 8 or terrain == 9:
            terrain = 12


        
        #get the max height in the local area
        maxHeight = max(mc.getHeights(x1, z1, x2, z2))
        # get the minimum height in the far area
        m = min(mc.getHeights(x1-50, z1-50, x2+50, z2+50))

        #Clearing out the platform
        mc.setBlocks(x1, maxHeight, z1, x2, maxHeight+80, z2, 0)

        diff = maxHeight - m

        for height in range(m, maxHeight):
            #spawns the base for the terraforming
            mc.setBlocks(x1-diff, height, z1-diff, x2+diff, height, z2+diff, terrain)
        
            if height + 1 < maxHeight:
                #This will randomly place blocks around the staircase to make it look more natural
                for x in range(x1-diff, x2+diff):
                    if random.random() > 0.13:
                        mc.setBlock(x, height+1, random.choice([z1-diff, z2+diff]), terrain)
                for z in range(z1-diff, z2+diff):
                    if random.random() > 0.13:
                        mc.setBlock(random.choice([x1-diff, x2+diff]), height+1, z, terrain)
                
            diff -= 1
        return maxHeight
