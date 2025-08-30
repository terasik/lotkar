# hare class
# hare 256x341 -> 64x85
import logging
import arcade
from defs import *

class Hare(arcade.Sprite):

    def __init__(self, color, nr, player_nr, **kwargs):
        logging.info("init Hare instanz mit color=%s nr=%s pl_nr=%s", color, nr, player_nr)
        self.hare_color=color
        self.nr=nr
        self.player_nr=player_nr
        self.available=True
        self.cell_nr=-1
        self.on_play=False
        self.move_ready=False
        self.init_scale=0.23
        self.init_width=64
        self.init_height=85
        self.cell_scale=2*CELL_RADIUS/HARE_HEIGHT_ORIG
        #self.new_position=self.calc_init_position()
        self.calc_init_wh()
        self.new_position=self.calc_init_position()
        texture=arcade.load_texture(f"resources/rabbit_{color}_{nr}.png")
        super().__init__(texture, scale=self.init_scale, **kwargs)

    def calc_init_wh(self):
        """ calculate init width and height of hare pics """
        max_width=(WINDOW_WIDTH-CELLS_FIELD_WIDTH-2*BOUNDARY_LINE_WIDTH)//PLAYER_HARE_CNT -\
                HARE_SPACE*PLAYER_HARE_CNT - 5
        max_height=WINDOW_HEIGHT//PLAYER_CNT-100
        scale_x=max_width/HARE_WIDTH_ORIG
        scale_y=max_height/HARE_HEIGHT_ORIG
        #print(f"scale_x={scale_x} scale_y={scale_y}")
        self.init_scale = scale_y if scale_x > scale_y else scale_x
        self.init_width=int(self.init_scale*HARE_WIDTH_ORIG)
        self.init_height=int(self.init_scale*HARE_HEIGHT_ORIG)
        #print(f"max_width={max_width} scale={self.init_scale} new_width={self.init_width} new_height={self.init_height}")


    def calc_init_position(self):
        x=CELLS_FIELD_WIDTH+BOUNDARY_LINE_WIDTH+\
                (self.init_width//2)+(self.nr-1)*(self.init_width+HARE_SPACE)
        y=WINDOW_HEIGHT-((WINDOW_HEIGHT*(self.player_nr+1))//PLAYER_CNT)+\
                BOUNDARY_LINE_WIDTH+HARE_SPACE//2+(self.init_height//2)
        #print(f"hare nr={self.nr} pl={self.player_nr} init_x={x} init_y={y}")
        return (x, y)

    def set_init_position(self):
        self.position=self.calc_init_position()
        #print(f"hare nr={self.nr} pl={self.player_nr} position={self.position}")

    def rescale_to_cell(self):
        self.scale=self.cell_scale

    def calc_velocity(self, now, end):
        abs_dif=abs(end-now)
        if abs_dif > 100:
            return 5
        elif abs_dif > 50 and abs_dif < 100:
            return 3
        elif abs_dif > 10 and abs_dif < 50:
            return 2
        else:
            return 1
        
         

    def move_to_cell(self):
        end_x=self.new_position[0]
        end_y=self.new_position[1]
        x_velo=self.calc_velocity(self.center_x, end_x)
        y_velo=self.calc_velocity(self.center_y, end_y)
        if self.center_x!=end_x and self.center_y!=end_y:
            self.move_ready=False
        if self.center_x>end_x:
            self.center_x-=x_velo
        elif self.center_x<end_x:
            self.center_x+=x_velo
        else:
            if self.center_y>end_y:
                self.center_y-=y_velo
            elif self.center_y<end_y:
                self.center_y+=y_velo
            else:
                self.move_ready=True

    def update(self, delta_time):
        self.move_to_cell()










