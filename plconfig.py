# player config menu

import arcade
from arcade.gui import (
    UITextureButton,
    UIInputText,
    UIImage,
    UIBoxLayout,
    UILabel
)
from defs import *

# hare textures
hare_images=[arcade.load_texture(f"resources/rabbit_{color}.png") for color in HARE_COLORS]

class PlayerConfig:

    def __init__(self, nr):
        self.nr=nr
        self.color_nr=0
        self.name=f"unknown_{nr+1}"

    
