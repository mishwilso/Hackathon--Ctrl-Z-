"""
Game
"""
import level as lvl

class Game():

    def __init__(self):
        self.level_num = 1
        self.lives = 3
        self.level_data = lvl.Level(self.level_num)

    def check_solution(self, user_solution):
        if user_solution == self.level_data.solve:
            self.level_num += 1
            return True
        else:
            self.lives -= 1
            return False

    def get_buttons(self):
        return self.level_data.buttons

    def set_level(self, new_level):
        self.level_num = new_level

    def get_level(self):
        return self.level_num

