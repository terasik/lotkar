# hier will be player class

import logging
import arcade 
from pyglet.graphics import Batch
from defs import *
from hare import Hare

"""
TEXT_SPACE=10
TEXT_X_OFFSET=BOUNDARY_LINE_WIDTH+5
TEXT_Y_OFFSET=BOUNDARY_LINE_WIDTH+5
TEXT_SIZE=22
TEXT_FONT_SIZE=(TEXT_SIZE*3)//4
"""
SOME_NAMES=["Lakimurq", "Avande", "Huzret", "Lerfa"]

class Player:

    status_sprite_list=arcade.SpriteList()

    def __init__(self, nr, color, **kwargs):
        logging.info("init Player instanz mit nr=%s color=%s", nr, color)
        self.hare_sprite_list=arcade.SpriteList()
        self.color=color
        self.nr=nr
        self.name=kwargs.get("name", SOME_NAMES[nr])
        self.batch=Batch()
        # player nr text
        self.text_nr=None
        self.text_hares_alive=None
        self.text_hares_win=None
        self.text_hares_dead=None
        self.hares_alive=PLAYER_HARE_CNT
        self.hares_win=0
        self.hares_dead=0

    def setup(self):
        # setup hares
        for h in range(PLAYER_HARE_CNT):
            hare_sprite=Hare(self.color, h+1, self.nr)
            #hare_sprite.position=((1+self.nr)*50*(1+h), (1+self.nr)*50*(1+h))
            hare_sprite.set_init_position()
            self.hare_sprite_list.append(hare_sprite)
        # setup text
        text_y=WINDOW_HEIGHT-((WINDOW_HEIGHT*self.nr)//PLAYER_CNT)-TEXT_SIZE-TEXT_Y_OFFSET
        text_x=CELLS_FIELD_WIDTH+TEXT_X_OFFSET
        #print(f"text_x={text_x}, text_y={text_y}")
        self.text_nr=arcade.Text(f"Spieler {self.nr+1}: {self.name}", 
                                    text_x, 
                                    text_y,
                                    font_size=TEXT_FONT_SIZE,
                                    color=arcade.color.BLACK,
                                    batch=self.batch)
        text_y=text_y-(TEXT_SIZE+TEXT_SPACE)
        self.text_hares_alive=arcade.Text(f"Hasen verfügbar: {PLAYER_HARE_CNT}", 
                                    text_x, 
                                    text_y, 
                                    font_size=TEXT_FONT_SIZE,
                                    color=arcade.color.BLACK,
                                    batch=self.batch)
        text_y=text_y-(TEXT_SIZE+TEXT_SPACE)
        self.text_hares_win=arcade.Text(f"Hasen gewonnen: 0", 
                                    text_x, 
                                    text_y, 
                                    font_size=TEXT_FONT_SIZE,
                                    color=arcade.color.BLACK,
                                    batch=self.batch)
        text_y=text_y-(TEXT_SIZE+TEXT_SPACE)
        self.text_hares_dead=arcade.Text(f"Hasen ins Loch gefallen: 0", 
                                    text_x, 
                                    text_y, 
                                    font_size=TEXT_FONT_SIZE,
                                    color=arcade.color.BLACK,
                                    batch=self.batch)


    def update(self, delta_time):
        self.hare_sprite_list.update(delta_time)
        self.text_hares_alive.text=f"Hasen verfügbar: {self.hares_alive}"
        self.text_hares_win.text=f"Hasen gewonnen: {self.hares_win}"
        self.text_hares_dead.text=f"Hasen ins Loch gefallen: {self.hares_dead}"

    @classmethod
    def setup_boundary_shapes(cls):
        #cls.boundary_list=arcade.shape_list.ShapeElementList()
        cls.boundary_shape_list=arcade.shape_list.ShapeElementList()
        # vertical boundary
        vert_shape=arcade.shape_list.create_line(CELLS_FIELD_WIDTH,
                                                 0,
                                                 CELLS_FIELD_WIDTH,
                                                 WINDOW_HEIGHT,
                                                 BOUNDARY_LINE_COLOR,
                                                 BOUNDARY_LINE_WIDTH)
        cls.boundary_shape_list.append(vert_shape)
        for p in range(PLAYER_CNT+1):
            y=(WINDOW_HEIGHT*p)//PLAYER_CNT
            hor_shape=arcade.shape_list.create_line(CELLS_FIELD_WIDTH,
                                                    y,
                                                    WINDOW_WIDTH,
                                                    y,
                                                    BOUNDARY_LINE_COLOR,
                                                    BOUNDARY_LINE_WIDTH)
            cls.boundary_shape_list.append(hor_shape)

    @classmethod
    def setup_status_sprites(cls):
        for p in range(PLAYER_CNT):
            player_area=arcade.SpriteSolidColor(WINDOW_WIDTH//4,
                                                WINDOW_HEIGHT//PLAYER_CNT,
                                                WINDOW_WIDTH*7//8,
                                                WINDOW_HEIGHT*p//PLAYER_CNT+WINDOW_HEIGHT//(PLAYER_CNT*2),
                                                arcade.color.WHITE)
            cls.status_sprite_list.append(player_area)
            

