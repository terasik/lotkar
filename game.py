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
GS_RANDOM_HOLE=5

GS2TEXT=["Karte ziehen", "Warte auf Eingabe", "Bewege Hase", "Prüfe Hase", "Prüfe Spieler", "Schwarzes Loch"]

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
        self.ready=False
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
            if self.timer_end>=CARD_TIME_END:
                self.timer_end=0
                self.card_nr=card_nr
                self.ready=True
            


class Game:
    """ main game class """
    def __init__(self, game_view):
        self.game_view=game_view
        self.sprite_list=arcade.SpriteList()
        self.status_sprite=None
        self.batch=Batch()
        self.play_time=0
        self.reset_timer=0
        self.time_change_cnt=0
        self.time_end_cnt=0
        self.hole_timer_change=0
        self.hole_timer_end=0
        # state machine vars
        self.player_active=0
        self.state=GS_RANDOM_CARD
        self.allow_input=False
        self.player_input=None
        self.hole_nr=0

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
        # state 
        self.text_state=arcade.Text("",
                                        100,
                                        GAME_STATUS_SPRITE_HEIGHT-TEXT_SIZE,
                                        font_size=TEXT_FONT_SIZE,
                                        color=arcade.color.BLACK,
                                        batch=self.batch)

        # cards
        self.game_card=GameCard()
        self.game_card.setup()
        self.sprite_list.append(self.game_card)


    def timer_change(self, dt, end_time):
        self.time_change_cnt+=dt
        if self.time_change_cnt>=end_time:
            self.time_change_cnt=0
            return True
        return False

    def timer_end(self, dt, end_time, reset=False):
        self.time_end_cnt+=dt
        if self.time_end_cnt>=end_time:
            if reset:
                self.time_end_cnt=0
            return True
        return False


    def update(self, delta_time):
        self.play_time+=delta_time
        self.reset_timer+=delta_time
        self.text_play_time.text=f"Zeit: {self.play_time:.1f}s"
        self.text_player_active.text=f"Spieler: {self.player_active+1}"
        self.text_state.x=self.text_player_active.content_width+50
        self.text_state.text=f"Status: {GS2TEXT[self.state]}"
        if self.state==GS_RANDOM_CARD:
            self.game_card.update(delta_time)
            if self.game_card.ready:
                # wait for user input 1,2,3,4
                self.game_card.ready=False
                self.reset_timer=0
                if self.game_card.card_nr==CARD_CNT-1:
                    self.state=GS_RANDOM_HOLE
                else:
                    self.state=GS_WAIT_FOR_INPUT

        elif self.state==GS_RANDOM_HOLE:
            time_end=self.timer_end(delta_time, CARD_TIME_END)
            if self.timer_change(delta_time, CARD_TIME_CHANGE):
                cell_nr=random.choice(CELL_DANGEROUS+(0,))
                print(f"--- cell_nr: {cell_nr}")
                print(f"--- hole_nr: {self.hole_nr}")
                self.reset_timer=0
                if self.hole_nr:
                    self.game_view.cell_list[self.hole_nr].color=arcade.color.RED
                if cell_nr:
                    self.game_view.cell_list[cell_nr].color=arcade.color.EERIE_BLACK
                self.hole_nr=cell_nr
                if time_end:
                    self.time_end_cnt=0
                    self.state=GS_CHECK_HARE

        elif self.state==GS_WAIT_FOR_INPUT:
            self.allow_input=True
            if self.player_input in ["1", "2", "3", "4"]:
                self.reset_timer=0
                self.allow_input=False

        elif self.state==GS_CHECK_HARE:
            if self.timer_change(delta_time, 3):
                self.reset_timer=0
                self.state=GS_CHECK_PLAYER

        elif self.state==GS_CHECK_PLAYER:
            if self.timer_change(delta_time, 3):
                self.reset_timer=0
                self.player_active+=1
                if self.player_active==PLAYER_CNT:
                    self.player_active=0
                self.state=GS_RANDOM_CARD

        if self.reset_timer>=GAME_RESET_TIME:
            self.state=GS_RANDOM_CARD

    def draw(self):
        self.sprite_list.draw()
        self.batch.draw()

