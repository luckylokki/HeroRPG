from sqlite3 import connect
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