from data.textborders import *
from random import randint,choice, uniform
class Mob:
    def __init__(self):
        with open("./data/mobs/mobs_names.txt") as names:
            lines = names.readlines()
        self.name = choice(lines).strip()
        self.max_hp = 100
        self.hp = self.max_hp
        self.atk_power = self.hp // 10
        self.def_power = 100 # not used
        self.lvl = 1
        self.exp = round(uniform(5.0, 25.0), 1)
        self.gold = randint(5, 100)


    def mob_info_dict(self):
        return {
            'Name': str(self.name),
            'EXP': str(str(self.exp)),
            'HP': str(str(self.hp) + '/' + str(self.max_hp)),
            'Gold': str(self.gold),
            'Atk': str(self.atk_power),
            'Def': str(self.def_power)
        }
    def is_alive(self):
        if self.hp > 0:
            return True
        elif self.hp <= 0:
            self.mob_dead()
            return False

    # Check mob death
    def mob_dead(self):
        self.hp = 0
        maintext_system_cl('(MOB DIED)')
        gridoutput(self.mob_info_dict())
    def reload(self):
        with open("./data/mobs/mobs_names.txt") as names:
            lines = names.readlines()
        self.name = choice(lines).strip()
        self.hp = self.max_hp
        self.exp = round(uniform(5.0, 25.0), 1)
        self.gold = randint(5, 100)
