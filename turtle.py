import arcade
import arcade as ac

# Constants
MOVEMENT_SPEED = 80
SPRITE_SCALE = 0.75

PLAYER_START_X = 200
PLAYER_START_Y = 100

FLAG_START_X = 225
FLAG_START_Y = 500

# Speed of the animation
FRAME_RATE = 30


class Turtle(ac.Sprite):
    """
    Move all directions by 80 pixels (move speed)
    and make sure the character doesn't leave the screen
    """
    def move(self, command_list):
        # Determine the direction the player is moving
        # Then move by the move speed
        for command in command_list:
            if command[0] == "move_left":
                self.center_x -= MOVEMENT_SPEED * command[1]
            elif command[0] == "move_right":
                self.center_x += MOVEMENT_SPEED * command[1]
            elif command[0] == "move_up":
                self.center_y += MOVEMENT_SPEED * command[1]
            elif command[0] == "move_down":
                self.center_y -= MOVEMENT_SPEED * command[1]

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

        # Define indexes for animation
        self.index_p = 0
        self.index_f = 0

        # Make the player sprite and lists
        self.player_list = None
        self.player_sprite = None

        # Make the flag sprite
        self.flag_sprite = None

        # Initialize variables
        self.player_list = arcade.SpriteList()

        # Set the sprites for player and flag
        self.player_sprite = Turtle(":resources:images/enemies/wormGreen.png", SPRITE_SCALE)
        self.player_list.append(self.player_sprite)

        self.flag_sprite = Turtle(":resources:images/items/flagGreen2.png", SPRITE_SCALE)

        # Position the sprites
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y

        self.flag_sprite.center_x = FLAG_START_X
        self.flag_sprite.center_y = FLAG_START_Y

    def update_animation(self, delta_time: float = 1 / 60):
        # Idle animation
        self.index_p += 1

        # If it's at the first frame, switch to the second
        if self.index_p == FRAME_RATE:
            self.player_sprite.append_texture(arcade.load_texture(":resources:images/enemies/wormGreen_move.png"))
            self.player_sprite.set_texture(1)
            return

        # If it's at the second frame, switch to the first
        if self.index_p == FRAME_RATE * 2:
            self.player_sprite.set_texture(0)
            self.index_p -= FRAME_RATE * 2
            return

    def update_flag_animation(self, delta_time: float = 1 / 60):
        # Idle animation
        self.index_f += 1

        # If it's at the first frame, switch to the second
        if self.index_f == FRAME_RATE / 2:
            self.flag_sprite.append_texture(arcade.load_texture(":resources:images/items/flagGreen1.png"))
            self.flag_sprite.set_texture(1)
            return

        # If it's at the second frame, switch to the third
        if self.index_f == FRAME_RATE:
            self.flag_sprite.set_texture(0)
            self.index_f -= FRAME_RATE
            return

    def on_update(self, delta_time: float):
        # Movement and game logic
        self.player_list.update()

        self.update_animation()
        self.update_flag_animation()
        self.on_draw()

    def on_draw(self):
        # Draw the sprite
        self.player_sprite.draw()
        self.flag_sprite.draw()
