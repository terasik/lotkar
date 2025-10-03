"""
file with constants
"""
from arcade import color

# window contants
WINDOW_WIDTH=1280
WINDOW_HEIGHT=720
WINDOW_TITLE = "Lotti Karrotti"

# cells constants
CELL_SPACE=20
CELLS_FIELD_WIDTH=WINDOW_WIDTH*3//4
CELL_CNT=26
CELL_DANGEROUS=(3,6,9, 12, 15, 18, 20, 22)
CELL_RADIUS=50

# players
#PLAYER_CNT=2
PLAYER_CNT_MAX=4
PLAYER_CNT_MIN=1

# boundaries
BOUNDARY_LINE_WIDTH=5
BOUNDARY_LINE_COLOR=color.BABY_BLUE

# players text
TEXT_SPACE=5
TEXT_X_OFFSET=BOUNDARY_LINE_WIDTH+5
TEXT_Y_OFFSET=BOUNDARY_LINE_WIDTH+5
TEXT_SIZE=16
TEXT_FONT_SIZE=(TEXT_SIZE*3)//4

# hares
HARE_CNT_MIN=1
HARE_CNT_MAX=4
HARE_WIDTH_ORIG=256
HARE_HEIGHT_ORIG=341
HARE_SPACE=5
HARE_COLORS=["blue",
             "lila",
             "red",
             "green",
             "orange",
             "yellow",
             "black"]

# tests
TEST_POS=[(0,16, 24), (3, 9, 17)]

# game
GAME_STATUS_SPRITE_HEIGHT=80
GAME_RESET_TIME=10

# cards
CARD_TYPE_CNT=4
CARD_SIZE=(67,66)
CARD_TIME_CHANGE=0.2
CARD_TIME_END=3.0
CARD_CNT=[23, 7, 3, 10]

# bkg
BKG_PIC_NORM="resources/bkg_norm.png"
BKG_PIC_WON="resources/bkg_won.png"
