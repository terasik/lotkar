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
PLAYER_CNT=4
PLAYER_CNT_MAX=4
PLAYER_CNT_MIN=1
PLAYER_HARE_CNT=3
PLAYER_PROPS=[{"color": "red", "name": "Bruno", "arcade_color": color.AZURE}, 
              {"color": "black", "name": "Zukti", "arcade_color": color.DARK_VIOLET}, 
              {"color": "orange", "name": "Arsen", "arcade_color": color.CRIMSON }, 
              {"color": "yellow", "name": "Ganta","arcade_color": color.DARK_PASTEL_GREEN}]

# colors
# orange -> WILLPOWER_ORANGE, PORTLAND_ORANGE
# red -> CADMIUM_RED
# yellow -> YELLOW, YELLOW_ROSE
C2AC={"blue": color.AZURE,
      "lila": color.DARK_VIOLET,
      "red": color.CRIMSON,
      "green": color.DARK_PASTEL_GREEN,
      "orange": color.PORTLAND_ORANGE,
      "yellow": color.YELLOW_ROSE,
      "black": color.QUARTZ }


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
HARE_WIDTH_ORIG=256
HARE_HEIGHT_ORIG=341
HARE_SPACE=5

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

