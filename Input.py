class Input(Player_class):
    def __init__(self):
        self.button1 = 0
        self.button2 = 0
        self.button3 = 0
        self.chosen_tile = "w"
        self.handle_mouse(camera)

    def handle_mouse(self,camera):
        x,y = pygame.mouse.get_pos()
        self.mouse_x_relative = x +camera.pos.x
        self.mouse_y_relative = y + camera.pos.y
        #self.row = i//self.wtiles
        #self.col = i - self.row*self.wtiles
        col = self.mouse_x_relative//map.tilesize
        row = self.mouse_y_relative//map.tilesize
        i = map.get_map_tiles(col,row)
        self.mousei = i


    def mouse_pressed(self):
        self.button1,self.button2,self.button3 = pygame.mouse.get_pressed()
        col, row = map.get_col_row(self.mousei)

        if self.button1 == 1:
            if self.boat_drop == False:
                if map.map_tiles[self.mousei] != self.chosen_tile:
                    map.map_tiles[self.mousei] = self.chosen_tile
                    if self.chosen_tile != ("s" and "f"):
                        map.terrain.append((col,row))
                if self.chosen_tile == "s":
                    if (col,row) not in map.start_list:
                        map.start_list.append((col,row))
                if self.chosen_tile == "f":
                    if (col,row) not in map.finish_list:
                        map.finish_list.append((col,row))
            else:
                map.boat_list.append(Player(self.mouse_x_relative,self.mouse_y_relative))

        if self.button3 == 1:
            if map.map_tiles[self.mousei] != "w":
                map.map_tiles[self.mousei] = "w"
                if (col,row) in map.terrain:
                    map.terrain.remove((col,row))
                if (col,row) in map.start_list:
                    map.start_list.remove((col,row))
                if (col,row) in map.finish_list:
                    map.finish_list.remove((col,row))
