import arcade

import arcade.gui

import arcade.gui.widgets
from arcade.experimental.uistyle import UIFlatButtonStyle

# Render button
default_style = {
    "normal": UIFlatButtonStyle(
        font_size=12,
        font_name=("calibri", "arial"),
        font_color=arcade.color.BRUNSWICK_GREEN,
        bg=arcade.color.WHITE,
        border=None,
        border_width=0,
    ),
    "hover": UIFlatButtonStyle(
        font_size=12,
        font_name=("calibri", "arial"),
        font_color=arcade.color.WHITE,
        bg=arcade.color.BRUNSWICK_GREEN,
        border=None,
        border_width=2,
    ),
    "press": UIFlatButtonStyle(
        font_size=12,
        font_name=("calibri", "arial"),
        font_color=arcade.color.WHITE,
        bg=arcade.color.BRUNSWICK_GREEN,
        border=arcade.color.ARMY_GREEN,
        border_width=2,
    ),
    "disabled": UIFlatButtonStyle(
        font_size=12,
        font_name=("calibri", "arial"),
        font_color=arcade.color.WHITE,
        bg=arcade.color.COOL_GREY,
        border=arcade.color.ASH_GREY,
        border_width=2,
    )
}


class Console(arcade.Section):
    """
    This represents a part of the View defined by its
    boundaries (left, bottom, etc.)
    """

    def __init__(self, left: int, bottom: int, width: int, height: int,
                 **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)
        self.manager = arcade.gui.UIManager()

        button_1 = self.create_button("speed")
        button_2 = self.create_button("+")
        button_3 = self.create_button("-")
        button_4 = self.create_button("*")
        button_5 = self.create_button("=")
        button_6 = self.create_button("==")
        button_7 = self.create_button("-")
        button_8 = self.create_button("#")

        clear_button = arcade.gui.UIFlatButton(x=left,
                                               y=bottom,
                                               width=195,
                                               height=60,
                                               text="Clear",
                                               style=default_style)

        run_button = arcade.gui.UIFlatButton(width=195,
                                             height=60,
                                             text="Run",
                                             style=default_style)

        quit_button = arcade.gui.UIFlatButton(x=100,
                                              y=160,
                                              width=200,
                                              height=60,
                                              text="Quit",
                                              style=default_style)

        grid = arcade.gui.UIGridLayout(x=left, y=bottom, column_count=4, row_count=3, horizontal_spacing=5,
                                       vertical_spacing=10)
        grid.add(button_1, col_num=0, row_num=0)
        grid.add(button_2, col_num=1, row_num=0)
        grid.add(button_3, col_num=2, row_num=0)
        grid.add(button_4, col_num=3, row_num=0)
        grid.add(button_5, col_num=0, row_num=1)
        grid.add(button_6, col_num=1, row_num=1)
        grid.add(button_7, col_num=2, row_num=1)
        grid.add(button_8, col_num=3, row_num=1)
        grid.add(clear_button, col_num=0, row_num=2, col_span=2)
        grid.add(run_button, col_num=2, row_num=2, col_span=2)

        self.selected: bool = False  # if this section is selected

        @button_1.event("on_click")
        def on_click_switch_button(event):
            print("button_1")

        @button_2.event("on_click")
        def on_click_switch_button(event):
            print("button_2")

        @button_3.event("on_click")
        def on_click_switch_button(event):
            print("button_3")

        @button_4.event("on_click")
        def on_click_switch_button(event):
            print("button_4")

        @button_5.event("on_click")
        def on_click_switch_button(event):
            print("button_5")

        @button_6.event("on_click")
        def on_click_switch_button(event):
            print("button_6")

        @button_7.event("on_click")
        def on_click_switch_button(event):
            print("button_7")

        @button_8.event("on_click")
        def on_click_switch_button(event):
            print("button_8")

        @clear_button.event("on_click")
        def on_click_switch_button(event):
            print("CLEAR!!")

        @quit_button.event("on_click")
        def on_click_switch_button(event):
            print("HELLO!!")

        self.manager.add(grid)
        self.manager.add(quit_button)


    def on_draw(self):
        """ Draw this section """
        # arcade.start_render()

        arcade.draw_lrtb_rectangle_filled(self.left, self.right, self.top // 2,
                                          self.bottom, arcade.color.APPLE_GREEN)
        arcade.draw_text(f'You\'re are on the {self.name}', self.left + 30,
                         self.top - 50, arcade.color.BLACK, 16)

        self.manager.draw()

    def create_button(self, display):
        return arcade.gui.UIFlatButton(width=95,
                                       height=60,
                                       text=display,
                                       style=default_style)

    def on_show_view(self):
        """ Render the screen. """
        self.manager.enable()

    def on_hide_view(self):
        # Disable the UIManager when the view is hidden.
        self.manager.disable()
