import arcade as ac
import windows as wind
import level as lvl
import console



def main():
    # create the window
    window = ac.Window(800, 640)

    # create the custom View. Sections are initialized inside the GameView init
    #view = wind.GameView()
    view = console.Console(window.width / 2, 0,
                            window.width / 2, window.height,
                            name='Right')

    view.add_section(wind.ScreenPart(0, 0, window.width / 2,
                                window.height, name='Left'))

    # show the view
    window.show_view(view)

    # run arcade loop
    window.run()


if __name__ == '__main__':
    main()
