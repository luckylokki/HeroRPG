'''Main parent class for player and npc'''
from data.textborders import *
from random import randint


class Warrior():
    def __init__(self, name, hp=100, max_hp=100, atk_power=30, def_power=30, lvl=1, gold=100, exp=0.0, pve=0):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.atk_power = atk_power #not used
        self.atk_power_s = self.hp // 10
        self.def_power = def_power #not used
        self.lvl = lvl
        self.gold = gold
        self.exp = exp
        self.max_exp = 100
        self.pve = pve

        self.is_alive = True


    # Data for printing
    def player_info_dict(self):
        return {
            'Name': str(self.name),
            'Level': str(self.lvl),
            'EXP': str(str(self.exp) + '/' + str(self.max_exp)),
            'HP': str(str(self.hp) + '/' + str(self.max_hp)),
            'Gold': str(self.gold),
            'Atk': str(self.atk_power_s),
            'Def': str(self.def_power),
            'PVE': str(self.pve)
        }

    # Data for queries
    def data_db(self):
        return {
            'Name': str(self.name),
            'HP': str(self.hp),
            'MAX_HP': str(self.max_hp),
            'Atk': str(self.atk_power_s),
            'Def': str(self.def_power),
            'Level': str(self.lvl),
            'Gold': str(self.gold),
            'EXP': str(self.exp),
            'PVE': str(self.pve)
        }

    # Check player death
    def player_dead(self, mob):
        self.hp = 0
        self.is_alive = False
        maintext_system('PLAYER DIED')
        lefttext_system_rl(f'You lose {mob.exp} of your EXP')
        lefttext_system_rl(f'You lose {mob.gold} of your Gold')
        lefttext_system_g('Note: You can use Healer to resurrect.')
        lefttext_system_m('Note: Pray to the old gods! Or die forever!')

    def lvl_up(self, value):
        self.lvl = self.lvl + value
        maintext_system_grats('LVL UP')
        centertext_grats('Congtaulations! You leveled up!')
    def lvl_down(self, value):
        if self.lvl <= 1:
            self.lvl = 1
        else:
            self.lvl = self.lvl - value
    def exp_up(self):
        if self.exp >= 100.0:
            self.lvl_up(1)
            self.exp = self.exp - 100.0
    def exp_down(self):
        if self.exp < 0 and self.lvl > 1:
            self.exp = self.max_exp + self.exp
            self.lvl_down(1)
        elif self.exp >= 0 and self.lvl == 1:
            self.exp = self.exp
            self.lvl = 1
        elif self.exp < 0 and self.lvl == 1:
            self.exp = 0
            self.lvl = 1
    def run(self, mob):
        self.gold -= mob.gold
        maintext_system_cl('MESSAGE')
        print(Fore.LIGHTRED_EX + f'You lose {mob.gold} gold')


    def atack(self, mob):
        self.pve += 1
        if mob.hp <= 0:
            lefttext_system_g(f'\nYou cant atack {mob.name} he is died...')
            return
        centertext_grats(f'The fight between {self.name} and {mob.name} is started!')
        while self.hp > 0 or mob.hp > 0:
            self_atack_random = randint(self.atk_power // 30, self.atk_power)
            mob_atack_random = randint(mob.atk_power // 30, mob.atk_power)
            self.hp -= mob_atack_random
            mob.hp -= self_atack_random
            if self.hp >= 1 and mob.hp <= 0:
                lefttext_system_gl(f'\n{self.name} kill the {mob.name}!!!')
                self.gold += mob.gold
                lefttext_system_grats(f'\nYou received {mob.exp} EXP and {mob.gold} gold {mob.name}')
                mob.gold = 0
                self.exp += mob.exp
                self.exp_up()
                break
            elif self.hp <= 0 and mob.hp >= 1:
                self.exp -= mob.exp
                self.exp_down()
                self.gold -= mob.gold
                if self.gold < 0:
                    self.gold = 0
                self.player_dead(mob)
                break
            elif mob.hp <= 0 and self.hp <= 0:
                lefttext_system_rl('\nBoth fell in fight!')
                break
            if mob_atack_random == 0:
                lefttext_system_m(f'{mob.name} missed! {self.name} left {self.hp} HP')
            else:
                lefttext_system_m(f'{self.name} damaged for {mob_atack_random} from {mob.name}! You have left {self.hp} HP')
            if self_atack_random == 0:
                lefttext_system_m(f'{self.name} missed! {mob.name} left {mob.hp} HP')
            else:
                lefttext_system_m(f'{mob.name} demaged for {self_atack_random} from {self.name}! Enemy has left {mob.hp} HP')
    # Joke-cheat, if use it your params will be 10050 =)
    def loki(self):
        self.lvl = 100500
        self.hp = 100500
        self.max_hp = 100500
        self.atk_power = 100500
        self.atk_power_s = 100500
        self.def_power = 100500
        self.gold = 100500
        self.is_alive = True
        maintext_system_grats('Wow! The gods heard you!')
        centertext_grats('Loki heard your prayer! And give 100500 powers!')
        centertext_grats('Look at your Hero Info press (i)')