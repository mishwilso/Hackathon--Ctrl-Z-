"""
Game
"""
import level as lvl


class Game():

    def __init__(self, level=1):
        self.level_num = level
        self.lives = 3
        self.level_data = lvl.Level(self.level_num)

    def check_solution(self, user_solution):
        """
        runs the user parsed code
        """
        if self.parse_code(user_solution) == None:
            return False
        else: 
            return self.parse_code(user_solution)

    def set_level(self, new_level):
        self.level_num = new_level
        self.level_data = lvl.Level(self.level_num)

    def get_level_data(self):
        return self.level_data

    def parse_code(self, code):
        """
        return a list of move instructions for the turtle parsed from the user code
        """
        moves = []

        moves.append(self.level_data.parsed_pre_code)

        # if the user input is a move command and the next input is an integer
        if code[0][0] == "m":
            if isinstance(code[1],(int)):
                moves.append(code)
            else:
                return None

        if code[0].contains("speed"):
            if code[1] == "=":
                if isinstance(code[2],(int)):
                    moves.append(code)
                else: 
                    return None
            else:
                return None
    
        return moves




