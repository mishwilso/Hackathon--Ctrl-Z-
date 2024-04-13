import arcade

class Console(arcade.Section):
    """
    This represents a part of the View defined by its
    boundaries (left, bottom, etc.)
    """

    def __init__(self, left: int, bottom: int, width: int, height: int,
                 **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)

        self.selected: bool = False  # if this section is selected

    def on_update(self, delta_time: float):
        # call on_update on the owned Box
        pass


    def on_draw(self):
        """ Draw this section """
        arcade.draw_lrtb_rectangle_filled(self.left, self.right, self.top // 2,
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