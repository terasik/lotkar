# some helper functions and classes

import logging
import arcade
from arcade.gui import (
    UIInputText,
    UITextureButton,
    UIBoxLayout,
    UITextureButton,
)
from defs import *

click_sound=arcade.Sound("resources/click.wav")

class ModInpText(UIInputText):
    """ input text with nr to have possibility
    to deactivate it
    """
    def __init__(self, nr, **kwargs):
        self.nr=nr
        super().__init__(**kwargs)

#name_text_inputs=[ModInpText(nr, text_color=arcade.color.BLACK) for nr in range(PLAYER_CNT_MAX)]
name_text_inputs=[]
# hare textures
hare_textures=[arcade.load_texture(f"resources/rabbit_{color}.png") for color in HARE_COLORS]
# button textures
btn_up_pic=arcade.load_texture("resources/arrow_basic_n_small.png")
btn_down_pic=arcade.load_texture("resources/arrow_basic_s_small.png")

def btn_up_handler_def(event):
    logging.info("btn up pressed on source %s", event.source)

def btn_down_handler_def(event):
    logging.info("btn down pressed on source %s", event.source)

def create_up_down_box(up_func=btn_up_handler_def, down_func=btn_down_handler_def):
    # buttons
    btn_up=UITextureButton(texture=btn_up_pic)
    @btn_up.event("on_click")
    def wr_up(event):
        # play click sound hier
        click_sound.play()
        up_func(event)
    btn_down=UITextureButton(texture=btn_down_pic)
    @btn_down.event("on_click")
    def wr_down(event):
        # play click sound hier
        click_sound.play()
        down_func(event)
    # buttons box
    up_down_box=UIBoxLayout(space_between=10)
    up_down_box.add(btn_up)
    up_down_box.add(btn_down)
    return up_down_box

