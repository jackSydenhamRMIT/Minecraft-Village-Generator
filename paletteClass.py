from mcpi.minecraft import Minecraft
from mcpi import block

class Palette:
    def __init__(self):
        self.wall, self.data_wall = 0, 0
        self.floor, self.data_floor = 0,0
        self.stairs = 0
        self.glass_pane = 0
        self.door = 0
        self.chimney = 0
        self.glass_frames, self.data_glass_frames = 0, 0
            
    def beigePalette(self):
        self.wall, self.data_wall = block.WOOD_PLANKS
        self.floor, self.data_floor = 5, 0
        self.stairs = 109
        self.glass_pane = block.GLASS_PANE  
        self.door = block.DOOR_DARK_OAK.id
        self.chimney = 45
        self.glass_frames, self.data_glass_frames = block.SANDSTONE

    def stonePalette(self):
        self.wall, self.data_wall = block.STONE_BRICK
        self.floor, self.data_floor = 35, 7
        self.stairs = 114
        self.glass_pane = block.GLASS_PANE 
        self.door = block.DOOR_SPRUCE.id
        self.chimney = 5
        self.glass_frames, self.data_glass_frames = block.OBSIDIAN

    def sandPalette(self):
        self.wall, self.data_wall = block.SANDSTONE
        self.floor, self.data_floor = 35, 0
        self.stairs = 180
        self.glass_pane = block.GLASS_PANE 
        self.door = block.DOOR_SPRUCE.id
        self.chimney = 5
        self.glass_frames, self.data_glass_frames = block.STONE

    def brickPalette(self):
        self.wall, self.data_wall = block.BRICK_BLOCK
        self.floor, self.data_floor = 5, 5
        self.stairs = 164
        self.glass_pane = block.GLASS_PANE 
        self.door = block.DOOR_SPRUCE.id
        self.chimney = 5
        self.glass_frames, self.data_glass_frames = block.WOOL
