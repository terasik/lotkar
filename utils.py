CELL_RADIUS=40
CELL_SPACE=20
WINDOW_WIDTH=1280
CELL_WINDOW_WIDTH=WINDOW_WIDTH*3//4
WINDOW_HEIGHT=720




def calc_cell_positions():
    """
    1 2 3 4 5 6
              7
            9 8
    """
    cell_diam=CELL_RADIUS*2+CELL_SPACE
    width=CELL_WINDOW_WIDTH
    max_hor_cnt=width//cell_diam
    max_ver_cnt=WINDOW_HEIGHT//cell_diam
    print(f"max_hor_cnt={max_hor_cnt} max_ver_cnt={max_ver_cnt}")
    ver_half=max_ver_cnt//2
    max_cell_cnt=(max_hor_cnt+1)*ver_half + max_hor_cnt*(max_ver_cnt%2)
    print(f"""\
max_hor_cnt={max_hor_cnt} 
max_ver_cnt={max_ver_cnt}
max_cell_cnt={max_cell_cnt}
""")
    # direction to right
    to_left=False
    d_x=CELL_WINDOW_WIDTH//max_hor_cnt
    d_y=WINDOW_HEIGHT//max_ver_cnt
    lines_with_cells=[]
    last_x=d_x*max_hor_cnt
    print(f"d_x={d_x} d_y={d_y} last_x={last_x}")
    # vertikal
    for cnt_ver in range(max_ver_cnt):
        y=d_y*(1+cnt_ver)
        print(f"cnt_ver={cnt_ver} y={y} to_left={to_left}")
        # horizontal
        #for cnt_hor in range(max_hor_cnt):
        if cnt_ver%2:
            lines_with_cells.append([last_x, y])
        else:
            for x in range(max_hor_cnt):
                if not to_left:
                    lines_with_cells.append([d_x*(1+x), y])
                else:
                    lines_with_cells.append([last_x-(d_x*x), y])
            to_left=not to_left
    print(lines_with_cells)
            


calc_cell_positions()

