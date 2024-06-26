from typing import Optional

import console as c

import turtle as t

import arcade


class Box(arcade.SpriteSolidColor):
    """ This is a Solid Sprite that represents a GREEN Box on the screen """

    def __init__(self, section):
        super().__init__(100, 100, arcade.color.APPLE_GREEN)
        self.section = section

    def on_update(self, delta_time: float = 1 / 60):
        # update the box (this actually moves the Box by changing its position)
        self.update()

        # if we hit the ground then lay on the ground and stop movement
        if self.bottom <= 0:
            self.bottom = 0
            self.stop()

    def release(self):
        self.section.hold_box = None
        self.change_y = -10


class ScreenPart(arcade.Section):
    """
    This represents a part of the View defined by its
    boundaries (left, bottom, etc.)
    """

    def __init__(self, left: int, bottom: int, width: int, height: int,
                 **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)

        self.selected: bool = False  # if this section is selected

        self.box: Box = Box(self)  # the section Box Sprite

        # position the Box inside this section using self.left + self.width
        self.box.position = self.left + (self.width / 2), 50

        # variable that will hold the Box when it's being dragged
        self.hold_box: Optional[Box] = None

    def on_update(self, delta_time: float):
        # call on_update on the owned Box
        self.box.on_update(delta_time)

    def on_draw(self):
        """ Draw this section """
        if self.selected:
            # Section is selected when mouse is within its boundaries
            arcade.draw_lrtb_rectangle_filled(self.left, self.right, self.top,
                                              self.bottom, arcade.color.GRAY)
            arcade.draw_text(f'You\'re are on the {self.name}', self.left + 30,
                             self.top - 50, arcade.color.BLACK, 16)

        # draw the box
        self.box.draw()

    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float,
                      _buttons: int, _modifiers: int):
        # if we hold a box, then whe move it at the same rate the mouse moves
        if self.hold_box:
            self.hold_box.position = x, y

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # if we pick a Box with the mouse, "hold" it and stop its movement
        if self.box.collides_with_point((x, y)):
            self.hold_box = self.box
            self.hold_box.stop()

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        # if hold_box is True because we pick it with on_mouse_press
        # then release the Box
        if self.hold_box:
            self.hold_box.release()

    def on_mouse_enter(self, x: float, y: float):
        # select this section
        self.selected = True

    def on_mouse_leave(self, x: float, y: float):
        # unselect this section
        self.selected = False

        # if we are holding this section box and we leave the section
        # we release the box as if we release the mouse button
        if self.hold_box:
            self.hold_box.release()

class MenuView(arcade.View):

    def __init__(self):
        super().__init__()

    def on_draw(self):
        self.clear()

class GameView(arcade.View):

    def __init__(self):
        super().__init__()

        # add sections to the view

        # 1) First section holds half of the screen
        self.add_section(t.TurtleScreen(0, 0, self.window.width / 2,
                                    self.window.height))

        # 2) Second section holds the other half of the screen
        self.add_section(c.Console(self.window.width / 2, 0,
                                    self.window.width / 2, self.window.height,
                                    name='Right'))

        print(self.window.width)
        print(self.window.height)

    def on_draw(self):
        # clear the screen
        self.clear(arcade.color.BEAU_BLUE)

        # draw a line separating each Section
        arcade.draw_line(self.window.width / 2, 0, self.window.width / 2,
                         self.window.height, arcade.color.BLACK, 1)

