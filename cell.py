
from defs import *
import arcade


class Cell(arcade.SpriteCircle):
    diam=CELL_RADIUS*2+CELL_SPACE
      
    def __init__(self, nr, **kwargs):
        self.nr=nr
        self.hare=None
        self.cell_type="green"
        color=(0,255,255)

        if nr in CELL_DANGEROUS:
            self.cell_type="red"
            color=(255,0,0)
        elif nr==(CELL_CNT-1):
            self.cell_type="orange"
            color=(255,255,0)

        super().__init__( CELL_RADIUS, color, False,**kwargs)


    @classmethod
    def calc_cell_positions(cls):
        """
        1 2 3 4 5 6
                  7
                9 8
        """
        cell_diam=cls.diam
        max_hor_cnt=CELLS_FIELD_WIDTH//cell_diam
        max_ver_cnt=(WINDOW_HEIGHT-GAME_STATUS_SPRITE_HEIGHT)//cell_diam
        print(f"max_hor_cnt={max_hor_cnt} max_ver_cnt={max_ver_cnt}")
        ver_half=max_ver_cnt//2
        max_cell_cnt=(max_hor_cnt+1)*ver_half + max_hor_cnt*(max_ver_cnt%2)
        print(f"max_hor_cnt={max_hor_cnt} max_ver_cnt={max_ver_cnt} max_cell_cnt={max_cell_cnt}")
        # direction to left
        to_left=False
        cell_positions=[]
        last_x=cell_diam*max_hor_cnt-(cell_diam//2)
        last_hx=last_x
        print(f"last_x={last_x}")
        # vertikal
        for cnt_ver in range(max_ver_cnt):
            y=cell_diam*(1+cnt_ver)-(cell_diam//2)+GAME_STATUS_SPRITE_HEIGHT
            #print(f"cnt_ver={cnt_ver} y={y} to_left={to_left}")
            # horizontal
            #for cnt_hor in range(max_hor_cnt):
            if cnt_ver%2:
                cell_positions.append([last_hx, y])
            else:
                for x in range(max_hor_cnt):
                    if not to_left:
                        cell_positions.append([cell_diam*(1+x)-(cell_diam//2), y])
                    else:
                        cell_positions.append([last_x-(cell_diam*x), y])
                to_left=not to_left
                last_hx=cell_positions[-1][0]
        print(cell_positions)
        return cell_positions
            


