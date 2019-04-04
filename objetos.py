import pygame
from settings import *
import random
from spritesheet import *

class base_object():
    def __init__(self,image):
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
    def draw(self,win,camera):
        win.blit(self.image,(self.x+ camera.pos.x*-1,self.y + camera.pos.y*-1))


    def get_off_camera_xy(self, camera):
        # create a Rect of the camera view
        cameraRect = pygame.Rect(camera.pos.x, camera.pos.y, winw, winh)
        while True:
            x = random.randint(int(camera.pos.x - winw), int(camera.pos.x + (2 * winw)))
            y = random.randint(int(camera.pos.y- winh), int(camera.pos.y + (2 * winh)))
            # create a Rect object with the random coordinates and use colliderect()
            # to make sure the right edge isn't in the camera view.
            objRect = pygame.Rect(x, y, self.rect.w, self.rect.h)
            if not objRect.colliderect(cameraRect):
                self.x,self.y = x,y
                return

    def camera_collision(self,camera,rect,map):
        cameraRect = pygame.Rect(camera.pos.x, camera.pos.y, winw, winh)
        if rect.colliderect(cameraRect):
            return True
        else:
            False

    def world_limits(self,camera):
        world_rect = pygame.Rect(0+camera.pos.x*-1, 0+camera.pos.y*-1, winw*3, winh*3)
        x = self.x #+ camera.pos.x*-1
        y = self.y #+ camera.pos.y*-1
        objRect = pygame.Rect(x, y, self.rect.w, self.rect.h)
        if not objRect.colliderect(world_rect):
            self.get_off_camera_xy(camera)

    def debug_mode(self):
        print("object pos:",self.x,self.y)


class Seaguls(base_object):
    def __init__(self,win,camera,map):
        self.x = 0
        self.y = 0
        self.index = 0
        self.angle = -45
        self.draw(win,camera,map)


    def transform_image(self,image,angle):
        self.rect = image.get_rect()
        self.rect.topleft = self.x,self.y
        self.trans_image = pygame.transform.rotate(image, angle)
        self.trans_image_rect = self.trans_image.get_rect()
        self.trans_image_rect.center = self.rect.center
        return self.trans_image

    def draw(self,win,camera,map):
        self.image = seaguls.output_draw(self.index)
        trans_image = self.transform_image(self.image,self.angle)
        bool = self.camera_collision(camera,self.trans_image_rect,map)
        if bool:
            win.blit(trans_image,(self.x+ camera.pos.x*-1,self.y + camera.pos.y*-1))
        self.index += 1/8
