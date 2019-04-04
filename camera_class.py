import pygame
from settings import *
from subject_base_class import *

class Camera(subject_base_class):
    def __init__(self,x,y,up,down,right,left):
        super().__init__(x,y,up,down,right,left)
        self.slack = 180
        self.player_acc = 2

    def adjust(self, player):
        if player.pos.x > self.pos.x + winw - self.slack:
            self.acc.x = self.player_acc
        if player.pos.x < self.pos.x + self.slack - player.rect.w:
            self.acc.x = -self.player_acc
        if player.pos.y > self.pos.y + winh - self.slack:
            self.acc.y = self.player_acc
        if player.pos.y < self.pos.y + self.slack - player.rect.h:
            self.acc.y = -self.player_acc
            #player.acc.x -= player.player_acc

    def debug_mode(self):
        print("Camera:  ", "Acc:", self.acc, "Vel:", self.vel, "Pos:", self.pos)

    def limits(self):
        if self.acc.x >= self.maximum_values.x:
            self.acc.x = self.maximum_values.x
        if self.acc.y >= self.maximum_values.y:
            self.acc.y = self.maximum_values.y
        if self.vel.x >= self.maximum_values.x:
            self.vel.x = self.maximum_values.x
        if self.vel.y >= self.maximum_values.y:
            self.vel.y = self.maximum_values.y
        if self.pos.x <= 0:
            self.pos.x=0
        if self.pos.y <= 0:
            self.pos.y = 0
        if self.pos.x + winw> winw*3:
            self.pos.x =  winw*2
        if self.pos.y + winh> winh*3:
            self.pos.y = winh*2

    def setup(self,player):
        camera1.dynamics()
        camera1.limits()
        camera1.handle_controls()
        camera1.adjust(player)

camera1 = Camera(winw,winh,pygame.K_w,pygame.K_s,pygame.K_d,pygame.K_a)
