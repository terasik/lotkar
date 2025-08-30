"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import logging
import arcade
from defs import *
from cell import Cell
from player import Player
from game import Game

CELL_POSITIONS=Cell.calc_cell_positions()
#test_sound=arcade.Sound("resources/blt.mp3")

class GameView(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self):
        super().__init__()
        #self.background_color = arcade.color.AMAZON
        self.bkg_pic_norm = arcade.load_texture(BKG_PIC_NORM)
        self.bkg_pic_won = arcade.load_texture(BKG_PIC_WON)
        self.bkg=self.bkg_pic_norm
        # If you have sprite lists, you should create them here,
        # and set them to None
        self.cell_list = arcade.SpriteList()
        self.player_list=[]
        self.game=None

        
    def setup(self):
        # create game status
        self.game=Game(self)
        self.game.setup()
        # create all cells
        for i in range(CELL_CNT):
            cell=Cell(i)
            cell.center_x=CELL_POSITIONS[i][0]
            cell.center_y=CELL_POSITIONS[i][1]
            self.cell_list.append(cell)
        # create player boundaries
        Player.setup_status_sprites()
        Player.setup_boundary_shapes()

        for p in range(PLAYER_CNT):
            player=Player(p, PLAYER_PROPS[p]["color"], name=PLAYER_PROPS[p]["name"])
            player.setup()
            self.player_list.append(player)
        #test_sound.play(loop=True)


    def reset(self):
        """Reset the game to the initial state."""
        # Do changes needed to restart the game here if you want to support that
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        arcade.draw_texture_rect(
            self.bkg,
            arcade.LBWH(0, 80, WINDOW_WIDTH*3/4, WINDOW_HEIGHT),
        )
        # Call draw() on all your sprite lists below
        #self.game.sprite_list.draw()
        #self.game.batch.draw()
        self.game.draw()
        self.cell_list.draw()
        Player.status_sprite_list.draw()
        Player.boundary_shape_list.draw()

        for p in self.player_list:
            p.hare_sprite_list.draw()
            p.batch.draw()
            #p.player_nr_text.draw()
                        
        

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.game.update(delta_time)
        for p in self.player_list:
            p.update(delta_time)
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        if key == arcade.key.ESCAPE:
            self.window.close()
        if self.game.allow_input:
            logging.info("taste %s gedrückt", key)
            if key in [arcade.key.NUM_1, arcade.key.KEY_1]:
                self.game.player_input=1
            elif key in [arcade.key.NUM_2, arcade.key.KEY_2]:
                self.game.player_input=2
            elif key in [arcade.key.NUM_3, arcade.key.KEY_3]:
                self.game.player_input=3
            elif key in [arcade.key.NUM_4, arcade.key.KEY_4]:
                self.game.player_input=4


    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    logging.info("starte ein gutes, ein genaues Spiel")
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create and setup the GameView
    game = GameView()
    game.setup()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    logging.info("gehe in die arcade schleife rein")
    arcade.run()



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, 
                        format="%(asctime)s %(levelname)s [%(module)s %(funcName)s] %(message)s")
    main()
