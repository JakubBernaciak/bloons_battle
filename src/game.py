from player import Player


class Game():
    def __init__(self, p1_name, p2_name):
        self.p1: Player = Player(p1_name)
        self.p2: Player = Player(p2_name)
        self.round = 1
