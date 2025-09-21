# menu view class

import logging
import arcade
from arcade.gui import (
    UIManager,
    UITextureButton,
    UIInputText,
    UIAnchorLayout,
    UIView,
    UIImage,
    UIBoxLayout,
    UILabel,
    UIFlatButton
)
from plconfig import PlayerConfig
from helpers import create_up_down_box
from defs import PLAYER_CNT_MAX, PLAYER_CNT_MIN
from lotkar import GameView


class MenuView(arcade.View):

    def __init__(self):
        super().__init__()
        self.background_color=arcade.color.GRAY
        self.player_cnt=PLAYER_CNT_MIN
        self.player_configs=[]
        #self.player_cnt_selection=arcade.SpriteList()
        # Create a UIManager
        self.ui = UIManager()
        # main box
        self.main_box=UIBoxLayout(vertical=True, align="center", space_between=25)
        # Create an anchor layout, which can be used to position widgets on screen
        self.anchor = self.ui.add(UIAnchorLayout())
        self.name_inps=[]
        # title
        lbl_title=UILabel(text="Menü", 
                          #width=600, 
                          align="center", 
                          font_size=32, 
                          text_color=arcade.color.BLACK, 
                          bold=True)
        self.anchor.add(lbl_title, anchor_x="left", anchor_y="top", align_x=10, align_y=-10)
        # append title label to main box
        # self.main_box.add(lbl_title)
        # players count
        lbl_player_cnt_gen=UILabel(text="Anzahl Spieler", 
                                   width=200, 
                                   align="left", 
                                   text_color=arcade.color.BLACK, 
                                   font_size=22)
        self.lbl_player_cnt_show=UILabel(text="1", 
                                         text_color=arcade.color.BLACK, 
                                         font_size=22, 
                                         width=200, 
                                         bold=True)
        player_cnt_box=UIBoxLayout(vertical=False, align="left", space_between=25)

        # players count line
        player_cnt_box.add(lbl_player_cnt_gen)
        #player_cnt_box.add(create_up_down_box())
        player_cnt_box.add(self.setup_player_cnt())
        player_cnt_box.add(self.lbl_player_cnt_show)
        # add players cnt line to main box
        self.main_box.add(player_cnt_box)
            
        self.setup_player_config()

        # add players count line to anchor
        self.anchor.add(self.main_box, anchor_x="center", anchor_y="top")
        self.setup_exit_button()
        self.setup_play_button()

    def setup_player_cnt(self):
        logging.info("setup player count")
        def inc_pl_cnt(event):
            self.player_cnt+=1
            if self.player_cnt>PLAYER_CNT_MAX:
                self.player_cnt=PLAYER_CNT_MAX
            else:
                logging.info("adding player config")
                self.main_box.add(self.player_configs[self.player_cnt-1])
            self.lbl_player_cnt_show.text=self.player_cnt
            logging.info("increase player count (+) to %s", self.player_cnt)
        def dec_pl_cnt(event):
            self.player_cnt-=1
            if self.player_cnt<PLAYER_CNT_MIN:
                self.player_cnt=PLAYER_CNT_MIN
            else:
                logging.info("removing player config")
                self.main_box.remove(self.player_configs[self.player_cnt])
            self.lbl_player_cnt_show.text=self.player_cnt
            logging.info("decrease player count (-) to %s", self.player_cnt)
        return create_up_down_box(inc_pl_cnt,dec_pl_cnt)

    def setup_exit_button(self):
        exit_btn=UIFlatButton(style=UIFlatButton.STYLE_RED, text="EXIT")
        self.anchor.add(exit_btn, 
                        anchor_x="left", 
                        anchor_y="bottom", 
                        align_x=20, 
                        align_y=20)
        @exit_btn.event("on_click")
        def exit_game(event):
            logging.info("exit game from menu..")
            self.window.close()

    def setup_play_button(self):
        start_btn=UIFlatButton(style=UIFlatButton.STYLE_BLUE, text="PLAY")
        self.anchor.add(start_btn, 
                        anchor_x="right", 
                        anchor_y="bottom", 
                        align_x=-20, 
                        align_y=20)
        @start_btn.event("on_click")
        def start_game(event):
            logging.info("starting game!")
            game_view=GameView(self.player_cnt,self.player_configs)
            self.window.show_view(game_view)

    def setup_player_config(self):
        logging.info("setup player config")
        # add player line
        for player_nr in range(PLAYER_CNT_MAX):
            player_config=PlayerConfig(player_nr)
            self.player_configs.append(player_config.setup_menu())

        for player_nr in range(self.player_cnt):
            self.main_box.add(self.player_configs[player_nr])

    def check_players_config(self):
        logging.info("checking player configs")


    def on_show_view(self) -> None:
        self.ui.enable()

    def on_hide_view(self) -> None:
        self.ui.disable()

    def on_draw(self):
        # Clear the screen
        self.clear()

        # Add draw commands that should be below the UI
        # ...

        self.ui.draw()

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        if key == arcade.key.ESCAPE:
            self.window.close()



def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(title="Testing Menu View")

    # Show the view on screen
    window.show_view(MenuView())

    # Start the arcade game loop
    arcade.run()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s [%(module)s %(funcName)s] %(message)s")
    main()
