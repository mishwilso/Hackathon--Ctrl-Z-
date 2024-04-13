import arcade as ac
import windows as wind
import level as lvl
import console
import game as g
import turtle as t


def main():
    # create the window
    window = ac.Window(800, 640)

    # create the custom View. Sections are initialized inside the GameView init
    # view = wind.GameView()

    game = g.Game()

    view = console.Console(window.width / 2, 0,
                           window.width / 2, window.height,
                           game)

    view.add_section(t.TurtleScreen(0, 0, window.width / 2,
                                    window.height))

    # show the view
    window.show_view(view)

    # run arcade loop
    window.run()


if __name__ == '__main__':
    main()
