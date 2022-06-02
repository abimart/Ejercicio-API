import sqlite3

class ConexionDateBase():
    def __init__(self):
        try:
            self.con = sqlite3.connect("database.db")
        except Exception as error:
            print(error)

    def createTable(self):
        try:
            self.cursor = self.con.cursor()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS data_lenguage (id INTEGER PRIMARY KEY AUTOINCREMENT, region CHAR, country CHAR, language CHAR, time REAL)")
            self.con.commit()
        except Exception as error:
            self.con.close()
            print (error)

    def insertData(self, fila):
        try:
            self.cursor = self.con.cursor()
            self.cursor.execute(f"INSERT INTO data_lenguage (region, country, language, time) VALUES (?, ?, ? ,?)", fila)
            self.con.commit()
        except Exception as error:
            self.con.close()
            print (error)

    def showTable(self):
        self.cursor = self.con.cursor()
        self.cursor.execute(f"SELECT region, country, language, time FROM data_lenguage")
        rows = self.cursor.fetchall()
        return rows 