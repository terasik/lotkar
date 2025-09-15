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
    UILabel
)
from plconfig import PlayerConfig
from helpers import create_up_down_box



class MenuView(arcade.View):

    def __init__(self):
        super().__init__()
        self.background_color=arcade.color.GRAY
        #self.player_cnt_selection=arcade.SpriteList()
        # Create a UIManager
        self.ui = UIManager()
        # main box
        self.main_box=UIBoxLayout(vertical=True, align="center", space_between=25)
        # Create an anchor layout, which can be used to position widgets on screen
        self.anchor = self.ui.add(UIAnchorLayout())
        self.name_inps=[]
        # title
        lbl_title=UILabel(text="Menü", width=600, align="center", font_size=32, text_color=arcade.color.BLACK, bold=True)
        # append title label to main box
        self.main_box.add(lbl_title)
        # players count
        lbl_player_cnt_gen=UILabel(text="Anzahl Spieler", width=200, align="left", text_color=arcade.color.BLACK, font_size=22)
        lbl_player_cnt_show=UILabel(text="1", text_color=arcade.color.AMAZON, font_size=22, width=200, bold=True)
        player_cnt_box=UIBoxLayout(vertical=False, align="left", space_between=25)

        # players count line
        player_cnt_box.add(lbl_player_cnt_gen)
        player_cnt_box.add(create_up_down_box())
        player_cnt_box.add(lbl_player_cnt_show)
        # add players cnt line to main box
        self.main_box.add(player_cnt_box)

        # add player line
        for player_nr in range(2):
            player_config=PlayerConfig(player_nr)
            self.main_box.add(player_config.setup_menu())

        # add players count line to anchor
        self.anchor.add(self.main_box, anchor_x="center")


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
