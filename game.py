# game class

#from enum import Enum
import logging
import random
import arcade
from pyglet.graphics import Batch
from defs import *
from player import Player
from cell import Cell
from card import Card

# game states
GS_RANDOM_CARD=0
GS_WAIT_FOR_INPUT=1
GS_MOVE_HARE=2
GS_CHECK_HARE=3
GS_CHECK_PLAYER=4
GS_RANDOM_HOLE=5
GS_SELECT_CELL=6
GS_END_OF_GAME=7
GS_CALC_NEXT_CELL=8

GS2TEXT=["Karte ziehen", "Warte auf Eingabe", "Bewege Hase", "Prüfe Hase", "Prüfe Spieler", "Schwarzes Loch", "Warte auf ZellNr. Eingabe", "Das ist das das Ende", "Berechne Ziel"]


class Game:
    """ main game class """
    def __init__(self, game_view):
        logging.info("init game instanz")
        self.game_view=game_view
        self.player_cnt=game_view.player_cnt
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
        self.hole_nr=-1
        self.hare_nr=0
        self.players_available=list(range(self.player_cnt))

    def setup(self):
        logging.info("setup Game Klasse")
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

        # free text 
        self.text_free=arcade.Text("",
                                        100,
                                        GAME_STATUS_SPRITE_HEIGHT-2*TEXT_SIZE,
                                        font_size=TEXT_FONT_SIZE,
                                        color=arcade.color.BLACK,
                                        batch=self.batch)

        # cards
        self.game_card=Card()
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

    def highlight_active_player(self):
        for p in range(self.player_cnt):
            if p==self.player_active:
                #player_color=C2AC[PLAYER_PROPS[p]["color"]]
                Player.status_sprite_list[self.player_cnt-p-1].color=arcade.color.GREEN
                #Player.status_sprite_list[self.player_cnt-p-1].color=player_color
                #Player.status_sprite_list[self.player_cnt-p-1].alpha=154
            else:
                Player.status_sprite_list[self.player_cnt-p-1].color=arcade.color.WHITE
                #Player.status_sprite_list[self.player_cnt-p-1].alpha=255


    def get_available_hares(self, player):
        ahl=[c for c,h in enumerate(player.hare_sprite_list) if h.available]
        return ahl


    def update(self, delta_time):
        self.play_time+=delta_time
        #self.reset_timer+=delta_time
        self.text_play_time.text=f"Zeit: {int(self.play_time)//60:>4}m {int(self.play_time)%60:>2}s"
        self.text_player_active.text=f"Spieler aktiv: {self.player_active+1}"
        self.text_state.x=self.text_player_active.content_width+50
        self.text_state.text=f"Status: {GS2TEXT[self.state]}"
        self.text_free.x=self.text_play_time.content_width+50
        self.text_free.text=f"Eingabe: {self.player_input}, Lochnr: {self.hole_nr}, Spieler aktiv: {self.players_available}"
        player=self.game_view.player_list[self.player_active]
        self.highlight_active_player()

        if self.state==GS_RANDOM_CARD:
            self.game_card.update(delta_time)
            if self.game_card.ready:
                # wait for user input 1,2,3,4
                self.game_card.ready=False
                #self.reset_timer=0
                logging.info("spielkarte ist: %s", self.game_card.card_nr)
                if self.game_card.card_nr==CARD_TYPE_CNT-1:
                    self.state=GS_RANDOM_HOLE
                else:
                    self.state=GS_WAIT_FOR_INPUT
                    self.allow_input=True

        elif self.state==GS_RANDOM_HOLE:
            time_end=self.timer_end(delta_time, CARD_TIME_END)
            if self.timer_change(delta_time, CARD_TIME_CHANGE):
                cell_nr=random.choice(CELL_DANGEROUS+(-1,))
                #self.reset_timer=0
                if self.hole_nr>0:
                    self.game_view.cell_list[self.hole_nr].color=arcade.color.RED
                if cell_nr>0:
                    self.game_view.cell_list[cell_nr].color=arcade.color.EERIE_BLACK
                self.hole_nr=cell_nr
                if time_end:
                    self.time_end_cnt=0
                    self.state=GS_CHECK_HARE
                    logging.info("schwarzes loch in der zelle nr %s", cell_nr)


        elif self.state==GS_WAIT_FOR_INPUT:
            ahl=self.get_available_hares(player)
            if not ahl:
                logging.warning("keine hasen beim spieler %s verfügbar", player.nr)
                self.state=GS_CHECK_PLAYER
            else:
                if self.player_input: 
                    if (self.player_input-1) in ahl:
                        logging.info("hase nr %s wird jetzt laufen", self.player_input)
                        self.hare_nr=self.player_input-1
                        #self.reset_timer=0
                        self.allow_input=False
                        #self.state=GS_SELECT_CELL
                        self.state=GS_CALC_NEXT_CELL
                    else:
                        logging.warning("hase nr %s ist nicht mehr im spiel", self.player_input)
                    self.player_input=None
            #self.reset_timer=0


        elif self.state==GS_SELECT_CELL:
            try:
                dest_cell=int(input("provide cell nr: "))
                if dest_cell-1 in list(range(CELL_CNT)):
                    new_position=Cell.calc_cell_positions()[dest_cell-1]
                    #print(f"new position: {new_position}")
                    player.hare_sprite_list[self.hare_nr].new_position=new_position
                    player.hare_sprite_list[self.hare_nr].rescale_to_cell()
                    old_cell_nr=player.hare_sprite_list[self.hare_nr].cell_nr
                    if old_cell_nr>=0:
                        self.game_view.cell_list[old_cell_nr].busy=False
                    player.hare_sprite_list[self.hare_nr].cell_nr=dest_cell-1
                    self.game_view.cell_list[dest_cell-1].busy=True
                    self.state=GS_MOVE_HARE
                else:
                    print("false input. try again")
            except:
                print("except: false input. try again")
            self.reset_timer=0


        elif self.state==GS_CALC_NEXT_CELL:
            if self.timer_change(delta_time, 2):
                logging.info("status GS_CALC_NEXT_CELL wird verarbeitet")
                #self.reset_timer=0
                cell_nr_now=player.hare_sprite_list[self.hare_nr].cell_nr
                cell_nr_next=cell_nr_now+self.game_card.card_nr+1
                if cell_nr_next >= CELL_CNT-1:
                    dest_cell=CELL_CNT-1
                    logging.info(f"berechnung zeigt, dass hase gewinnen wird")
                else:
                    cell_cnt=0
                    for cell_nr in range(cell_nr_now+1, CELL_CNT-1):
                        if not self.game_view.cell_list[cell_nr].busy:
                            if cell_cnt==self.game_card.card_nr:
                                dest_cell=cell_nr
                                break
                            else:
                                cell_cnt+=1
                    else:
                        dest_cell=CELL_CNT-1
                        logging.info(f"berechnung in der schleife und hase wird gewinnen")
                        
                #print(f"calculated dest cell: {dest_cell}")
                logging.info("brechnete zelle %s", dest_cell)

                new_position=Cell.calc_cell_positions()[dest_cell]
                player.hare_sprite_list[self.hare_nr].new_position=new_position
                player.hare_sprite_list[self.hare_nr].rescale_to_cell()
                old_cell_nr=player.hare_sprite_list[self.hare_nr].cell_nr
                if old_cell_nr>=0:
                    logging.info("zelle nr %s wird frei", old_cell_nr)
                    self.game_view.cell_list[old_cell_nr].busy=False
                player.hare_sprite_list[self.hare_nr].cell_nr=dest_cell
                self.game_view.cell_list[dest_cell].busy=True
                logging.info("zelle nr %s wird besetzt", dest_cell)
                self.state=GS_MOVE_HARE


        elif self.state==GS_MOVE_HARE:

            if player.hare_sprite_list[self.hare_nr].move_ready:
                logging.info("hase %s des spielers %s ist an der zelle angekommen", player.nr, self.hare_nr)
                self.state=GS_CHECK_HARE
            else:
                self.reset_timer=0



        elif self.state==GS_CHECK_HARE:
            """ 
            iterate over all players
            """
            if self.timer_change(delta_time, 2):
                logging.info("status GS_CHECK_HARE wird verarbeitet")
                #self.reset_timer=0
                for p in self.game_view.player_list:
                    for h in p.hare_sprite_list:
                        # hare in the hole
                        if h.available and h.cell_nr>=0 and h.cell_nr==self.hole_nr:
                            #print(f"hare nr. {h.nr} of player nr. {p.nr+1} is in the hole")
                            logging.info("hase %s des spielers %s ist ins loch gefallen", h.nr, p.nr+1)
                            self.game_view.cell_list[h.cell_nr].busy=False
                            h.available=False
                            h.visible=False
                            p.hares_alive-=1
                            p.hares_dead+=1
                        # hare at the end
                        if h.available and h.cell_nr>=CELL_CNT-1:
                            print(f"hare nr. {h.nr} of player nr. {p.nr+1} won")
                            #logging.info("hase %s des spielers %s hat gewonnen", h.nr, p.nr+1)
                            self.game_view.cell_list[h.cell_nr].busy=False
                            h.available=False
                            h.visible=False
                            p.hares_alive-=1
                            p.hares_win+=1
                            #self.game_view.bkg=self.game_view.bkg_pic_won
                self.state=GS_CHECK_PLAYER

        elif self.state==GS_CHECK_PLAYER:
            if self.timer_change(delta_time, 2):
                #self.game_view.bkg=self.game_view.bkg_pic_norm
                logging.info("status GS_CHECK_PLAYER wird verarbeitet")
                #self.reset_timer=0
                self.check_players()
                for t in range(self.player_cnt):
                    self.player_active+=1
                    if self.player_active==self.player_cnt:
                        self.player_active=0
                    if self.player_active in self.players_available:
                        self.state=GS_RANDOM_CARD
                        logging.info("nächster spieler ist %s", self.player_active)
                        break
                else:
                    logging.info("ende des spiels ist erreicht")
                    self.state=GS_END_OF_GAME

        elif self.state==GS_END_OF_GAME:
            if self.timer_change(delta_time, 1):
                #self.reset_timer=0
                logging.info("press ESC button to let me free")
                from end import EndView
                # Create and setup the EndView
                end_view = EndView()
                end_view.setup()

                # Show EndView on screen
                self.game_view.window.show_view(end_view)


        #if self.reset_timer>=GAME_RESET_TIME:
        #    logging.info("reset timer zeit ist erreicht")
        #    self.state=GS_RANDOM_CARD

    def check_players(self):
        apl=[]
        for p in self.game_view.player_list:
            if p.hares_alive:
                apl.append(p.nr)
        self.players_available=apl
        logging.info("spieler noch verfügbar %s", apl)

    def draw(self):
        self.sprite_list.draw()
        self.batch.draw()

