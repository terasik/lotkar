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
from defs import PLAYER_CNT_MAX, PLAYER_CNT_MIN, BKG_PIC_MENU, WINDOW_WIDTH, WINDOW_HEIGHT
from lotkar import GameView

#arcade.resources.load_kenney_fonts()

class MenuView(arcade.View):

    def __init__(self):
        super().__init__()
        self.background_color=arcade.color.GRAY
        self.bkg_pic = arcade.load_texture(BKG_PIC_MENU)
        self.check_ok=False
        self.player_cnt=PLAYER_CNT_MIN
        self.player_prop_lines=[]
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
        self.anchor.add(self.main_box, anchor_x="center", anchor_y="top", align_y=-20)
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
                self.main_box.add(self.player_prop_lines[self.player_cnt-1])
            self.lbl_player_cnt_show.text=self.player_cnt
            logging.info("increase player count (+) to %s", self.player_cnt)
        def dec_pl_cnt(event):
            self.player_cnt-=1
            if self.player_cnt<PLAYER_CNT_MIN:
                self.player_cnt=PLAYER_CNT_MIN
            else:
                logging.info("removing player config")
                self.main_box.remove(self.player_prop_lines[self.player_cnt])
            self.lbl_player_cnt_show.text=self.player_cnt
            logging.info("decrease player count (-) to %s", self.player_cnt)
        return create_up_down_box(inc_pl_cnt,dec_pl_cnt)

    def setup_exit_button(self):
        style=UIFlatButton.STYLE_RED
        style["normal"]["font_color"]=(0,0,0,255)
        style["hover"]["font_color"]=(0,0,0,255)
        exit_btn=UIFlatButton(style=style, text="ENDE")
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
        style=UIFlatButton.STYLE_BLUE
        style["normal"]["font_color"]=(0,0,0,255)
        style["hover"]["font_color"]=(0,0,0,255)
        start_btn=UIFlatButton(style=style, text="SPIEL")
        self.anchor.add(start_btn, 
                        anchor_x="right", 
                        anchor_y="bottom", 
                        align_x=-20, 
                        align_y=20)
        @start_btn.event("on_click")
        def start_game(event):
            logging.info("show some message box")
            if self._check_hare_colors():
                msg_text="""\
Alles bereit für ein Spiel!
Drücke 'Ja' für Spielen oder
'Abbruch' um zurück zum Menü zu kommen"""
            else:
                msg_text="""\
Achtung, Achtung eine Durchsage:
Einige Spieler haben gleiche Hasenfarben!!
Drücke 'Ja' um trotzdem weiter zu spielen oder 
'Abbruch' um eine Korrektur im Menü zu machen"""
            msg_box=arcade.gui.UIMessageBox(width=300, 
                                            height=300, 
                                            message_text=msg_text, 
                                            title="Prüfe, prüfe..",
                                            buttons=["Ja", "Abbruch"])
            @msg_box.event("on_action")
            def msg_box_act(event):
                logging.info("msg box on_action %s", event)
                if event.action=="Ja":
                    # start game hier
                    self.check_ok=True
                    self._goto_game()
                else:
                    self.check_ok=False
            self.ui.add(msg_box)
            if self.check_ok:
                self._goto_game()

    def _goto_game(self):
        logging.info("starting game!")
        game_view=GameView(self.player_cnt,self.player_configs)
        game_view.setup()
        self.window.show_view(game_view)

    def _check_hare_colors(self):
        """
        check hare colors. if players have same color
        show it on message box
        """
        colors=set()
        for p in range(self.player_cnt):
            colors.add(self.player_configs[p].color_nr)
        if self.player_cnt == len(colors):
            return True
        return False



    def setup_player_config(self):
        logging.info("setup player config")
        # add player line
        for player_nr in range(PLAYER_CNT_MAX):
            player_config=PlayerConfig(player_nr)
            self.player_prop_lines.append(player_config.setup_menu())
            self.player_configs.append(player_config)

        for player_nr in range(self.player_cnt):
            self.main_box.add(self.player_prop_lines[player_nr])

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
        arcade.draw_texture_rect(
            self.bkg_pic,
            arcade.LBWH(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT),
            alpha=64
        )

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
