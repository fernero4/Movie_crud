import sqlite3


class Conexion_db:
    def __init__(self):
        self.data_base = 'C:/Users/ferna/Downloads/python/CRUD/db/movies.db'
        self.conexion = sqlite3.connect(self.data_base)
        self.cursor = self.conexion.cursor()

    def Close_db(self):
        self.conexion.commit()
        self.conexion.close()
