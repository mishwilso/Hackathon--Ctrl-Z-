"""
level.py
stores data for a level, including solution, starting positions, and buttons
"""

import arcade as ac
import json

class Level():
    
    def __init__(self, lvl_num):
        with open("level.json", 'r') as lvl_file:
            all_lvl = json.load(lvl_file)

        lvl_data = all_lvl.get(str(lvl_num))

        self.start_pos = lvl_data.get("start_pos")
        self.end_pos = lvl_data.get("end_pos")
        self.pre_code = lvl_data.get("pre_code")
        self.post_code = lvl_data.get("post_code")
        self.buttons = lvl_data.get("buttons")
        self.solve = lvl_data.get("solve")

    def get_start_pos(self):
        return self.start_pos
    
    def get_end_pos(self):
        return self.end_pos
