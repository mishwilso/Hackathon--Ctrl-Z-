import arcade as ac
import windows as wind
import level as lvl

def main():
    # create the window
    window = ac.Window(800, 640)

    # create the custom View. Sections are initialized inside the GameView init
    view = wind.GameView()

    # show the view
    window.show_view(view)

    new_lvl = lvl.Level(1)
    print(new_lvl.get_start_pos)

    # run arcade loop
    window.run()


if __name__ == '__main__':
    main()