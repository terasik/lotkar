"""
main game view
"""
import logging
import arcade
from arcade.gui import (
    UIManager,
    UIAnchorLayout,
    UIBoxLayout,
    UILabel,
    UIFlatButton
)

from defs import *
from menu import MenuView

LBL_TEXT="""Meine Damen und Herren,
Ende von Lotti Karroti Spiel ist erreicht
Drücke 'Menü' Button oder Taste 'M' um wieder zum Menü zu kommen
Drücke 'Ende' oder Taste 'Esc' um das Spiel zu beenden"""

#test_sound=arcade.Sound("resources/blt.mp3")

class EndView(arcade.View):
    """
    Main gaming class.

    """

    def __init__(self):
        super().__init__()
        self.bkg_pic = arcade.load_texture(BKG_PIC_WON)
        self.ui = UIManager()
        self.anchor = self.ui.add(UIAnchorLayout())
        self.main_box=UIBoxLayout(vertical=True, align="center", space_between=25)
        lbl_title=UILabel(text=LBL_TEXT,
                          align="center",
                          font_size=22,
                          text_color=arcade.color.BLACK,
                          multiline=True,
                          bold=True)
        self.main_box.add(lbl_title)
        self.setup_menu_button()
        self.setup_exit_button()
        self.anchor.add(self.main_box)
        
    def setup(self):
        #test_sound.play(loop=True)
        pass

    def setup_menu_button(self):
        style=UIFlatButton.STYLE_BLUE
        style["normal"]["font_color"]=(0,0,0,255)
        style["hover"]["font_color"]=(0,0,0,255)
        menu_btn=UIFlatButton(style=style, text="MENÜ")
        @menu_btn.event("on_click")
        def goto_menu(event):
            logging.info("go to menu view")
            menu_view=MenuView()
            self.window.show_view(menu_view)
        self.main_box.add(menu_btn)

    def setup_exit_button(self):
        style=UIFlatButton.STYLE_RED
        style["normal"]["font_color"]=(0,0,0,255)
        style["hover"]["font_color"]=(0,0,0,255)
        exit_btn=UIFlatButton(style=style, text="ENDE")
        @exit_btn.event("on_click")
        def exit_game(event):
            logging.info("exit game from end view..")
            self.window.close()
        self.main_box.add(exit_btn)

    def on_show_view(self) -> None:
        self.ui.enable()

    def on_hide_view(self) -> None:
        self.ui.disable()

    def on_draw(self):
        """
        Render the screen.
        """
        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        arcade.draw_texture_rect(
            self.bkg_pic,
            arcade.LBWH(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT),
            alpha=170
        )

        self.ui.draw()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass


    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        if key == arcade.key.ESCAPE:
            logging.info("exit game from end view..")
            self.window.close()



def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    logging.info("endansicht wird vorbereitet")
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, "Lotti Karroti Ende")

    # Create and setup the EndView
    end_view = EndView()
    end_view.setup()

    # Show EndView on screen
    window.show_view(end_view)

    # Start the arcade game loop
    logging.info("gehe in die endansicht schleife rein")
    arcade.run()



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, 
                        format="%(asctime)s %(levelname)s [%(module)s %(funcName)s] %(message)s")
    main()
