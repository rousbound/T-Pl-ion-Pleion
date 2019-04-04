import pygame
import random
from settings import*
from spritesheet import *
from Gaia import*
class Map():

    def __init__(self):
        self.water = pygame.image.load(directory + "/Boat_images/water1.png").convert_alpha()
        #self.grass = full_grass.output_draw(random.randint(5000), 0).convert_alpha()#
        self.grass = pygame.image.load(directory + "/Boat_images/grass3.png").convert_alpha()
        self.house1 = pygame.image.load(directory + "/Boat_images/mini_mini_houses.png").convert_alpha()
        self.grass_index = 0
        self.water_index = 0
        #self.grass_images = self.load_tiles(full_grass,self.grass_index)
        #self.water_images = self.load_tiles(full_water,self.water_index)
        self.tile_size = 32
        self.wtiles = winw*3/self.tile_size
        self.htiles = winh*3/self.tile_size
        i = 0
        self.row = i//self.wtiles
        self.col = i - self.row*self.wtiles
        self.maximum_row = self.htiles
        self.maximum_col = self.wtiles

        self.source = 100
        self.map_tiles = self.create_map()
        self.random_source_tiles = self.create_source_islands2(self.map_tiles)
        print(self.random_source_tiles)
        gaia.Gaia(self.random_source_tiles)
        self.create_grass(self.random_source_tiles,self.map_tiles)
        self.house_list = self.create_houses()

    def get_map_tiles(self,col,row):
        tile_pos = int(row*self.wtiles + col)
        return tile_pos

    def get_col_row(self,tile_pos):
        row = tile_pos//self.wtiles
        col = tile_pos - row*self.wtiles
        return col,row

    def get_adjacent(self,col,row):
        el = col,row
        list = [[el[0]-1,el[1]-1],[el[0],el[1]-1],[el[0]+1,el[1]-1],[el[0]-1,el[1]],[el[0]+1,el[1]],[el[0]-1,el[1]+1],[el[0],el[1]+1],[el[0]+1,el[1]+1]]
        return list

    def draw_grid(self):
        for x in range(0, winw, self.tile_size):
            pygame.draw.line(win,(255,255,255), (x,0), (x,winh))
        for y in range(0, winh, self.tile_size):
            pygame.draw.line(win,(255,255,255), (0,y), (winw,y))

    def create_map(self):
        list = []
        while len(list) < 7200:
            ap = "w"
            list.append(ap)
        return list

    def create_source_islands2(self,list):
        list2 = []
        for i in range (self.source):
            x = random.randint(0,self.maximum_col-1)
            y = random.randint(0,self.maximum_row-1)
            list2.append([x,y])
            list[self.get_map_tiles(x,y)] = "g"
        return list2 #[[x,y],[x',y']

    def create_source_islands(self):
        col, row = (winw+winw/2)//self.tile_size,(winh+winh/2)//self.tile_size
        list = [[int(col),int(row)]]
        return list


    def create_grass(self,list,list2):
        for el in list:
            if el[0] < self.maximum_col and el[1] < self.maximum_row:
                list2[self.get_map_tiles(el[0],el[1])] = "g"




    def load_tiles(self,spritesheet,index):
        list = []
        for x in range(spritesheet.totalCellCount):
            list.append(spritesheet.output_draw(int(index), 0))
            index += 1
        print(list)
        index = 0
        return list



    def create_houses(self):
        house_list = []
        occupied_list = []
        for (i,el) in enumerate(self.map_tiles):
            counter = 0
            if el == "g":
                col,row = self.get_col_row(i)
                adjacent_list = self.get_adjacent(col,row)
                for el2 in adjacent_list:
                    tile_pos = self.get_map_tiles(el2[0],el2[1])
                    print(adjacent_list, tile_pos)
                    if tile_pos >=0 and tile_pos < len(self.map_tiles):
                        if self.map_tiles[tile_pos] == "g"  and el2 not in occupied_list:
                            counter += 1
            if counter == 8:
                for el in adjacent_list:
                    occupied_list.append(el)
                house_list.append([col,row])
        return house_list
                #win.blit(self.house1,(col*32,row*32))#(col*32 + camera.pos.x*-1,row*32 + camera.pos.y*-1))

    def draw_houses(self,win,camera):
        for el in self.house_list:
            #col,row = self.get_col_row(el[0]-1,el[1]-1)
            col = el[0]-1
            row = el[1]-1
            win.blit(self.house1,(col*32 + camera.pos.x*-1,row*32 + camera.pos.y*-1))


    def get_in_camera(self,camera):
        list = []
        col,row = camera.pos.x//self.tile_size,camera.pos.y//self.tile_size
        for x in range(winw//self.tile_size):
            for y in range(winh//self.tile_size):
                list.append([col+x,row+y])
        return list

    def camera_collision(self,camera,image):
        for el in in_camera:
            cameraRect = pygame.Rect(camera.pos.x, camera.pos.y, winw, winh)
            objRect = image.get_rect()
            xa,ya = self.col*self.tile_size,self.row*self.tile_size
            objRect.topleft = xa,ya
            if objRect.colliderect(cameraRect):
                return True
            else:
                False


    def draw(self,win,camera):
        in_camera = self.get_in_camera(camera)
        for el in in_camera:
            col = el[0]
            row = el[1]
            tile = self.map_tiles[self.get_map_tiles(col,row)]
            if tile == "w":
                blit = self.water
            if tile == "g":
                blit = self.grass
            x,y = col*self.tile_size+camera.pos.x*-1,row*self.tile_size+camera.pos.y*-1
            win.blit(blit,(x,y))


map = Map()
