CELL_RADIUS=10
WINDOW_WIDTH=30
WINDOW_HEIGHT=70



def calc_cell_positions():
  """
  1 2 3 4 5 6
            7
          9 8
  """
  cell_diam=CELL_RADIUS*2+5
  width=int(WINDOW_WIDTH)
  max_hor_cnt=int(width/cell_diam)
  max_ver_cnt=int(WINDOW_HEIGHT/cell_diam)
  print(f"max_hor_cnt={max_hor_cnt} max_ver_cnt={max_ver_cnt}")
  ver_half=int(max_ver_cnt/2)
  max_cell_cnt=(max_hor_cnt+1)*ver_half + max_hor_cnt*(max_ver_cnt%2)
  print(f"""\
max_hor_cnt={max_hor_cnt} 
max_ver_cnt={max_ver_cnt}
max_cell_cnt={max_cell_cnt}
""")

calc_cell_positions()

