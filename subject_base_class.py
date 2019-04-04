import pygame
from settings import *


class subject_base_class():
    def __init__(self,x,y,up,down,right,left):
        self.x = x
        self.y = y
        self.acc = vec(0,0)
        self.vel = vec(0,0)
        self.pos = vec(self.x,self.y)
        self.up = up
        self.down= down
        self.right = right
        self.left = left
        self.maximum_values = vec(10,10)
        self.image = "null"


    def debug_mode(self):
        print("Player:  ", "Acc:", self.acc, "Vel:", self.vel, "Pos:", self.pos)


    def draw(self):
        win.blit(self.image,(self.pos + camera1.pos*-1))


    def handle_controls(self):
        keys = pygame.key.get_pressed()
        self.acc = vec(0,0)
        if keys[self.up]:
            self.acc.y = -self.player_acc
        if keys[self.down]:
            self.acc.y = self.player_acc
        if keys[self.left]:
            self.acc.x = -self.player_acc
        if keys[self.right]:
            self.acc.x = self.player_acc

    def dynamics(self):
        self.vel += self.acc
        self.vel *= 0.95
        self.pos += self.vel

    def limits(self):
        if self.acc.x >= self.maximum_values.x:
            self.acc.x = self.maximum_values.x
        if self.acc.y >= self.maximum_values.y:
            self.acc.y = self.maximum_values.y
        if self.vel.x >= self.maximum_values.x:
            self.vel.x = self.maximum_values.x
        if self.vel.y >= self.maximum_values.y:
            self.vel.y = self.maximum_values.y
