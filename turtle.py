import arcade
import arcade as ac

# Constants
MOVEMENT_SPEED = 80
SPRITE_SCALE = 0.75


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

        # Make the player sprite and lists
        self.player_list = None
        self.player_sprite = None

        # Initialize variables
        self.player_list = arcade.SpriteList()
        self.player_sprite = Turtle(":resources:images/enemies/wormGreen.png", SPRITE_SCALE)

        self.player_list.append(self.player_sprite)

        # TODO: Try and animate :)
        self.player_sprite = Turtle(":resources:images/enemies/wormGreen_move.png", SPRITE_SCALE)

        self.player_list.append(self.player_sprite)

        # Position the sprite
        self.player_sprite.center_x = 200
        self.player_sprite.center_y = 100

    def update_animation(self, delta_time: float = 1 / 60):
        # Idle animation
        # If it's at the first frame, switch to the second
        if self.player_sprite == self.player_list[0]:
            self.player_sprite = self.player_list[1]
            return

        # If it's at the second frame, switch to the first
        if self.player_sprite == self.player_list[1]:
            self.player_sprite = self.player_list[0]
            return

    def on_update(self, delta_time: float):
        # Movement and game logic
        self.player_list.update()

    def on_draw(self):
        # Draw the sprite
        self.player_list.draw()
