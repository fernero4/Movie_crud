from .connection_db import Conexion_db
from tkinter import messagebox


def Create_table():
    conexion = Conexion_db()
    sql = '''
    CREATE TABLE movies(
        id_movie INTEGER, 
        name VARCHAR(50),
        duration VARCHAR(10),
        genre VARCHAR(30),
        PRIMARY KEY(id_movie AUTOINCREMENT)
    )
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.Close_db()
        messagebox.showinfo('Create record', 'Table create successfully')
    except:
        messagebox.showwarning('Create DB', 'the table is already created')


def Delete_table():
    conexion = Conexion_db()
    sql = 'DROP TABLE movies'

    try:
        conexion.cursor.execute(sql)
        conexion.Close_db()
        messagebox.showinfo('Eliminate record',
                            'Table eliminated successfully')
    except:
        messagebox.showerror('Eliminate record',
                             "There's no table to eliminate")


class Movie:
    def __init__(self, name, duration, genre):
        self.id_movie = None
        self.name = name
        self.duration = duration
        self.genre = genre

    def __str__(self):
        return f'Movie [{self.name}, {self.duration}, {self.genre}]'


def Save_movies(movie):
    conexion = Conexion_db()
    sql = f"""
    INSERT INTO movies (name, duration, genre)
    VALUES('{movie.name}', '{movie.duration}', '{movie.genre}')
    """
    try:
        conexion.cursor.execute(sql)
        conexion.Close_db()
    except:
        messagebox.showerror('Error',
                             "There's no table to insert the movie, create one first")


def show_movies():
    conexion = Conexion_db()
    list_movie = []
    sql = 'SELECT * FROM movies'
    try:
        conexion.cursor.execute(sql)
        list_movie = conexion.cursor.fetchall()
        conexion.Close_db()
    except:
        messagebox.showwarning('Conexion to DB', 'Create a table first')
    return list_movie


def Edit_movie(movie, id_movie):
    conexion = Conexion_db()
    sql = f"""
    UPDATE movies
    SET name = '{movie.name}', duration = '{movie.duration}', genre = '{movie.genre}'
    WHERE id_movie={id_movie}
    """
    try:
        conexion.cursor.execute(sql)
        conexion.Close_db()
    except:
        messagebox.showerror('Error',
                             "This record could not be edited")


def Delete(id_movie):
    conexion = Conexion_db()
    sql = f'DELETE FROM movies WHERE id_movie={id_movie}'

    try:
        conexion.cursor.execute(sql)
        conexion.Close_db()
    except:
        messagebox.showerror('Error',
                             "Could not delete record")
