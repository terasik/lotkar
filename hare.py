# hare class

import arcade

class Hare(arcade.Sprite):

    def __init__(self, color, nr, **kwargs):
        self.hare_color=color
        self.nr=nr
        texture=arcade.load_texture(f"resources/rabbit_{color}_{nr}.png")
        super().__init__(texture, scale=0.25, **kwargs)

    #def setup(self, position=(100,100)):
    #    self.sprite=arcade.Sprite(self.texture)
    #    self.sprite.position=position
