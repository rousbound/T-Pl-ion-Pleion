import pygame
import math
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

winw = 1280
winh = 640
win = pygame.display.set_mode((winw,winh))

FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Tó Ploion Pleion')
pygame.init()
vec = pygame.math.Vector2
directory = dir_path
