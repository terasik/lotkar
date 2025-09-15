# player config menu

import logging
import arcade
from arcade.gui import (
    UITextureButton,
    UIInputText,
    UIImage,
    UIBoxLayout,
    UILabel
)
from defs import *
from helpers import name_text_inputs, hare_textures, create_up_down_box, ModInpText


class PlayerConfig:

    def __init__(self, nr):
        self.nr=nr
        self.color_nr=0
        self.name=f"unknown_{nr+1}"

    def setup_menu(self):
        player_prop_line=UIBoxLayout(vertical=False, align="left", space_between=25)
        lbl_player_nr=UILabel(text=f"Spieler {self.nr+1}", align="left", text_color=arcade.color.BLACK, font_size=22)
        hare_up_down_box=create_up_down_box()
        hare_image=UIImage(texture=hare_textures[self.nr], width=64, height=85)
        lbl_name=UILabel(text=f"Name", align="left", text_color=arcade.color.BLACK, font_size=22)
        name_input=ModInpText(self.nr, text_color=arcade.color.BLACK)
        #name_input=name_text_inputs[self.nr]
        @name_input.event("on_change")
        def name_input_change(event):
            logging.info("change event %s", event.source.nr)
            self.name=event.new_value
        @name_input.event("on_click")
        def name_input_click(event):
            logging.info("click event: %s", event.source.nr)
            for s in name_text_inputs:
                if s.nr == event.source.nr:
                    event.source.activate()
                else:
                    s.deactivate()
        name_text_inputs.append(name_input)
        player_prop_line.add(lbl_player_nr)
        player_prop_line.add(hare_up_down_box)
        player_prop_line.add(hare_image)
        player_prop_line.add(lbl_name)
        player_prop_line.add(name_input)
        return player_prop_line

