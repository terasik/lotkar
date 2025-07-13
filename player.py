# hier will be player class

import arcade 
from defs import *
from hare import Hare

class Player:

    def __init__(self, nr, color, **kwargs):
        self.hare_sprite_list=arcade.SpriteList()
        self.color=color
        self.nr=nr


    def setup(self):
        # setup hares
        for h in range(PLAYER_HARE_CNT):
            hare_sprite=Hare(self.color, h+1)
            hare_sprite.position=((1+self.nr)*50*(1+h), (1+self.nr)*50*(1+h))
            self.hare_sprite_list.append(hare_sprite)

    @classmethod
    def setup_boundaries(cls):
        cls.boundary_list=arcade.shape_list.ShapeElementList()
        # vertical boundary
        vert_shape=arcade.shape_list.create_line(CELLS_FIELD_WIDTH,
                                                 0,
                                                 CELLS_FIELD_WIDTH,
                                                 WINDOW_HEIGHT,
                                                 BOUNDARY_LINE_COLOR,
                                                 BOUNDARY_LINE_WIDTH)
        cls.boundary_list.append(vert_shape)
        for p in range(PLAYER_CNT+1):
            y=(WINDOW_HEIGHT*p)//PLAYER_CNT
            hor_shape=arcade.shape_list.create_line(CELLS_FIELD_WIDTH,
                                                    y,
                                                    WINDOW_WIDTH,
                                                    y,
                                                    BOUNDARY_LINE_COLOR,
                                                    BOUNDARY_LINE_WIDTH)
            cls.boundary_list.append(hor_shape)
            

