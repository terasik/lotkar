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

# button textures
btn_up_pic=arcade.load_texture("resources/arrow_basic_n_small.png")
btn_down_pic=arcade.load_texture("resources/arrow_basic_s_small.png")

# players_config

class ModInpText(UIInputText):
    def __init__(self, nr, **kwargs):
        self.nr=nr
        super().__init__(**kwargs)

class MenuView(arcade.View):

    def __init__(self):
        super().__init__()
        self.background_color=arcade.color.GRAY
        self.player_cnt_selection=arcade.SpriteList()
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
        player_cnt_box.add(self._create_up_down_box())
        player_cnt_box.add(lbl_player_cnt_show)
        # add players cnt line to main box
        self.main_box.add(player_cnt_box)

        # add player line
        self.main_box.add(self._create_player_line())
        self.main_box.add(self._create_player_line(1))
        #self.main_box.add(self._create_player_line(2))
        #self.main_box.add(self._create_player_line(3))

        # add players count line to anchor
        self.anchor.add(self.main_box, anchor_x="center")

    def _create_up_down_box(self):
        # buttons
        btn_up=UITextureButton(texture=btn_up_pic)
        btn_down=UITextureButton(texture=btn_down_pic)
        # buttons box
        up_down_box=UIBoxLayout(space_between=10)
        up_down_box.add(btn_up)
        up_down_box.add(btn_down)
        return up_down_box

    def _create_player_line(self, nr=0):
        player_prop_line=UIBoxLayout(vertical=False, align="left", space_between=25)
        lbl_player_nr=UILabel(text=f"Spieler {nr+1}", align="left", text_color=arcade.color.BLACK, font_size=22)
        hare_up_down_box=self._create_up_down_box()
        hare_images=UIImage(texture=hare_images[nr], width=64, height=85)
        lbl_name=UILabel(text=f"Name", align="left", text_color=arcade.color.BLACK, font_size=22)
        inp_name=ModInpText(nr, text_color=arcade.color.BLACK)
        @inp_name.event("on_change")
        def inp_name_change(event):
            logging.info("change event %s", event.source.nr)
            #logging.info("on_change event: %s", event)
        @inp_name.event("on_click")
        def inp_name_click(event):
            logging.info("click event: %s", event.source.nr)
            for s in self.name_inps:
                if s.nr == event.source.nr:
                    event.source.activate()
                else:
                    s.deactivate()
            #event.source.activate()
        self.name_inps.append(inp_name)
        player_prop_line.add(lbl_player_nr)
        player_prop_line.add(hare_up_down_box)
        player_prop_line.add(hare_images)
        player_prop_line.add(lbl_name)
        player_prop_line.add(inp_name)

        return player_prop_line




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
