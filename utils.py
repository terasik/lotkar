from defs import * 

CELL_RADIUS=45


def calc_cell_positions():
    """
    1 2 3 4 5 6
              7
            9 8
    """
    cell_diam=CELL_RADIUS*2+CELL_SPACE
    max_hor_cnt=CELLS_FIELD_WIDTH//cell_diam
    max_ver_cnt=WINDOW_HEIGHT//cell_diam
    print(f"max_hor_cnt={max_hor_cnt} max_ver_cnt={max_ver_cnt}")
    ver_half=max_ver_cnt//2
    max_cell_cnt=(max_hor_cnt+1)*ver_half + max_hor_cnt*(max_ver_cnt%2)
    print(f"max_hor_cnt={max_hor_cnt} max_ver_cnt={max_ver_cnt} max_cell_cnt={max_cell_cnt}")
    # direction to left
    to_left=False
    d_x=CELLS_FIELD_WIDTH//max_hor_cnt
    d_y=WINDOW_HEIGHT//max_ver_cnt
    lines_with_cells=[]
    last_x=d_x*max_hor_cnt-(d_x//2)
    print(f"d_x={d_x} d_y={d_y} last_x={last_x}")
    # vertikal
    for cnt_ver in range(max_ver_cnt):
        y=d_y*(1+cnt_ver)-(d_y//2)
        print(f"cnt_ver={cnt_ver} y={y} to_left={to_left}")
        # horizontal
        #for cnt_hor in range(max_hor_cnt):
        if cnt_ver%2:
            lines_with_cells.append([last_x, y])
        else:
            for x in range(max_hor_cnt):
                if not to_left:
                    lines_with_cells.append([d_x*(1+x)-(d_x//2), y])
                else:
                    lines_with_cells.append([last_x-(d_x*x), y])
            to_left=not to_left
    print(lines_with_cells)
            


def calc_cell_radius():
    """ 
    calculate cell radius from cell cnt
    """
    #max_cell_cnt=(CELLS_FIELD_WIDTH//cell_diam+1)*WINDOW_HEIGTH//(2*cell_diam) + max_hor_cnt*(max_ver_cnt%2)
    pass

calc_cell_positions()

