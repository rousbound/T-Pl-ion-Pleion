import random
from objetos import *

def handle_objects(game,win,camera,map):
    if len(game.objects_list) < 30:
        r = random.randint(1,3)
        game.objects_list.append(base_object(directory +"/Boat_images/cloud%d.png"%r))
        for i in game.objects_list:
            i.get_off_camera_xy(camera)
            i.world_limits(camera)
            #game.rain_list.append(rain(i.x,i.y))

    for i in game.objects_list:
        i.x += 1
    """for i in game.rain_list:
        i.x += 1
        i.rain()"""


    if len(game.seaguls_list) < 30:
        game.seaguls_list.append(Seaguls(win,camera,map))
        for i in game.seaguls_list:
            i.get_off_camera_xy(camera)
            i.world_limits(camera)
    for i in game.seaguls_list:
        i.x += 2
        i.y -= 2

def draw_objects(game,win,camera,map):
    for i in game.objects_list:
        i.draw(win,camera)
    for i in game.seaguls_list:
        i.draw(win,camera,map)
    """for i in self.rain_list:
        i.draw(win,camera1)"""
