# fix self.matrix
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from random import choice
from tkinter import messagebox
from PIL import Image, ImageTk
import time

class GuessNameGameGUI:
    def __init__(self, master):
        self.master = master
        self.alphabet = [chr(n).lower() for n in range(ord('A'), ord('Z') + 1)]
        self.alphabet_mapping = {v: idx for idx, v in enumerate(self.alphabet)}
        self.names = []
        self.matrix = []
        self.count_names = []
        self.letters = []
        self.name = ""
        self.score = 0
        self.lives = 3
        self.attempts = 0

        self.create_gui()

    def create_gui(self):
        self.master.geometry('400x400')
        self.master.title('Guess My Name')

        self.fig, self.ax = plt.subplots()
        plt.close(self.fig)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.label_name = tk.Label(self.master, text='Guess a Name')
        self.label_name.grid(row=1, column=0, sticky="w")

        self.entry_name = tk.Entry(self.master)
        self.entry_name.grid(row=1, column=1, sticky="w")

        self.b_update = tk.Button(self.master, text='Update', command=self.update_plot)
        self.b_update.grid(row=2, column=0, columnspan=2, sticky="nsew")

        self.label_score = tk.Label(self.master, text='Score: 0')
        self.label_score.grid(row=3, column=0, sticky="w")

        self.label_lives = tk.Label(self.master, text='Lives: 3')
        self.label_lives.grid(row=3, column=1, sticky="w")

        self.label_attempts = tk.Label(self.master, text='Attempts: 0')
        self.label_attempts.grid(row=4, column=0, columnspan=2, sticky="w")

        self.guesses_label = tk.Label(self.master, text="Your guesses:")
        self.guesses_label.grid(row=5, column=1, sticky="e")

        self.guess_count_label = tk.Label(self.master, text=0)
        self.guess_count_label.grid(row=6, column=1, sticky="e")

        self.b_show_names = tk.Button(self.master, text="Show All Names", command=self.show_all_names)
        self.b_show_names.grid(row=7, column=0, columnspan=2, sticky="nsew")

        self.b_random_name = tk.Button(self.master, text="Random Name", command=self.show_random_name)
        self.b_random_name.grid(row=8, column=0, columnspan=2, sticky="nsew")

        self.random_name_label = tk.Label(self.master, text="")
        self.random_name_label.grid(row=9, column=0, columnspan=2, sticky="nsew")


        self.generate_names()
        self.create_matrix(self.names)
        self.update_guesses()
        self.draw_bar_plot()

    def generate_names(self):
        self.names = [choice(self.alphabet) + n + choice(self.alphabet) for n in self.alphabet]
        self.names.sort()

    def create_matrix(self, names):
        self.matrix = [[] for _ in range(len(self.alphabet))]
        for idx, name in enumerate(names):
            first_letter = name[0].lower()
            col_idx = self.alphabet_mapping[first_letter]
            self.matrix[col_idx].append(name)
        self.matrix = list(filter(lambda n: n, self.matrix))
        print('matrix: \n|', self.matrix)

    def extract_letter(self):
        self.letters = []
        for sublist in self.matrix:
            if sublist:
                first_letter = sublist[0][0]
                self.letters.append(first_letter)

    def get_x_y_to_plot(self):
        self.extract_letter()
        x = np.arange(len(self.letters))
        y = self._count_names(self.matrix)
        return x, y

    def draw_bar_plot(self):
        self.ax.clear()
        x, y = self.get_x_y_to_plot()
        self.ax.bar(x, y)
        self.ax.set_xticks(x)
        self.ax.set_xticklabels(self.letters)
        self.ax.set_title('Filtering and Sorting Names')
        self.ax.set_xlabel('Letters')
        self.ax.set_ylabel('Count')
        self.canvas.draw()

    def _count_names(self, matrix):
        output = [len(names) for names in matrix]
        return output

    def validate_given_name(self, name):
        if name.isdigit() or name[0].isdigit():
            raise ValueError('Only alphabet letters are allowed')
        elif len(name) >= 3:
            name = name[:3].lower()
            print('validate name: ', name)
        return name

    def is_name_in_matrix(self, target, filter=None):
        if not filter:
            output = any(target in names for names in self.matrix)
        elif filter:
            output = bool(list(filter(lambda names: target in names, self.matrix)))
        else:
            return False
        return output

    def update_guesses(self):
        guesses = self.guesses_label.cget("text")
        self.guesses_label.config(text=guesses)
        self.guess_count_label.config(text=str(len(guesses.split("\n"))))

    def update_score(self):
        self.label_score.config(text=f'Score: {self.score}')

    def update_lives(self):
        self.label_lives.config(text=f'Lives: {self.lives}')

    def update_attempts(self):
        self.label_attempts.config(text=f'Attempts: {self.attempts}')

    def update_plot(self):
        name = self.entry_name.get()
        print('entry name:', name)
        print('is_name: ', self.is_name_in_matrix(name))
        if name: # here if given any name will cut to validate len of name;
            name = self.validate_given_name(name)
            print('entry after validate: ', name)
        if name and self.is_name_in_matrix(name):
            messagebox.showinfo("Name", name)
            self.score += 1
            # self.lives -= 1
            self.update_score()
            self.update_lives()
        elif not name:
            ...
        elif not self.is_name_in_matrix(name):
            print('no name: ', name, self.is_name_in_matrix(name))
            print('all names: ', self.matrix)
            messagebox.showerror('Error', 'Invalid name!')
            self.lives -= 1
            self.update_lives()
            if self.lives <= 0:
                self.master.after(1000, self.show_game_over_message)
                # messagebox.showinfo('Game Over', 'You have run out of lives!')
                # self.master.destroy()
        else:
            if self.score > 3:
                messagebox.showinfo('You Win!', 'Congratulations ')
                self.master.destroy()


            messagebox.showerror('Error', 'Unknown Error!')
            self.master.destroy()

        self.generate_names()
        self.create_matrix(self.names)
        self.draw_bar_plot()
        self.attempts += 1
        self.update_attempts()


    def show_all_names(self):
        if not hasattr(self, "top") or not self.top.winfo_exists():
            self.top = tk.Toplevel(self.master)
            self.top.title('All Names')
            self.top.geometry('+%d+%d' % (self.master.winfo_rootx() + self.master.winfo_width(), self.master.winfo_rooty()))

            frame = tk.Frame(self.top, width=400, height=600, background='white')
            frame.pack_propagate(0)
            frame.pack(padx=10, pady=10)
            frame2 = tk.Frame(self.top)
            img_path = 'img/completed the game.jpg'
            w, h = 400, 250
            img = ImageTk.PhotoImage(Image.open(img_path).resize((w, h)))
            self.make_label(frame, 0, 0, w, h, img)

            # Configure the style for the labels
            style = ttk.Style()
            style.configure("NameLabel.TLabel", font=("Arial", 14, "bold"))
            
            for idx, name in enumerate(self.names):
                if idx < 5:
                    # Create a label for each name
                    label = ttk.Label(frame, text=name, style="NameLabel.TLabel")
                    label.grid(row=idx, column=0, sticky="w")
           
            # Center the frame within the window
            frame.update()
            frame.place(relx=0.5, rely=0.5, anchor="center")



    def show_all_names(self):
        if not hasattr(self, "top") or not self.top.winfo_exists():
            self.top = tk.Toplevel(self.master)
            self.top.title('All Names')
            self.top.geometry('+%d+%d' % (self.master.winfo_rootx() + self.master.winfo_width(), self.master.winfo_rooty()))
            
            self.add_picture(self.top)

            # Create a frame in the top window
            frame1 = tk.Frame(self.top)
            frame1.pack(padx=10, pady=10)
            
            # # Configure the style for the labels
            style = ttk.Style()
            style.configure("NameLabel.TLabel", font=("Arial", 14, "bold"))
            
            for idx, name in enumerate(self.names):
                """TODO: add x2 1 more column from proejct with x2 column in the toggle"""
                label = ttk.Label(frame1, text=name, style="NameLabel.TLabel")
                size = len(self.names)
                if idx < size:
                    if idx % size // (size // 2) == 0:
                        label.grid(row=1 + idx, column=0, sticky="w")
                    else:
                        label.grid(row=1 + idx - (size // 2), column=1, sticky="w")

                # if idx < 15:
                #     if idx < size:
                #     # Create a label for each name
                #         label.grid(row=idx + size, column=0, sticky="w")
                #     elif idx > size and idx < 10:
                #         label.grid(row=idx - size, column=2, sticky="w")
                #     else:
                #         label.grid(row=idx - size, column=1, sticky="w")

                    
            # Center the frame within the window
            frame1.update()
            frame1.place(relx=0.5, rely=0.7, anchor="center")

    def show_random_name(self):
        random_name = choice(self.names)
        self.random_name_label.config(text=random_name)

    def show_game_over_message(self):
        self.add_picture()
        time.sleep(1)
        # add delay 2 sec before close the gui
        self.master.after(2000, self.master.destroy())

    def add_picture(self, top):
        frame = tk.Frame(top, width=400, height=600, background='white')
        frame.pack_propagate(0)
        frame.pack(padx=10, pady=10)
        img_path = 'img/completed the game.jpg'
        w, h = 400, 250
        img = ImageTk.PhotoImage(Image.open(img_path).resize((w, h), Image.ANTIALIAS))
        self.make_label(frame, 0, 0, w, h, img)

    def make_label(self, top, x, y, w, h, img, *args, **kwargs):
        label = ttk.Label(top, image=img, *args, **kwargs)
        label.image = img
        label.place(x=x, y=y, width=w, height=h)
        return label


# Create the GUI
root = tk.Tk()
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

game_gui = GuessNameGameGUI(root)
root.mainloop()
