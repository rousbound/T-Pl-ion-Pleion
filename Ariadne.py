from queue import *
import pygame
import numpy

def get_adjacent(el):
    list = [(el[0]-1,el[1]-1),(el[0],el[1]-1),(el[0]+1,el[1]-1),(el[0]-1,el[1]),(el[0]+1,el[1]),(el[0]-1,el[1]+1),(el[0],el[1]+1),(el[0]+1,el[1]+1)]
    if (el[0] + el[1])%2 == 0:
        list.reverse()
    return list

def get_tangent_adjacent(el):
    el = int(el[0]),int(el[1])
    tuple = [(el[0]+1,el[1]),(el[0],el[1]-1),(el[0]-1,el[1]),(el[0],el[1]+1)]
    if (el[0] + el[1])%2 == 0:
        tuple.reverse()
    return tuple


def draw_rect(win,el):
    pygame.draw.rect(win,(255,255,255),(el[0]*32,el[1]*32,32,32), 2)


def get_tile_direction(path):
    path_directions = []
    for (i,el) in enumerate(path):
        if i < len(path) -1:
            #print(path[i],path[i+1])
            #x = path[i][0] - path[i+1][0]
            #y = path[i][1] - path[i+1][1]
            new_tuple = tuple(numpy.subtract(path[i], path[i+1]))
            path_directions.append((new_tuple,path[i]))
    return path_directions


def heuristic(a, b):
   return abs(a[0] - b[0]) + abs(a[1] - b[1])



def Ariadne(win,start,goal,terrain):
    frontier = Queue()
    frontier.put(start, 0)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()
        #print("Queue:", frontier)
        if current == goal:
           break
        neighbors = get_tangent_adjacent(current)
        for next in neighbors: #get_Adjacent
            if next not in came_from:
                if list(next) not in terrain:
                    print("goal:",goal,"next:",next)
                    priority = heuristic(goal,next)
                    frontier.put(next,priority)
                    came_from[next] = current

    #print("Came From:", came_from)
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    #print("Path:", path)
    return path
