# Adding village structures/objects
from mcpi.minecraft import Minecraft
from mcpi import block
import mcpi.entity as entity
import random

class villageAesthetics:
    def __init__(self, mc):
        self.x, self.y, self.z = mc.player.getPos()


# Well the fence and water does not work but ill work on that later :)
    def spawnWell(self, mc):
        print(self.x, self. y, self.z)
        mc.setBlocks(self.x, self.y, self.z, self.x+4, self.y, self.z+4, block.GRAVEL)
        mc.setBlocks(self.x+1, self.y, self.z+1, self.x+3, self.y+1, self.z+3, block.COBBLESTONE)
        mc.setBlocks(self.x+2, self.y+5, self.z+2, self.x+2, self.y-5, self.z+2, block.AIR)

        mc.setBlocks(self.x+1, self.y+2, self.z+1, self.x+1, self.y+3, self.z+1, block.FENCE)
        mc.setBlocks(self.x+1, self.y+2, self.z+3, self.x+1, self.y+3, self.z+3, block.FENCE)
        mc.setBlock(self.x+3, self.y+2, self.z+1, self.x+3, self.y+3, self.z+1, block.FENCE)
        mc.setBlock(self.x+3, self.y+2, self.z+3, self.x+3, self.y+3, self.z+3, block.FENCE)


        mc.setBlocks(self.x+1, self.y+4, self.z+1, self.x+3, self.y+4, self.z+3, block.COBBLESTONE)
        mc.setBlocks(self.x+2, self.y+2, self.z+2, block.WATER_FLOWING)



# Streetlamps
    def spawnLamp(self, mc):
        print("SPAWN LAMP")
        mc.setBlock(self.x, self.y+4, self.z, block.GLOWSTONE_BLOCK)
        mc.setBlocks(self.x, self.y, self.z, self.x, self.y+3, self.z, block.FENCE)

        mc.setBlock(self.x, self.y+5, self.z, block.TRAPDOOR.id, 0)
        mc.setBlock(self.x, self.y+4, self.z+1, block.TRAPDOOR.id, 4|1)
        mc.setBlock(self.x+1, self.y+4, self.z, block.TRAPDOOR.id, 4|3)
        mc.setBlock(self.x-1, self.y+4, self.z, block.TRAPDOOR.id, 4|2)
        mc.setBlock(self.x, self.y+4, self.z-1, block.TRAPDOOR.id, 4|0)





# Trees
    def spawnTree(self, mc):
        print("SPAWN TREE")
        mc.setBlocks(self.x+2, self.y+4, self.z+2, self.x-2, self.y+4, self.z-2, block.LEAVES)
        mc.setBlocks(self.x+1, self.y+5, self.z+1, self.x-1, self.y+5, self.z-1, block.LEAVES)
        mc.setBlock(self.x, self.y+6, self.z, block.LEAVES)
        mc.setBlocks(self.x, self.y, self.z, self.x, self.y+4, self.z, block.WOOD)


# Animal pens
    def spawnPen(self, mc):
        print("spawn pen")
        mc.setBlocks(self.x, self.y, self.z, self.x+5, self.y, self.z+5, block.FENCE)
        mc.setBlocks(self.x+1, self.y, self.z+1, self.x+4, self.y, self.z+4, block.AIR)

        animal = random.randint(1,4)
        count = random.randint(3, 6)

        if animal == 1:
            for i in range(count):
                mc.spawnEntity(self.x+1, self.y, self.z+1, entity.COW.id)
        elif animal == 2:
            for i in range(count):
                mc.spawnEntity(self.x+1, self.y, self.z+1, entity.CHICKEN.id)
        elif animal == 3:
            for i in range(count):
                mc.spawnEntity(self.x+1, self.y, self.z+1, entity.SHEEP.id)
        elif animal == 4:
            for i in range(count):
                mc.spawnEntity(self.x+1, self.y, self.z+1, entity.PIG.id)


# Water fountain [
    def spawnFountain(self, mc):
        mc.setBlocks(self.x+7,self.y+1,self.z-1,self.x+7,self.y+1,self.z+5,block.MOSS_STONE)
        mc.setBlocks(self.x-1,self.y+1,self.z-1,self.x-1,self.y+1,self.z+5,block.MOSS_STONE)
        mc.setBlocks(self.x-1,self.y+1,self.z-1,self.x+6,self.y+1,self.z-1,block.MOSS_STONE)
        mc.setBlocks(self.x-1,self.y+1,self.z+5,self.x+6,self.y+1,self.z+5,block.MOSS_STONE)
        mc.setBlocks(self.x-1,self.y,self.z-1,self.x+7,self.y,self.z+5,block.MOSS_STONE)
        mc.setBlocks(self.x+2,self.y,self.z+1,self.x+4,self.y,self.z+3,block.STONE_BRICK)
        mc.setBlocks(self.x+2,self.y,self.z+2,self.x+4,self.y+4,self.z+2,block.STONE_BRICK)

        mc.setBlock(self.x+5,self.y,self.z+2,block.STONE_BRICK)
        mc.setBlock(self.x+1,self.y,self.z+2,block.STONE_BRICK)

        mc.setBlock(self.x+3,self.y,self.z+4,block.STONE_BRICK)

        mc.setBlock(self.x+3,self.y,self.z,block.STONE_BRICK)
        mc.setBlock(self.x+3,self.y+5,self.z+2,block.WATER)
        mc.setBlocks(self.x+3,self.y,self.z+1,self.x+3,self.y+4,self.z+3,block.STONE_BRICK)


# Village tower/church/hall?


mc = Minecraft.create()
village = villageAesthetics(mc)
village.spawnFountain
