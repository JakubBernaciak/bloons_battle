import settings


class Player():
    def __init__(self, name):
        self.name = name
        self.health = settings.max_health
        self.money = settings.money_on_start
