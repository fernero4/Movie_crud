import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from model.movies_db import Create_table, Delete_table, show_movies, Edit_movie, Delete
from model.movies_db import Movie, Save_movies


def help():
    messagebox.showinfo("Catalogue's movies",
                        "this is an aplication of example for a catalogue")


def menu_bar(root):
    menu = tk.Menu(root)
    root.config(menu=menu, width=300, height=300)

    start_menu = tk.Menu(menu, tearoff=0)
    help_menu = tk.Menu(menu, tearoff=0)

    menu.add_cascade(label='File', menu=start_menu)
    menu.add_cascade(label='Help', menu=help_menu)  # , command=help(root)

    start_menu.add_command(
        label='Create a record  in DB', command=Create_table)
    start_menu.add_command(
        label='Eliminate a record  in DB', command=Delete_table)
    start_menu.add_command(label='Leave', command=root.destroy)
    help_menu.add_command(label='General information', command=help)


class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=800, height=480, background='#D4E0FA')
        self.root = root
        self.pack()
        self.id_movie = None

        self.movies_fields()
        self.Disable_fields()
        self.Table_movies()

    def movies_fields(self):
        # labels
        self.name_label = tk.Label(self, text='Name: ', background='#D4E0FA')
        self.name_label.config(font=('Arial', 14, 'bold'))
        self.name_label.grid(row=0, column=0, padx=10, pady=10)

        self.duration_label = tk.Label(
            self, text='Duration: ', background='#D4E0FA')
        self.duration_label.config(font=('Arial', 14, 'bold'))
        self.duration_label.grid(row=1, column=0, padx=10, pady=10)

        self.genre_label = tk.Label(self, text='Genre: ', background='#D4E0FA')
        self.genre_label.config(font=('Arial', 14, 'bold'))
        self.genre_label.grid(row=2, column=0, padx=10, pady=10)

        # stringvars
        self.name = tk.StringVar()
        self.duration = tk.StringVar()
        self.genre = tk.StringVar()

        # entrys
        self.name_entry = tk.Entry(self)
        self.name_entry.config(width=50, textvariable=self.name,
                               font=('Arial', 14, 'bold'))
        self.name_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        self.duration_entry = tk.Entry(self)
        self.duration_entry.config(width=50, textvariable=self.duration,
                                   font=('Arial', 14, 'bold'))
        self.duration_entry.grid(
            row=1, column=1, padx=10, pady=10, columnspan=2)

        self.genre_entry = tk.Entry(self)
        self.genre_entry.config(width=50, textvariable=self.genre,
                                font=('Arial', 14, 'bold'))
        self.genre_entry.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        # buttons
        self.new_buttom = tk.Button(
            self, text='New', command=self.Enable_fields)
        self.new_buttom.config(width=20, font=(
            'Arial', 14, 'bold'), fg='#000000', bg='#5C6AB6', cursor='hand2', activebackground='#515FAB')
        self.new_buttom.grid(row=4, column=0, padx=10, pady=10)

        self.save_buttom = tk.Button(self, text='Save', command=self.Save)
        self.save_buttom.config(width=20, font=(
            'Arial', 14, 'bold'), fg='#000000', bg='#5C6AB6', cursor='hand2', activebackground='#515FAB')
        self.save_buttom.grid(row=4, column=1, padx=10, pady=10)

        self.cancel_buttom = tk.Button(
            self, text='Cancel', command=self.Disable_fields)
        self.cancel_buttom.config(width=20, font=(
            'Arial', 14, 'bold'), fg='#000000', bg='#5C6AB6', cursor='hand2', activebackground='#515FAB')
        self.cancel_buttom.grid(row=4, column=2, padx=10, pady=10)

        self.edit_buttom = tk.Button(self, text='Edit', command=self.Edit_data)
        self.edit_buttom.config(width=20, font=(
            'Arial', 14, 'bold'), fg='#000000', bg='#5C6AB6', cursor='hand2', activebackground='#515FAB')
        self.edit_buttom.grid(row=6, column=0, padx=10, pady=10)

        self.Eliminate_buttom = tk.Button(
            self, text='Eliminate', command=self.Delete_data)
        self.Eliminate_buttom.config(width=20, font=(
            'Arial', 14, 'bold'), fg='#000000', bg='#5C6AB6', cursor='hand2', activebackground='#515FAB')
        self.Eliminate_buttom.grid(row=6, column=1, padx=10, pady=10)

    def Enable_fields(self):
        self.name_entry.config(state='normal')
        self.duration_entry.config(state='normal')
        self.genre_entry.config(state='normal')

        self.save_buttom.config(state='normal')
        self.cancel_buttom.config(state='normal')

    def Disable_fields(self):
        self.id_movie = None
        self.name.set('')
        self.duration.set('')
        self.genre.set('')

        self.name_entry.config(state='disabled')
        self.duration_entry.config(state='disabled')
        self.genre_entry.config(state='disabled')

        self.save_buttom.config(state='disabled')
        self.cancel_buttom.config(state='disabled')

    def Save(self):
        movie = Movie(self.name.get(), self.duration.get(), self.genre.get())
        if self.id_movie == None:
            Save_movies(movie)
        else:
            Edit_movie(movie, self.id_movie)
        self.Table_movies()
        self.Disable_fields()

    def Table_movies(self):
        self.movies_list = show_movies()
        self.movies_list.reverse()
        self.table = ttk.Treeview(
            self, columns=('Nombre', 'Duracion', 'Genero'))
        self.table.grid(row=5, column=0, columnspan=4, sticky='nse')

        # scrollbar
        self.scroll = ttk.Scrollbar(
            self, orient='vertical', command=self.table.yview)
        self.scroll.grid(row=5, column=4, sticky='nse')
        self.table.configure(yscrollcommand=self.scroll.set)

        self.table.heading('#0', text='ID')
        self.table.heading('#1', text='NAME')
        self.table.heading('#2', text='DURATION')
        self.table.heading('#3', text='GENRE')

        for movie in self.movies_list:
            self.table.insert('', 0, text=movie[0], values=(
                movie[1], movie[2], movie[3]))

    def Edit_data(self):
        try:
            self.id_movie = self.table.item(self.table.selection())['text']
            self.name_movie = self.table.item(
                self.table.selection())['values'][0]
            self.duration_movie = self.table.item(
                self.table.selection())['values'][1]
            self.genre_movie = self.table.item(
                self.table.selection())['values'][2]
            self.Enable_fields()

            self.name_entry.insert(0, self.name_movie)
            self.duration_entry.insert(0, self.duration_movie)
            self.genre_entry.insert(0, self.genre_movie)

        except:
            messagebox.showerror('Error', 'No record selected')

    def Delete_data(self):
        try:
            self.id_movie = self.table.item(self.table.selection())['text']
            Delete(self.id_movie)
            self.Table_movies()
            self.id_movie = None
        except:
            messagebox.showerror('Error', 'you did not select a record')
