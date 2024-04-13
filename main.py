import arcade as ac
import arcade.gui
import windows as wind
import level as lvl
import console
import game as g
import turtle as t

game = g.Game()

def main():
    # create the window
    window = ac.Window(800, 640)

    # create the custom View. Sections are initialized inside the GameView init
    # view = wind.GameView()



    # view = console.Console(window.width / 2, 0,
    #                        window.width / 2, window.height,
    #                        game)
    #
    # view.add_section(t.TurtleScreen(0, 0, window.width / 2,
    #                                 window.height))

    view = MenuView()

    # show the view
    window.show_view(view)

    # run arcade loop
    window.run()

class MenuView(ac.View):
    def __init__(self):
        super().__init__()
        self.manager = ac.gui.UIManager()

        play_button = arcade.gui.UIFlatButton(x= (self.window.width // 2) - 100,
                                              y=self.window.height // 2,
                                              width=200,
                                              height=60,
                                              text="Play")

        # Initialise the button with an on_click event.
        @play_button.event("on_click")
        def on_click_switch_button(event):
            game_view = LevelView()
            self.window.show_view(game_view)

        self.manager.add(play_button)

        self.game_view = None  # Placeholder for the game view instance

        # Create theme object and set theme

    def on_show(self):
        arcade.set_background_color(arcade.color.DARK_BLUE)

    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.manager.draw()

    def on_show_view(self):
        """ Render the screen. """
        self.manager.enable()

    def on_hide_view(self):
        # Disable the UIManager when the view is hidden.
        self.manager.disable()

class LevelView(ac.View):
    def __init__(self):
        super().__init__()
        self.manager = ac.gui.UIManager()

        button_list = []
        for i in range(30):
            button_list.append(self.create_button(i + 1))

        @button_list[0].event("on_click")
        def on_click_switch_button(event):
            game.set_level(1)
            view = console.Console(self.window.width / 2, 0,
                                  self.window.width / 2, self.window.height,
                                  game)

            view.add_section(t.TurtleScreen(0, 0, self.window.width / 2,
                                           self.window.height))

            self.window.show_view(view)



        @button_list[1].event("on_click")
        def on_click_switch_button(event):
            print(1)

        @button_list[2].event("on_click")
        def on_click_switch_button(event):
            print(2)

        grid = arcade.gui.UIGridLayout(x=50, y=20, column_count=6, row_count=5, horizontal_spacing=5,
                                       vertical_spacing=10)
        button_count = 0
        for row in range(5):
            for col in range(6):
                grid.add(button_list[button_count], col_num=col, row_num=row)
                button_count += 1

        self.manager.add(grid)
        self.game_view = None  # Placeholder for the game view instance

        # Create theme object and set theme

    def on_show(self):
        arcade.set_background_color(arcade.color.GREEN_YELLOW)

    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.manager.draw()

    def on_show_view(self):
        """ Render the screen. """
        self.manager.enable()

    def on_hide_view(self):
        # Disable the UIManager when the view is hidden.
        self.manager.disable()

    def create_button(self, display):
        return arcade.gui.UIFlatButton(width=110,
                                       height=110,
                                       text=display)


if __name__ == '__main__':
    main()
