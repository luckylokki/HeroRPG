import os
import csv
from sqlite3 import connect
from alive_progress import alive_bar
from data.textborders import *


class InitDB:
    def __init__(self):
        maintext_system_l('DATABASE DOES NOT EXIST')
        lefttext_system_gl("Create database...")
        os.mkdir('./db/')
        lefttext_system_gl('Loading Database:')

    def database_init(self):
        with alive_bar() as bar:
            lefttext_system_gl('Connecting to database')
            conn = connect('./db/game.db')
            cur = conn.cursor()
            lefttext_system_gl('Creating table for players')
            # Create players table
            cur.execute("""CREATE TABLE IF NOT EXISTS players(
               id INTEGER PRIMARY KEY,
               uname TEXT,
               hp INTEGER,
               max_hp INTEGER,
               atk INTEGER,
               def INTEGER,
               lvl INTEGER,
               gold INTEGER,
               exp REAL,
               pve INTEGER);
            """)

            # commit the changes
            conn.commit()
            # close the database connection to let other operations use it
            conn.close()

            bar()
