import pygame
from settings import *
from subject_base_class import *
from spritesheet import *
from Ariadne import *
from map_class import*

class Player(subject_base_class):
    def __init__(self,x,y,up,down,right,left,map):
        super().__init__(x,y,up,down,right,left)
        self.acc = vec(0,0)
        self.vel = vec(0,0)
        self.pos = vec(self.x,self.y)

        self.cellindex = 0
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
        self.boat = boat_right
        self.player_acc = 0.5
        self.mastro_angle = 0
        self.health = 390
        self.map = map
        self.atributes(self.map)


        self.button1 = 0
        self.button2 = 0
        self.button3 = 0
        self.actual_tile = (self.col,self.row)
        self.dest_tile = (self.col,self.row)
        self.path = []
        self.pathing = False

    def debug_mode(self):
        print("Player:  ", "Acc:", self.acc, "Vel:", self.vel, "Pos:", self.pos)
        #print(self.cellindex//9)
        #print("up:",self.moving_up,"down:",self.moving_down,"right",self.moving_right,"left:",self.moving_left)
        #print(self.boat)
        print(self.health)

    def dynamics(self):

        self.vel += self.acc
        self.vel *= 0.95
        self.pos += self.vel

    def atributes(self,map):
        self.image = self.boat.output_draw(int(self.cellindex%9))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.half_rect = pygame.Rect(self.rect.left,self.rect.centery,self.rect.w,self.rect.h/2)
        self.col = self.half_rect.left//map.tile_size
        self.row = self.half_rect.top//map.tile_size
        self.col_row = (self.col,self.row)
        self.i = map.get_map_tiles(self.col,self.row)
        self.adjacent_list = map.get_adjacent(self.col,self.row)


    def handle_keyboard_controls(self):
        keys = pygame.key.get_pressed()
        if keys[self.up]:
            self.moving_up = True
        if keys[self.down]:
            self.moving_down = True
            #self.acc.y = self.player_acc
        if keys[self.left]:
            self.moving_left = True
            #self.acc.x = -self.player_acc
            self.mastro_angle += 2
        if keys[self.right]:
            self.moving_right = True
            #self.acc.x = self.player_acc
            self.mastro_angle -= 2

    def handle_direction(self):
        self.acc = vec(0,0)
        if self.moving_up  == True:
            self.acc.y = -self.player_acc
            #self.vel.y = -self.player_vel
            #self.pos.y -= self.player_vel
        if self.moving_down == True:
            self.acc.y = self.player_acc
            #self.vel.y = self.player_vel
            #self.pos.y += self.player_vel
        if self.moving_right == True:
            self.acc.x = self.player_acc
            #self.vel.x = self.player_vel
            #self.pos.x += self.player_vel
        if self.moving_left == True:
            self.acc.x = -self.player_acc
            #self.vel.x = -self.player_vel
            #self.pos.x -= self.player_vel
        print("up:",self.moving_up,"down:",self.moving_down,"right:",self.moving_right,"left:",self.moving_left)
        self.draw_direction()
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    def handle_direction_change(self):
        if int(self.vel.x)>0:
            self.moving_right = True
            self.moving_left = False
        elif int(self.vel.x) <0:
            self.moving_right = False
            self.moving_left = True
        elif int(self.vel.x) == 0:
            self.moving_left = False
            self.moving_right = False

        if int(self.vel.y)<0:
            self.moving_up = True
            self.moving_down = False
        elif int(self.vel.y)>0:
            self.moving_up = False
            self.moving_down = True
        elif int(self.vel.y) == 0:
            self.moving_up = False
            self.moving_down = False


    def draw_direction(self):
        if self.moving_up and self.moving_right == True:
            self.boat = boat_up_diagonal
        elif self.moving_down and self.moving_right == True:
            self.boat = boat_down_diagonal
        elif self.moving_up and self.moving_left == True:
            self.boat = boat_up_diagonal
        elif self.moving_down and self.moving_left == True:
            self.boat = boat_down_diagonal
        elif self.moving_up  == True:
            self.boat = boat_up
        elif self.moving_down == True:
            self.boat = boat_down
        elif self.moving_right == True:
            self.boat = boat_right
        elif self.moving_left == True:
            self.boat = boat_right


    def draw_player(self,surface,camera):
        self.relative_pos = vec(self.pos.x+camera.pos.x*-1,self.pos.y+camera.pos.y*-1)
        self.image = self.boat.output_draw(int(self.cellindex%9))
        if self.vel.x >= 0:
            blit = self.image
        else:
            blit = pygame.transform.flip(self.image, True, False)
        win.blit(blit,(self.relative_pos.x,self.relative_pos.y))
        self.cellindex += 1/8



    def draw(self,win,camera):
        self.draw_player(win,camera)
        self.draw_path(win,camera,map,self.actual_tile,self.dest_tile,self.path)

    def collision(self,map):
        for el in self.adjacent_list:
            i = map.get_map_tiles(el[0],el[1])
            el_rect = pygame.Rect(el[0]*map.tile_size,el[1]*map.tile_size,32,32)
            if self.half_rect.colliderect(el_rect) and map.map_tiles[i] == "g":
                self.health -= abs(self.vel.x+self.vel.y)*10
                self.vel.x *= 0.05
                self.vel.y *= 0.05



    def setup(self,camera,map):
        self.dynamics()
        self.handle_keyboard_controls()
        self.handle_direction()
        #self.handle_direction_change()
        self.atributes(map)
        self.limits()
        self.collision(map)
        self.input_setup(camera,map)




    def handle_mouse(self,camera):
        x,y = pygame.mouse.get_pos()
        self.mouse_x_relative = x +camera.pos.x
        self.mouse_y_relative = y + camera.pos.y
        col = self.mouse_x_relative//map.tile_size
        row = self.mouse_y_relative//map.tile_size
        i = map.get_map_tiles(col,row)
        self.mousei = i


    def mouse_pressed(self):
        self.button1,self.button2,self.button3 = pygame.mouse.get_pressed()
        col, row = map.get_col_row(self.mousei)
        if self.button1 == 1:
            self.dest_tile = (col,row)
            self.pathing = True


    def path_finder(self,map):
        self.actual_tile = (self.col,self.row)
        print("path:",self.path)
        if self.actual_tile == self.dest_tile:
            self.path = []
            self.pathing = False
        else:
            if self.pathing == True:
                self.path = Ariadne(win,self.actual_tile,self.dest_tile,tuple(map.random_source_tiles))

    def collide_directions(self, map):
        path_directions = get_tile_direction(self.path)
        for el in self.adjacent_list:
            for el2 in path_directions:
                if tuple(el) == el2[1]:
                    self.get_directions(el2[0])

    def get_directions(self,el):
        if el[0] == -1:
            self.moving_right = True
            self.moving_left = False
        if el[0] == 1:
            self.moving_left = True
            self.moving_right = False
        if el[1] == -1:
            self.moving_down = True
            self.moving_up = False
        if el[1] == 1:
            self.moving_up = True
            self.moving_down = False

    def draw_path(self,win,camera,map,start,finish,path):
        path_pixels = []
        for el in path:
            path_pixels.append([(el[0]*map.tile_size)-camera.pos.x+map.tile_size/2,(el[1]*map.tile_size)-camera.pos.y+map.tile_size/2])
        for (i,el) in enumerate(path_pixels):
            if i < len(path_pixels)-1:
                el2 = path_pixels[i+1]
                pygame.draw.line(win,(255,255,255), el, el2, 5)


    def input_setup(self,camera,map):
        self.handle_mouse(camera)
        self.path_finder(map)
        self.collide_directions(map)







player1 = Player(winw+winw/2,winh+winh/2,pygame.K_UP,pygame.K_DOWN,pygame.K_RIGHT,pygame.K_LEFT,map)
