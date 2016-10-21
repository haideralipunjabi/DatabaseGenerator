#Database Manager
import sqlite3
import os


databaseName = "PokemonGO.db"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.abspath(os.path.join(BASE_DIR, databaseName))


class DatabaseManager:


    def __init__(self):
        if not os.path.isfile(DB_DIR):
            self.create_database()
        else:
            if self.overwrite():
                os.remove(DB_DIR)
                self.create_database()
            else:
                exit()

    def overwrite(self):  #Function to get user input on whether to overwrite the existing database
         user_input_overwrite = str(input('Old database found, Overwrite? (Y/N): '))
         if user_input_overwrite.lower() == 'y':
             return True
         if user_input_overwrite.lower() == 'n':
            return False
         else:
             print('INVALID INPUT')
             self.overwrite()



    def android_support(self):  #Function to get user input on whether to make the database compatible with android apps
        user_input = str(input("Add Support for Android? (Y/N): "))
        if user_input.lower() == 'y':
            return True
        if user_input.lower() == 'n':
            return False
        else:
            print('INVALID INPUT')
            self.android_support()




    def create_database(self):  #Function to create the database file, and execute table creation code

        self.connection = sqlite3.connect(DB_DIR)
        self.cursor = self.connection.cursor()
        #Default table 'PokeGODB' creation
        self.cursor.execute('''CREATE TABLE [PokeGODB] (
	    [_id]	integer NOT NULL,
	    [DexID]	integer,
	    [Name]	varchar,
        [AvgMultiplier]	varchar(4),
        [MaxLimit]	integer,
        [amzCP]	integer,
        [goodCP]	integer,
        [evoName]	varchar ,
        [evoDex]	integer,
        [evoMaxLimit]	integer,
        [family]	varchar,
        [Candy]	integer,
        PRIMARY KEY ([_id])

        )''')
        #Optional table to add compatibility with android apps
        if self.android_support():
               self.cursor.execute('''CREATE TABLE "android_metadata" (
               "locale" TEXT DEFAULT 'en_US'
                )''')
        self.connection.commit()
        #Function to insert the data of a single Pokemon
    def update_database(self, DexID, Name, AvgMultiplier, MaxLimit, amzCP, goodCP, evoName, evoDex, evoMaxLimit, family, Candy):
        connection = sqlite3.connect(DB_DIR)
        self.cursor.execute('''INSERT INTO PokeGODB(_id, DexID, Name,AvgMultiplier, MaxLimit, amzCP, goodCP, evoName, evoDex,evoMaxLimit, family, Candy) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''', (self.maxid(), DexID, Name, AvgMultiplier, MaxLimit, amzCP, goodCP, evoName, evoDex, evoMaxLimit, family, Candy))
        self.connection.commit()
    def maxid(self):
        self.cursor.execute('SELECT MAX(_id) FROM PokeGODB')
        id = self.cursor.fetchone()[0]
        if(id == None):
            id = 0
        return id +1

    def end(self):
        print("All Done!!!")
        self.connection.close()