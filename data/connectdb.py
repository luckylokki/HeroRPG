from sqlite3 import connect
from data.textborders import *
"""Class for database connection"""
class Connection:
    def __init__(self):
        self.conn = connect('./db/game.db')
    def __enter__(self):
        cur = self.conn.cursor()

        return cur
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()

    # Save player in game
    @staticmethod
    def save_player(player):
        user = tuple(player.values())
        with Connection() as c:
            sqlite_update_query = """Update players set uname=?,hp=?,max_hp=?,atk=?,def=?,lvl=?,gold=?,exp=?,pve=? where uname = ?;"""
            column_values = (user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8], user[0])
            c.execute(sqlite_update_query, column_values)
        lefttext_system_gl("Data is saved.")