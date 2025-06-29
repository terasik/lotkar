"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade

# window constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Lotti Karrotti"

# cell constants
CELL_POSITIONS=[(50, 50), (100, 50), (150, 50), (200, 50),
                (200, 100),
                (50, 150), (100, 150), (150,150), (200, 150)]
CELL_CNT=len(CELL_POSITIONS)
CELL_SCALE=0.1
CELL_DANGEROUS=(2, 4, 5)
CELL_RADIUS=40


cell_green_texture = arcade.load_texture("cell_green.png")
cell_red_texture = arcade.load_texture("cell_red.png")
cell_hole_texture = arcade.load_texture("cell_hole.png")

CELL_TYPE_TO_PATH={"green": "green.png", "red": "red.png", "hole": "red_with_hole.png"}

class Cell(arcade.Sprite):
  
  def __init__(self, nr, **kwargs):
    self.nr=nr
    self.hare=None
    # maybe replace with type?
    #center_x=CELL_POSITIONS[nr][0]
    #center_y=CELL_POSITIONS[nr][1]
    #scale=CELL_SCALE
    # which hare is on this cell
    if self.nr in CELL_DANGEROUS:
      texture=cell_red_texture
      self.cell_type="red"
    else:
      texture=cell_green_texture
      self.cell_type="green"
    super().__init__(texture, CELL_SCALE, CELL_POSITIONS[nr][0], CELL_POSITIONS[nr][1], **kwargs)
    
#  def change_type(self, cell_type):
#    self.path_or_texture=CELL_TYPE_TO_PATH[cell_type]

def calc_cell_positions():
  """
  1 2 3 4 5 6
            7
          9 8
  """
  cell_diam=CELL_RADIUS*2+10
  width=int(WINDOW_WIDTH*0.75)
  max_hor_cnt=int(width/cell_diam)
  max_ver_cnt=int(WINDOW_HEIGHT/cell_diam)
  print(f"max_hor_cnt={max_hor_cnt} max_ver_cnt={max_ver_cnt}")
  ver_half=int(max_ver_cnt/2)
  max_cell_cnt=(max_hor_cnt+1)*ver_half + max_hor_cnt*(max_ver_cnt%2)
  print(f"""\
max_hor_cnt={max_hor_cnt} 
max_ver_cnt={max_ver_cnt}
max_cell_cnt={max_cell_cnt}
""")
  
  
  
  

class CellSprite(arcade.SpriteCircle):
  def __init__(self, nr, **kwargs):
    self.nr=nr
    self.hare=None

    #self.center_x=CELL_POSITIONS[nr][0]
    #self.center_y=CELL_POSITIONS[nr][1]
    #self.position=(CELL_POSITIONS[nr][0], CELL_POSITIONS[nr][1])
    # which hare is on this cell
    if self.nr in CELL_DANGEROUS:
      #texture=cell_red_texture
      self.cell_type="red"
      color=(255,0,0)
    else:
      #texture=cell_green_texture
      self.cell_type="green"
      color=(0,255,255)
    
    super().__init__( CELL_RADIUS, color, False,**kwargs)


class GameView(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self):
        super().__init__()

        self.background_color = arcade.color.SCHOOL_BUS_YELLOW

        # If you have sprite lists, you should create them here,
        # and set them to None
        self.cell_list = arcade.SpriteList()
        
    def setup(self):

        for i in range(CELL_CNT):
          cell=CellSprite(i)
          #cell.position= (CELL_POSITIONS[i][0], CELL_POSITIONS[i][1])
          cell.center_x=CELL_POSITIONS[i][0]
          cell.center_y=CELL_POSITIONS[i][1]
          self.cell_list.append(cell)
        print(self.__dir__())

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

        # Call draw() on all your sprite lists below

        self.cell_list.draw()
        arcade.draw_line(int(WINDOW_WIDTH*0.75), 
                          0, 
                          int(WINDOW_WIDTH*0.75), 
                          WINDOW_HEIGHT, 
                          arcade.color.BABY_BLUE,
                          5)
                        
        

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
        pass

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
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create and setup the GameView
    game = GameView()
    game.setup()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()



if __name__ == "__main__":
    main()