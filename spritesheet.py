import pygame
from settings import*

class spritesheet:
    def __init__(self, filename, cols, rows):
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.cols = cols
        self.rows = rows
        self.totalCellCount = cols * rows

        self.rect = self.sheet.get_rect()
        w = self.cellWidth = int(self.rect.width / cols)
        h = self.cellHeight = int(self.rect.height / rows)
        hw, hh = self.cellCenter = (int(w / 2), int(h / 2))
        self.cells = list([(index % cols * w, int(index / cols) * h, w, h) for index in range(self.totalCellCount)])

    def draw(self, surface, cellIndex, x, y, bool):
        if bool == True:
            sheet = pygame.transform.flip(self.sheet,True,False)
        if bool == False:
            sheet = self.sheet
        surface.blit(sheet, (x, y), self.cells[cellIndex])
        subsurface = sheet.subsurface(self.cells[cellIndex])
        return subsurface

    def output_draw(self, cellIndex):
        subsurface = self.sheet.subsurface(self.cells[int(cellIndex)%self.totalCellCount])
        return subsurface


    def special_draw(self,cellIndex):
        return self.cells[cellIndex]



boat_up = spritesheet(directory + "/Boat_images/boat_up.png",9,1)
boat_up_diagonal = spritesheet(directory + "/Boat_images/boat_up_right.png",9,1)
boat_right = spritesheet(directory + "/Boat_images/boat_right.png",9,1)
boat_down_diagonal = spritesheet(directory + "/Boat_images/boat_right_down.png",9,1)
boat_down = spritesheet(directory + "/Boat_images/boat_down.png",9,1)
seaguls = spritesheet(directory + "/Boat_images/seaguls1.png",3,1)
full_grass = spritesheet(directory + "/Boat_images/full_grass2.png",12,6)
full_water = spritesheet(directory + "/Boat_images/full_water.png",10,5)
