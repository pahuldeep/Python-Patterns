# Frog world
from Developer.dev import Dev
from Developer.ai import AI

class HumanWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t------ Human World -------'

    def make_character(self):
        return Dev(self.player_name)

    def make_obstacle(self):
        return AI()
