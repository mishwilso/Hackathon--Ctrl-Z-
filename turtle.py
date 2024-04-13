import arcade
import arcade as ac

# Constants
MOVEMENT_SPEED = 55
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
    def __init__(self, texture, spirtescale, x, y):
        super().__init__(texture, spirtescale, center_x=x, center_y=y)
        self.target_y = self.center_y
        self.target_x = self.center_x
        self.speed = 0

    def move(self, command_list):
        # Determine the direction the player is moving
        # Then move by the move speed
        self.speed = 0

        for command in command_list:
            self.move(command)

        # Check if out of bounds
        self.check_out_of_bounds()

    def move_sqaure(self, command):
        if command[0] == "move_left":
            self.center_x -= MOVEMENT_SPEED * command[1]
        elif command[0] == "move_right":
            self.center_x += MOVEMENT_SPEED * command[1]
        elif command[0] == "move_up":

            if isinstance(command[1], str):
                self.target_y += MOVEMENT_SPEED * self.speed
            else:
                self.target_y += MOVEMENT_SPEED * command[1]
        elif command[0] == "move_down":
            self.center_y -= MOVEMENT_SPEED * command[1]
        elif command[0] == "speed":
            speed = int(command[1])

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

    def update(self):
        # Move the dot towards the target position
        dx = self.target_x - self.center_x
        dy = self.target_y - self.center_y
        distance = ((dx ** 2) + (dy ** 2)) ** 0.5
        if distance > MOVEMENT_SPEED:
            scale = MOVEMENT_SPEED / distance
            dx *= scale
            dy *= scale

        self.center_x += dx
        self.center_y += dy




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

        # Make the flag sprite
        self.flag_sprite = None

        # Initialize variables
        self.player_list = arcade.SpriteList()

        # Set the sprites for player and flag
        self.player_sprite = Turtle(":resources:images/enemies/wormGreen.png", SPRITE_SCALE, PLAYER_START_X, PLAYER_START_Y)
        self.player_list.append(self.player_sprite)

        self.flag_sprite = Turtle(":resources:images/items/flagGreen2.png", SPRITE_SCALE, FLAG_START_X, FLAG_START_Y)

        # Position the sprites
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
        arcade.schedule(self.player_list.update(), 1/80)

        self.update_animation()
        self.update_flag_animation()
        self.on_draw()

    def on_draw(self):
        # Draw the sprite
        self.player_sprite.draw()

        self.flag_sprite.draw()
