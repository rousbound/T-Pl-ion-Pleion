import pygame
from settings import *

def draw_mastro(win,player):
    mastro = pygame.image.load(directory + "/Boat_images/mastro2.png")
    mastro_rect = mastro.get_rect()
    mastro_rect.topleft = 1035,375
    mastro_rotated = pygame.transform.rotate(mastro, player.mastro_angle)
    mastro_rotated_rect = mastro_rotated.get_rect()
    mastro_rotated_rect.center = mastro_rect.center
    win.blit(mastro_rotated,(mastro_rotated_rect.topleft))


def draw_health_bar(game,win,player):
    blit = game.health_bar.subsurface(0,0,player.health,34)
    win.blit(blit,(65,580))

def draw_GUI(game,win,player):
    draw_mastro(win,player)
    draw_health_bar(game,win,player)
