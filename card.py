# game cards

import random
import arcade
from pyglet.graphics import Batch
from defs import *

class Card(arcade.Sprite):
    """
    1 -> 23
    2 -> 5
    3 -> 3
    K -> 10
    """

    def __init__(self):
        self.timer_change=0
        self.timer_end=0
        self.card_nr=0
        self.ready=False
        self.deck=[]
        self.deck_len=0
        self.new_deck()
        position=(CELLS_FIELD_WIDTH-5-CARD_SIZE[0]/2,
                              GAME_STATUS_SPRITE_HEIGHT/2)

        super().__init__(visible=False, center_x=position[0], center_y=position[1])

    def setup(self):
        self.textures=[arcade.load_texture(f"resources/card_{i+1}.png") for i in range(CARD_TYPE_CNT)]

    def update(self, delta_time):
        self.timer_change+=delta_time
        self.timer_end+=delta_time
        if self.timer_change>=CARD_TIME_CHANGE:
            card_nr=random.randrange(CARD_TYPE_CNT)
            self.set_texture(card_nr)
            self.timer_change=0
            self.visible=True
            if self.timer_end>=CARD_TIME_END:
                self.timer_end=0
                deck_nr=random.randrange(self.deck_len)
                self.card_nr=self.deck[deck_nr]
                self.set_texture(self.card_nr)
                del self.deck[deck_nr]
                self.deck_len-=1
                if not self.deck_len:
                    self.new_deck()
                self.ready=True
                print(f"card nr: {self.card_nr}, deck_nr: {deck_nr}, deck_len: {self.deck_len}")

    def _update(self):
        pass

    def new_deck(self):
        self.deck.clear()
        scc=[0 for c in range(CARD_TYPE_CNT)]
        for cc in range(sum(CARD_CNT)):
            for t in range(1000):
                tnr=random.randrange(CARD_TYPE_CNT)
                scc[tnr]+=1
                if scc[tnr] > CARD_CNT[tnr]:
                    scc[tnr]-=1
                    continue
                self.deck.append(tnr)
                break
            else:
                raise RuntimeError("sth wrong with mr. random")
        self.deck_len=sum(CARD_CNT)
        #print(f"scc: {scc}")
        #print(f"new deck of cards: {self.deck} {len(self.deck)}")



