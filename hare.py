# hare class
# hare 256x341 -> 64x85
import arcade
from defs import *

class Hare(arcade.Sprite):

    def __init__(self, color, nr, player_nr, **kwargs):
        self.hare_color=color
        self.nr=nr
        self.player_nr=player_nr
        self.available=True
        self.on_play=False
        self.calc_start_position()
        texture=arcade.load_texture(f"resources/rabbit_{color}_{nr}.png")
        super().__init__(texture, scale=0.25, **kwargs)

    def calc_start_position(self):
        start_x=CELLS_FIELD_WIDTH+BOUNDARY_LINE_WIDTH+HARE_SPACE
        max_width=(WINDOW_WIDTH-CELLS_FIELD_WIDTH-2*BOUNDARY_LINE_WIDTH)//PLAYER_HARE_CNT -\
                HARE_SPACE*PLAYER_HARE_CNT - 5
        scale=max_width/HARE_WIDTH_ORIG
        new_width=int(scale*HARE_WIDTH_ORIG)
        new_height=int(scale*HARE_HEIGHT_ORIG)
        start_x=start_x+(new_width//2)+(self.nr-1)*(new_width+HARE_SPACE)
        start_y=WINDOW_HEIGHT-((WINDOW_HEIGHT*(self.player_nr+1))//PLAYER_CNT)+\
                BOUNDARY_LINE_WIDTH+HARE_SPACE+(new_height//2)
        print(f"hare : max_width={max_width} scale={scale} new_width={new_width} new_height={new_height}")
        print(f"hare: start_x={start_x} start_y={start_y}")





