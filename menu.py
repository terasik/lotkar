# menu view class

import logging
import arcade
from arcade.gui import (
    UIManager,
    UITextureButton,
    UIInputText,
    UIAnchorLayout,
    UIView,
)

class MenuPlayerCnt:
    """
    class to player count select in menu view
    """
    pass


class MenuView(arcade.View):

    def __init__(self):
        super().__init__()
        self.background=arcade.color.AZURE
        self.player_cnt_selection=arcade.SpriteList()
        # Create a UIManager
        self.ui = UIManager()

        # Create an anchor layout, which can be used to position widgets on screen
        anchor = self.ui.add(UIAnchorLayout())
        name_box=anchor.add(UIInputText(text_color=(0,0,0)), anchor_x="left", anchor_y="top", align_y=-100)
        name_box_2=anchor.add(UIInputText(text_color=(255,0,0)), anchor_x="left", anchor_y="top", align_y=-200)
        print("anchor: ", anchor.children)
        #anchor.do_layout()
        @name_box.event("on_change")
        def on_change(event):
            print("changed text in inputbox: ", event)
        @name_box_2.event("on_change")
        def on_change(event):
            print("changed text in inputbox 2: ", event)

    def on_show_view(self) -> None:
        self.ui.enable()

    def on_hide_view(self) -> None:
        self.ui.disable()

    def on_draw(self):
        # Clear the screen
        self.clear(color=arcade.color.AZURE)

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
