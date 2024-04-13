import arcade

import arcade.gui

import game as g
import turtle

import turtle as t

import arcade.gui.widgets
from arcade.experimental.uistyle import UIFlatButtonStyle

# Render button
default_style = {
    "normal": UIFlatButtonStyle(
        font_size=12,
        font_name="Kenney Mini Square",
        font_color=arcade.color.BRUNSWICK_GREEN,
        bg=arcade.color.WHITE,
        border=None,
        border_width=0,
    ),
    "hover": UIFlatButtonStyle(
        font_size=12,
        font_name="Kenney Mini Square",
        font_color=arcade.color.WHITE,
        bg=arcade.color.BRUNSWICK_GREEN,
        border=None,
        border_width=2,
    ),
    "press": UIFlatButtonStyle(
        font_size=12,
        font_name="Kenney Mini Square",
        font_color=arcade.color.WHITE,
        bg=arcade.color.BRUNSWICK_GREEN,
        border=arcade.color.ARMY_GREEN,
        border_width=2,
    ),
    "disabled": UIFlatButtonStyle(
        font_size=12,
        font_name="Kenney Mini Square",
        font_color=arcade.color.WHITE,
        bg=arcade.color.COOL_GREY,
        border=arcade.color.ASH_GREY,
        border_width=2,
    )
}


class Console(arcade.View):
    """
    This represents a part of the View defined by its
    boundaries (left, bottom, etc.)
    """

    def __init__(self, left: int, bottom: int, width: int, height: int, game: g.Game,
                 **kwargs):
        super().__init__()

        self.turtle = t.TurtleScreen(0, 0, self.window.width / 2,
                                           self.window.height)
        self.add_section(self.turtle)

        self.left = left
        self.right = left + width
        self.top = bottom + height
        self.bottom = bottom
        self.width = width
        self.height = height
        self.code = "HI!!!"
        self.game = game
        self.combined_code = []

        self.start_code = game.get_level_data().pre_code
        self.end_code = game.get_level_data().post_code
        self.button_values = game.get_level_data().buttons

        self.user_input = []

        self.manager = arcade.gui.UIManager()

        button_1 = self.create_button(self.button_values[0])
        button_2 = self.create_button(self.button_values[1])
        button_3 = self.create_button(self.button_values[2])
        button_4 = self.create_button(self.button_values[3])
        button_5 = self.create_button(self.button_values[4])
        button_6 = self.create_button(self.button_values[5])
        button_7 = self.create_button(self.button_values[6])
        button_8 = self.create_button(self.button_values[7])

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
            self.add_user_input(self.button_values[0])

        @button_2.event("on_click")
        def on_click_switch_button(event):
            self.add_user_input(self.button_values[1])

        @button_3.event("on_click")
        def on_click_switch_button(event):
            self.add_user_input(self.button_values[2])

        @button_4.event("on_click")
        def on_click_switch_button(event):
            self.add_user_input(self.button_values[3])

        @button_5.event("on_click")
        def on_click_switch_button(event):
            self.add_user_input(self.button_values[4])

        @button_6.event("on_click")
        def on_click_switch_button(event):
            self.add_user_input(self.button_values[5])

        @button_7.event("on_click")
        def on_click_switch_button(event):
            self.add_user_input(self.button_values[6])

        @button_8.event("on_click")
        def on_click_switch_button(event):
            self.add_user_input(self.button_values[7])

        @clear_button.event("on_click")
        def on_click_switch_button(event):
            self.user_input = []

        @run_button.event("on_click")
        def on_click_switch_button(event):
            moves = game.check_solution(self.user_input)
            if moves:
                self.turtle.player_sprite.move(moves)

        self.manager.add(grid)

    def on_draw(self):
        """ Draw this section """
        # arcade.start_render()
        # self.clear(arcade.color.BEAU_BLUE)
        self.clear(arcade.color.WHITE)

        arcade.draw_lrtb_rectangle_filled(self.left, self.left + 30, self.top,
                                          self.bottom, arcade.color.LIGHT_GRAY)

        arcade.draw_lrtb_rectangle_filled(self.left, self.right, self.top // 3,
                                          self.bottom, arcade.color.APPLE_GREEN)

        lines_offset = self.top * (2/3) // 22 + 10

        for i in range(14):
            arcade.draw_text(f'{i + 1}', self.left + 10,
                             self.top - 30 - (i * lines_offset), arcade.color.BLACK, 12,
                             font_name="Kenney Pixel")

        user_code = ""
        for word in self.user_input:
            user_code += word + " "

        self.combined_code = []
        self.combined_code += self.start_code
        self.combined_code.append(user_code)

        self.combined_code += self.end_code

        for line in range(len(self.combined_code)):
            arcade.draw_text(f'{self.combined_code[line]}', self.left + 35,
                             self.top - 30 - (line * lines_offset) - 4, arcade.color.BLACK, 14,
                             font_name="Kenney Mini Square")

        #arcade.draw_text(f'{user_code}', self.left + 30,
                         #self.top - 50, arcade.color.WHITE, 16)

        # draw a line separating each Section
        arcade.draw_line(self.window.width / 2, 0, self.window.width / 2,
                         self.window.height, arcade.color.BLACK, 1)

        self.manager.draw()

    def create_button(self, display):
        return arcade.gui.UIFlatButton(width=97,
                                       height=60,
                                       text=display,
                                       style=default_style)

    def on_show_view(self):
        """ Render the screen. """
        self.manager.enable()

    def on_hide_view(self):
        # Disable the UIManager when the view is hidden.
        self.manager.disable()

    def add_user_input(self, user_Input):
        if len(self.user_input) < 8:
            self.user_input.append(user_Input)
