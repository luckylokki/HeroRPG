from data.hero import Warrior, Healer
from data.db import InitDB
from data.connectdb import Connection
from data.textborders import *
from data.mobs import Mob
import os


class Game:
    res_counter = 0
    # Load player data from database for work
    def load_player_db(self):
        with Connection() as c:
            result = c.execute("SELECT * FROM players").fetchall()
        return result

    # Create new player and save it to database
    def new_player(self):
        maintext_system_cl('ENTER NAME')
        centertext_system_c('Your name, hero !\n')

        player_name = input('Name: ')
        while player_name == '' or player_name in [i[1] for i in self.load_player_db()]:
            maintext_system_cl('ENTER NAME')
            centertext_system("This name is busy!\n")
            centertext_system_c('Your name, hero !\n')
            player_name = input(Fore.LIGHTCYAN_EX + 'Name: ')
        else:
            # Create new player
            main_player = Warrior(player_name)
            self.player = main_player
            player_name = self.player
            # Create new player database record
            with Connection() as c:
                c.execute("INSERT INTO players (uname,hp,max_hp,atk,def,lvl,gold,exp,pve) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);",
                tuple(player_name.data_db().values()))
        return player_name

    # load player from save in database
    def load_player(self):
        maintext_system_cl('ENTER NAME')
        centertext_system_c('Please enter player name for load!\n')
        player_name = input(Fore.LIGHTCYAN_EX + 'Name: ')
        if player_name == 'b':
            self.game_loop()
        while player_name not in [i[1] for i in self.load_player_db()]:
            maintext_system_cl('ENTER NAME')
            centertext_system("Player not found\n")
            centertext_system_c('Please enter player name for load!\n')
            centertext_system_c('Press (b) for back.\n')
            player_name = input(Fore.LIGHTCYAN_EX + 'Name: ')
            if player_name == 'b':
                self.game_loop()
        else:
            # Load player from database
            player_loaded = [i for i in self.load_player_db() if i[1] == player_name]
            player_loaded = player_loaded[0]
            main_player = Warrior(name=player_loaded[1], hp=player_loaded[2], max_hp=player_loaded[3],
                                  atk_power=player_loaded[4], def_power=player_loaded[5],
                                  lvl=player_loaded[6], gold=player_loaded[7], exp=player_loaded[8],
                                  pve=player_loaded[9])
            self.player = main_player
            player_name = self.player
            maintext_system_cl('PLAYER LOADED')
        return player_name

    # Save player in game
    def save_player(self, player):
        user = tuple(player.values())

        with Connection() as c:
            sqlite_update_query = """Update players set uname=?,hp=?,max_hp=?,atk=?,def=?,lvl=?,gold=?,exp=?,pve=? where uname = ?;"""
            column_values = (user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8], user[0])
            c.execute(sqlite_update_query, column_values)
        lefttext_system_gl("Data is saved.")

    # Main game loop
    def game_loop(self):
        while True:
            # Try database folder and database file if not exist- create
            if not os.path.exists('./db/'):
                newdb = InitDB()
                newdb.database_init()
                self.player = self.new_player()
                # output player data
                gridoutput(self.player.player_info_dict())
                while self.player.is_alive():
                    self.main_game()
            # If database exist, create new player or load from save
            else:
                maintext_system_cl('')
                centertext_blue_l('Welcome to Text RPG Game')
                maintext_system_cl('')
                centertext_system_c("New(n) game load(l)")
                startch = input(Fore.LIGHTCYAN_EX + 'Choise: ')
                if startch == 'n' or startch == '':
                    # Make new global hero and enemy which will change over time
                    self.player = self.new_player()
                    # output player data
                    gridoutput(self.player.player_info_dict())
                    self.main_game()
                if startch == 'l':
                    self.player = self.load_player()
                    gridoutput(self.player.player_info_dict())
                    self.main_game()
    #main game actions
    def main_game(self):
        maingame = True
        self.enemy = self.new_enemy()
        while maingame:
            maintext_system_cl('MAIN ACTIONS')
            centertext_system_c('Move(m) Info(i) Healer(h)')
            centertext_system_c('Load(l) Save(s) Quit(q)')
            chs = input(Fore.LIGHTCYAN_EX + 'Choise: ')
            #Hero details info
            if chs.lower() == 'i':
                maintext_system_cl('HERO DETAILS')
                gridoutput(self.player.player_info_dict())
            #Battle mode
            elif chs.lower() == 'm':
                if self.player.is_alive == False and self.res_counter < 3:
                    maintext_system_l('You cant move, the player is died!')
                    centertext_system_g('You can resurrect!Use Healer(h)!')
                elif self.player.is_alive == True:
                    self.enemy.reload()
                    self.battle_info()
                    centertext_system_cl('You can fight or run!')
                    centertext_system_c('Fiaght(f), Run(r)')
                    lefttext_system_g(f'Note: If you run, you will pay {self.enemy.gold} Gold.')

                    chsm = input(Fore.LIGHTCYAN_EX + 'Choise: ')
                    # print(Style.RESET_ALL)
                    print(Fore.MAGENTA)
                    if chsm.lower() == 'f':
                        self.player.atack(self.enemy)

                        gridoutput(self.player.player_info_dict())
                    else:
                        self.player.run(self.enemy)
                        centertext_system_c('Next turn')

                else:
                    centertext_system_c('All attempts are used')
                #Load another player
            elif chs.lower() == 'l':
                maintext_system_cl('LOAD GAME')
                self.player = self.load_player()
                self.res_counter = 0
                gridoutput(self.player.player_info_dict())
                #Save your hero to database
            elif chs.lower() == 's':
                maintext_system_cl('SAVE GAME')
                self.save_player(self.player.data_db())
                #Use healer
            elif chs.lower() == 'h':
                maintext_system_cl('HEALER')
                if self.res_counter >= 3:
                    centertext_system_g("Sorry hero!")
                    centertext_system_g("You have already used your 3 attempts!")
                else:
                    if self.player.hp <= 0:
                        centertext_system_c('Healer can resurrect you!(Total 3 times)')
                        centertext_system_c(f'You use {self.res_counter} ressurect times.')
                        centertext_system_c('This will be cost 100 gold!')
                        centertext_system_c('Res? Yes(y), No(n), Pray(p)')
                        chsh = input(Fore.LIGHTCYAN_EX + 'Choise: ')
                        if chsh.lower() == 'y':
                            self.resur(self.player)
                            self.res_counter +=1
                            gridoutput(self.player.player_info_dict())
                        if chsh.lower() == 'p':
                            chsp = input(Fore.LIGHTCYAN_EX + 'Gods name: ')
                            if chsp.lower() == 'loki':
                                self.player.loki()
                            else:
                                maintext_system_grats('MESSAGE')
                                centertext_grats('This God dont hear you...')
                    else:
                        centertext_system_c('Healer can heal you 20 HP')
                        centertext_system_c('This will be cost 10 gold')
                        centertext_system_c('Heal? Yes(y), No(n)')
                        chsh = input(Fore.LIGHTCYAN_EX + 'Choise: ')
                        if chsh == 'y':
                            self.healing(self.player)
                            gridoutput(self.player.player_info_dict())
                # Exit from game
            elif chs.lower() == 'q':
                maintext_system_cl('QUIT')
                centertext_system_c('Press (y) for end the game.')
                centertext_system_c('Press any button for return: ')
                qchs = input(Fore.LIGHTCYAN_EX + 'Choise: ')
                print(Style.RESET_ALL)
                if qchs.lower() == 'y':
                    quit()
            elif chs.lower() == 'loki':
                self.player.loki()
    # Use healer for heal
    def healing(self, player):
        player = self.player
        # Create healer
        h_npc = Healer()
        #heal
        h_npc.heal_hero(player)
    def resur(self,player):
        player = self.player
        # Create healer
        h_npc = Healer()
        #resurrect
        h_npc.resurrect(player)
    def new_enemy(self):
        enemy = Mob()
        return enemy
    def battle_info(self):
        self.textwidth = 70
        maintext_system_cl('BATTLE INFO')
        centertext_system_cl(lr_justify('[HERO]', '[ENEMY]', self.textwidth))
        centertext_system_c(lr_justify('Name: ' + str(self.player.name), 'Name: ' + str(self.enemy.name), self.textwidth))
        centertext_system_c(lr_justify(str('Atk: ' + str(self.player.atk_power_s)),
                         str('Atk: ' + str(self.enemy.atk_power)),self.textwidth))
        centertext_system_c(lr_justify(str('HP: ' + str(self.player.hp) + '/' + str(self.player.max_hp)),
                         str('HP: ' + str(self.enemy.hp) + '/' + str(self.enemy.max_hp)), self.textwidth))
        centertext_system_c(lr_justify(str('XP: ' + str(self.player.exp) + '/' + str(self.player.max_exp)),
                         str('XP drop: ' + str(self.enemy.exp)),self.textwidth))
        centertext_system_c(lr_justify(str('Gold: ' + str(self.player.gold)),
                         str('Gold drop: ' + str(self.enemy.gold)),self.textwidth))

if __name__ == '__main__':
    newgame = Game()
    newgame.game_loop()
