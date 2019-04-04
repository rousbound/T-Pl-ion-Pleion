import pygame
import random
from settings import*
class Gaia():

    def __init__(self):
        self.tilesize = 32
        self.wtiles = winw*3/self.tilesize
        self.htiles = winh*3/self.tilesize
        tile_pos = 0
        self.row = tile_pos//self.wtiles
        self.col = tile_pos - self.row*self.wtiles
        self.maximum_row = self.htiles
        self.maximum_col = self.wtiles
        self.tile_limit = 1000

    def debug_mode(self,x):
        #if x == 0:
            #print("map tiles: ",self.map_tiles)
        if x == 1:
            print("random source tiles list:",self.random_source_tiles)
        if x == 2:
            print("adjacent list:", "lenght:", len(self.adjacent_list), self.adjacent_list)
        if x == 3:
            print("counter_adjacent_list: ", "lenght:", len(self.counter_adjacent_list), self.counter_adjacent_list)
        if x == 4:
            print("central counter list: ",self.central_counter_list)
        if x == 5:
            print(" reconstructed_list:","lenght:",len(self.reconstructed_list),self.reconstructed_list)
        if x == 6:
            print("indexed adjacent list:","lenght:",len(self.indexed_adjacent_list),self.indexed_adjacent_list)
        if x == 7:
            print(" sorted indexed adjacent list:","lenght:",len(self.sorted_list),self.sorted_list)
            pass
        pass



    def draw_grid(self):
        for x in range(0, winw, self.tilesize):
            pygame.draw.line(win,(255,255,255), (x,0), (x,winh))
        for y in range(0, winh, self.tilesize):
            pygame.draw.line(win,(255,255,255), (0,y), (winw,y))


    def create_map(self):
        list = []
        while len(list) < 7200:
            ap = "w"
            list.append(ap)
        return list

    def get_map_tiles(self,col,row):
        tile_pos = int(row*self.wtiles + col)
        return tile_pos

    def get_col_row(self,tile_pos):
        row = tile_pos//self.wtiles
        col = tile_pos - row*self.wtiles
        return col,row



    def get_adjacent(self,col,row):
        el = col,row
        list = [[el[0]-1,el[1]-1],[el[0],el[1]-1],[el[0]+1,el[1]-1],[el[0]-1,el[1]],[el[0]+1,el[1]],[el[0]-1,el[1]+1],[el[0],el[1]+1],[el[0]+1,el[1]+1]]
        return list

    def busca(self,el2,list,index):
        for (i,el3) in enumerate(list):
            if el3[index] == el2:
                #print(i)
                return i
        return None

    def busca2(self,el2,list): #list = [[[[[53, 39], 0], [[54, 39], 0], [[55, 39], 0], [[53, 40], 0], [[55, 40], 0], [[53, 41], 0], [[54, 41], 0], [[55, 41], 0]]]]
        for (i,el3) in enumerate(list):
            for el4 in el3:
                if el4[0] == el2:
                    #print(i)
                    return i
        return None



    def create_source_islands(self,list):
        list2 = []
        for i in range (100):
            x = random.randint(0,self.maximum_col-1)
            y = random.randint(0,self.maximum_row-1)
            list2.append([x,y])
            list[self.get_map_tiles(x,y)] = "g"
        return list2 #[[x,y],[x',y']

    def create_adjacent_list(self,list): #AL
        final_list = []
        for el in list:
            eights_list = []
            temp_list = self.get_adjacent(el[0],el[1])
            for el2 in temp_list:
                eights_list.append(el2)
            final_list.append(eights_list)
        return final_list  # [ [[x-1][y-1]]...., [[x+1][y+1]] ],  [ [[x'-1][y'-1]]...., [[x'+1][y'+1]] ]


    def create_counter_adjacent_list(self,list): #cAL
        final_list = []
        for el in list:
            for el2 in el:
                pos = self.busca(el2,final_list,0)
                if pos != None:
                    final_list[pos][1] += 1
                    final_list[pos][2] += 1
                else:
                    final_list.append([el2,0,0])
        return final_list


    def reconstruct_adjacent_list(self,adjacent_list,counter_adjacent_list): #ficaria melhor invertido a checagem, para organizar a lista ouput como a adjacent list e a source list
        list1 = adjacent_list
        list2 = counter_adjacent_list
        reconstructed_list = list3 = []
        while len(list2) != 0:
            for el in list1:
                eights = []
                for el2 in el:
                    #print(el2)
                    for el3 in list2:
                        if el2 == el3[0]:
                            eights.append([el3[0],el3[1]])
                            if el3[2] == 0:
                                list2.remove(el3)
                            else:
                                el3[2] -= 1
                list3.append(eights)
        return list3




    def create_eights_counter_adjacent_list(self,list):
        print(len(list))
        list_copy = list
        print(list_copy), print(len(list_copy))
        full_list = []
        while (len(list_copy) != 0):
            eights_list = []
            for i in range(8):
                print(i)
                eights_list.append(list_copy[i])
                print(eights_list)
            for i in range(8):
                del list_copy[0]
            print(list_copy)
            full_list.append(eights_list)
        print("full list:",full_list)
        return full_list


    def get_central_counter_list(self,list1,list2): #random_source_tiles, self.counter_adjacent_list
        central_counter_list = []
        for el in list1:
            counter = 0
            adjacent = self.get_adjacent(el[0],el[1])
            for el2 in adjacent:
                for el3 in list2:
                    if el2 == el3[0]:
                        counter += el3[1]
            central_counter_list.append([el,counter])
        return central_counter_list


    def index_adjacent_list(self,list1,list2): # self.central_counter_list + self.reconstructed_list
        final_list = []
        for (i,el1) in enumerate(list1):
                final_list.append([el1,list2[i]])
        return final_list


    def complex_sort(self,list):
        for el in list:
            exchanges = True
            passnum = len(el[1])-1
            while passnum > 0 and exchanges:
                exchanges = False
                for i in range(passnum):
                    if el[1][i][1] < el[1][i+1][1]:
                        exchanges = True
                        temp = el[1][i][1]
                        el[1][i][1] = el[1][i+1][1]
                        el[1][i+1][1] = temp
                passnum = passnum-1
        return list


    def get_choices(self,el,ti): # da pra simplificar isso aqui transformando em n_list
        n_list = []
        choices = []
        for x in el:
            n_list.append(x[1])
        for x in el:
            choices.append(x[0])
        rand = random.randint(0,ti-1)
        print("n_list",n_list)
        print("choices:", choices )
        print("rand:", rand)
        x = el
        if 0 <= rand < el[0][1]:
            chosen = el[0][0]
        if el[0][1] <= rand < el[0][1]+el[1][1]:
            chosen = el[1][0]
        ela = el[0][1]+el[1][1]
        if ela <= rand < ela + el[2][1]:
            chosen = el[2][0]
        elb = ela + el[2][1]
        if elb <= rand < elb + el[3][1]:
            chosen = el[3][0]
        elc = elb + el[3][1]
        if elc <= rand < elc+ el[4][1]:
            chosen = el[4][0]
        eld = elc + el[4][1]
        if eld <= rand < eld + el[5][1]:
            chosen = el[5][0]
        ele = eld + el[5][1]
        if ele <= rand < ele + el[6][1]:
            chosen = el[6][0]
        elf = ele + el[6][1]
        if elf <= rand < ti:
            chosen = el[7][0]
        return chosen

    def run_choices(self,list1,random_source_tiles):
        list_copy = list1
        for el in list_copy:
            el[0][1] += 8
            ti = el[0][1]
            for el2 in el[1]:
                el2[1] += 1
        #print("list copy:",list_copy)
        for indexed_list in list_copy:
            print("ti:",ti)
            choice = self.get_choices(indexed_list[1],ti)
            random_source_tiles.append(choice)
        print(random_source_tiles)
        #print("list copy:", len(list_copy))

    def Gaia(self,random_source_tiles):
        while len(random_source_tiles) < self.tile_limit:
            self.adjacent_list = self.create_adjacent_list(random_source_tiles)
            self.debug_mode(2)
            self.counter_adjacent_list = self.create_counter_adjacent_list(self.adjacent_list)
            self.debug_mode(3)
            self.central_counter_list = self.get_central_counter_list(random_source_tiles, self.counter_adjacent_list)
            self.debug_mode(4)
            self.reconstructed_list = self.reconstruct_adjacent_list(self.adjacent_list, self.counter_adjacent_list)
            self.debug_mode(5)
            self.indexed_adjacent_list = self.index_adjacent_list(self.central_counter_list,self.reconstructed_list)
            self.debug_mode(6)
            self.sorted_list = self.complex_sort(self.indexed_adjacent_list)
            self.debug_mode(7)
            self.run_choices(self.sorted_list,random_source_tiles)
        print("----DONE----")
        print("Final list:", random_source_tiles)




gaia = Gaia()
