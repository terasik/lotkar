# menu view class

import logging
import arcade
from arcade.gui import (
    UIManager,
    UITextureButton,
    UIInputText,
    UIAnchorLayout,
    UIView,
    UIBoxLayout,
    UILabel
)

class PlayersConfig:
    """
    players config class
    """
    pass

# some UI widgets
btn_up_pic=arcade.load_texture("resources/arrow_basic_n_small.png")
btn_down_pic=arcade.load_texture("resources/arrow_basic_s_small.png")

class MenuView(arcade.View):

    def __init__(self):
        super().__init__()
        self.background_color=arcade.color.GRAY
        self.player_cnt_selection=arcade.SpriteList()
        # Create a UIManager
        self.ui = UIManager()
        # main box
        main_box=UIBoxLayout(vertical=True, align="center", space_between=20)
        # title
        lbl_title=UILabel(text="Menü Ansicht", width=600, align="center", font_size=32, text_color=arcade.color.BLACK, bold=True)
        # append title label to main box
        main_box.add(lbl_title)
        # buttons
        btn_up=UITextureButton(texture=btn_up_pic)
        btn_down=UITextureButton(texture=btn_down_pic)
        # buttons box
        up_down_box=UIBoxLayout(space_between=10)
        up_down_box.add(btn_up)
        up_down_box.add(btn_down)
        # players count
        lbl_player_cnt_gen=UILabel(text="Anzahl Spieler", width=200, align="left", text_color=arcade.color.BLACK, font_size=22)
        lbl_player_cnt_show=UILabel(text="1", text_color=arcade.color.AMAZON, font_size=22, width=200, bold=True)
        player_cnt_box=UIBoxLayout(vertical=False, align="left", space_between=20)

        # Create an anchor layout, which can be used to position widgets on screen
        anchor = self.ui.add(UIAnchorLayout())
        # players count line
        player_cnt_box.add(lbl_player_cnt_gen)
        player_cnt_box.add(up_down_box)
        player_cnt_box.add(lbl_player_cnt_show)
        # add players cnt line to main box
        main_box.add(player_cnt_box)
        # add players count line to anchor
        anchor.add(main_box, anchor_x="center")

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
    main()
