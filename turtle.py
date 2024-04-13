import arcade
import arcade as ac

# Constants
MOVEMENT_SPEED = 80
SPRITE_SCALE = 0.75

PLAYER_START_X = 200
PLAYER_START_Y = 100

FLAG_START_X = 225
FLAG_START_Y = 500


class Turtle(ac.Sprite):
    """
    Move all directions by 80 pixels (move speed)
    and make sure the character doesn't leave the screen
    """
    def move_left(self):
        # Move the player by the move speed
        self.center_x -= MOVEMENT_SPEED

        # Check if out of bounds
        self.check_out_of_bounds()

    def move_right(self):
        # Move the player by the move speed
        self.center_x += MOVEMENT_SPEED

        # Check if out of bounds
        self.check_out_of_bounds()

    def move_up(self):
        # Move the player by the move speed
        self.center_y += MOVEMENT_SPEED

        # Check if out of bounds
        self.check_out_of_bounds()

    def move_down(self):
        # Move the player by the move speed
        self.center_y -= MOVEMENT_SPEED

        # Check if out of bounds
        self.check_out_of_bounds()

    # Check if the player is out of bounds
    def check_out_of_bounds(self):
        if self.left < 0:
            self.left = 0
        elif self.right > arcade.get_window().width - 401:
            self.right = arcade.get_window().width - 401

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > arcade.get_window().height - 1:
            self.top = arcade.get_window().height - 1


class TurtleScreen(arcade.Section):
    """
    Show the Turtle
    """

    def __init__(self, left, right, bottom, top):
        # Parent class initializer
        super().__init__(left, right, bottom, top)
        self.left = left
        self.right = right
        self.bottom = bottom
        self.top = top

        # self.index = 0

        # Make the player sprite and lists
        self.player_list = None
        self.player_sprite = None

        # Make the flag sprite
        self.flag_sprite = None

        # Initialize variables
        self.player_list = arcade.SpriteList()

        # Assign the sprites
        self.player_sprite = Turtle(":resources:images/enemies/wormGreen.png", SPRITE_SCALE)
        self.player_list.append(self.player_sprite)

        self.flag_sprite = Turtle(":resources:images/items/flagGreen2.png", SPRITE_SCALE)

        # TODO: Try and animate? :)
        # self.player_sprite = Turtle(":resources:images/enemies/wormGreen_move.png", SPRITE_SCALE)
        # self.player_list.append(self.player_sprite)

        # Position the sprites
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y

        self.flag_sprite.center_x = FLAG_START_X
        self.flag_sprite.center_y = FLAG_START_Y

    # Doesn't work currently and isn't needed if we run out of time
    def update_animation(self, index, delta_time: float = 1 / 60):
        # Idle animation
        self.index += 1

        # If it's at the first frame, switch to the second
        if self.player_sprite == self.player_list[0] and index == 120:
            self.player_sprite = self.player_list[1]
            self.index -= 120
            return

        # If it's at the second frame, switch to the first
        if self.player_sprite == self.player_list[1] and index == 120:
            self.player_sprite = self.player_list[0]
            self.index -= 120
            return

    def on_update(self, delta_time: float):
        # Movement and game logic
        self.player_list.update()
        # self.update_animation(self.index)
        self.on_draw()

    def on_draw(self):
        # Draw the sprite
        self.player_sprite.draw()
        self.flag_sprite.draw()
