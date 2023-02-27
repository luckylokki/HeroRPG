from data.textborders import *
from data.hero import Warrior


class Healer(Warrior):
    def __init__(self):
        super().__init__(name='Torvald')
        self.gold = 10000

    def heal_hero(self, hero):
        if hero.gold < 10:
            lefttext_system_ml(f'{self.name} says: ')
            lefttext_system_g("    You havn't enogh money!")
            lefttext_system_g("    You need 10 gold for heal")
        else:
            if hero.hp == hero.max_hp:
                lefttext_system_ml(f'{self.name} says: ')
                lefttext_system_g("    You dont need it. Your HP is 100.")
            elif hero.hp < hero.max_hp:
                hero.gold -= 10
                self.gold += 10
                hero.hp += 20
                if hero.hp > hero.max_hp:
                    hero.hp = hero.max_hp
                lefttext_system_ml(f'{self.name} says: ')
                lefttext_system_g("    I heal you 20 HP")
    def resurrect(self,hero):
        if hero.gold < 100:
            lefttext_system_ml(f'{self.name} says: ')
            lefttext_system_g("    You havn't enogh money!")
            lefttext_system_g("    You need 100 gold for resurrect")

        else:
            if hero.hp == hero.max_hp:
                lefttext_system_ml(f'{self.name} says: ')
                lefttext_system_g("    You dont need it. Your HP is 100.")
            elif hero.hp < hero.max_hp:
                hero.gold -= 100
                self.gold += 100
                hero.hp += hero.max_hp
                hero.is_alive = True
                if hero.hp > hero.max_hp:
                    hero.hp = hero.max_hp
                lefttext_system_ml(f'{self.name} says: ')
                lefttext_system_g("    Welcome back hero!")

