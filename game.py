# game class

#from enum import Enum
import random
import arcade
from pyglet.graphics import Batch
from defs import *

"""
class GameStMa(Enum):
    RANDOM_CARD=0
    MOVE_HARE=1
    CHECK_HARE=2
    CHECK_PLAYER=3
"""
# game states
GS_RANDOM_CARD=0
GS_WAIT_FOR_INPUT=1
GS_MOVE_HARE=2
GS_CHECK_HARE=3
GS_CHECK_PLAYER=4

"""
class GameCard(arcade.Sprite):
    def __init__(self):
        pass
"""

class GameCard(arcade.Sprite):

    def __init__(self):
        self.timer_change=0
        self.timer_end=0
        self.card_nr=0
        position=(CELLS_FIELD_WIDTH-5-CARD_SIZE[0]/2,
                              GAME_STATUS_SPRITE_HEIGHT/2)
        super().__init__(visible=False, center_x=position[0], center_y=position[1])

    def setup(self):
        self.textures=[arcade.load_texture(f"resources/card_{i+1}.png") for i in range(CARD_CNT)]




    def update(self, delta_time):
        self.timer_change+=delta_time
        self.timer_end+=delta_time
        if self.timer_change>=CARD_TIME_CHANGE:
            card_nr=random.randrange(CARD_CNT)
            self.set_texture(card_nr)
            self.timer_change=0
            self.visible=True
        #if self.timer_end>=CARD_TIME_END:
        #    self.timer_end=0
        #    self.set_texture(card_nr)
        #    self.card_nr=card_nr
            


class Game:
    """ main game class """
    def __init__(self):
        self.sprite_list=arcade.SpriteList()
        self.status_sprite=None
        self.batch=Batch()
        self.play_time=0
        # state machine vars
        self.player_active=0
        self.state=GS_RANDOM_CARD
        self.player_input=None

    def setup(self):
        # status section
        self.status_sprite=arcade.SpriteSolidColor(CELLS_FIELD_WIDTH,
                                                   GAME_STATUS_SPRITE_HEIGHT,
                                                   CELLS_FIELD_WIDTH/2,
                                                   GAME_STATUS_SPRITE_HEIGHT/2,
                                                   arcade.color.GREEN)
        self.sprite_list.append(self.status_sprite)
        # status text
        # who's turn ?
        self.text_player_active=arcade.Text("",
                                        5,
                                        GAME_STATUS_SPRITE_HEIGHT-TEXT_SIZE,
                                        font_size=TEXT_FONT_SIZE,
                                        color=arcade.color.BLACK,
                                        batch=self.batch)
        # playtime
        self.text_play_time=arcade.Text("",
                                        5,
                                        GAME_STATUS_SPRITE_HEIGHT-2*TEXT_SIZE,
                                        font_size=TEXT_FONT_SIZE,
                                        color=arcade.color.BLACK,
                                        batch=self.batch)
        # cards
        self.game_card=GameCard()
        self.game_card.setup()
        self.sprite_list.append(self.game_card)

    def update(self, delta_time):
        self.play_time+=delta_time
        self.text_play_time.text=f"Zeit: {self.play_time:.1f}s"
        self.text_player_active.text=f"Spieler: {self.player_active}"
        if self.state==GS_RANDOM_CARD:
            self.game_card.update(delta_time)
            if self.game_card.ready:
                # wait for user input 1,2,3,4
                self.state=GS_WAIT_FOR_INPUT

    def draw(self):
        self.sprite_list.draw()
        self.batch.draw()

