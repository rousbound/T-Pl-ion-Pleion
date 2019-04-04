#!/usr/bin/env python
# -*-coding=utf-8 -*-
import pygame, math, random
from settings import *
from player_class import *
from camera_class import *
from objetos import *
from map_class import *
from Handle_objects import*
from GUI import *

class Game():
    def __init__(self):
        self.objects_list = []
        self.seaguls_list = []
        self.rain_list = []
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.bg = pygame.image.load(directory +"/Boat_images/lvl3_gui2.png")
        self.health_bar = pygame.image.load(directory +"/Boat_images/health_bar.png")
        self.mastro_rotated = 0
        #self.mastro_angle = 0
        pass

    def debug_mode(self):
        player1.debug_mode()
        pass

    def fps_counter(self):
        self.clock.tick(self.fps)
        self.win_caption = pygame.display.set_caption("Tó Ploion Pleion    FPS:%d"%self.clock.get_fps())

    def draw_screen(self):
        map.draw(win,camera1)
        map.draw_houses(win,camera1)
        player1.draw(win,camera1)
        draw_objects(self,win,camera1,map)
        win.blit(self.bg,(0,0))
        draw_GUI(self,win,player1)
        #pygame.draw.rect(win,(255,255,255), pygame.Rect(0+camera1.pos.x*-1, 0+camera1.pos.y*-1, winw*3, winh*3), 100)
        pygame.display.update()



    def setup(self):
        player1.setup(camera1,map)
        camera1.setup(player1)
        handle_objects(self,win,camera1,map)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                player1.mouse_pressed()

        self.debug_mode()
        camera1.debug_mode()
        self.fps_counter()

    def main(self):
        self.draw_screen()
        self.events()
        self.setup()


g= Game()
