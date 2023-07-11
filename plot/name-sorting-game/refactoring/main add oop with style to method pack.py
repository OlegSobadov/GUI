import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from random import choice
from tkinter import messagebox


class GuessNameGameGUI:
    """
    Guess Name Game GUI

    This class represents the graphical user interface for the Guess Name Game.
    It allows users to guess names and visualizes the distribution of names by their starting letters.

    Attributes:
        master (tkinter.Tk): The root Tkinter window.
        alphabet (List[str]): A list of lowercase alphabet letters.
        alphabet_mapping (Dict[str, int]): A mapping of alphabet letters to their corresponding indices.
        names (List[str]): A list of generated names.
        matrix (List[List[str]]): A matrix representation of names grouped by their starting letters.
        count_names (List[int]): The count of names for each starting letter.
        letters (List[str]): A list of unique starting letters.
        name (str): The current name for guessing.

    Methods:
        create_gui(): Creates and configures the GUI elements.
        generate_names(): Generates a list of random names.
        create_matrix(names: List[str]): Creates a matrix representation of names grouped by their starting letters.
        extract_letter(): Extracts the unique starting letters from the matrix.
        get_x_y_to_plot(): Retrieves the x and y data for plotting the bar chart.
        draw_bar_plot(): Draws and updates the bar chart visualization.
        _count_names(matrix: List[List[str]]): Counts the number of names for each starting letter.
        validate_given_name(name: str) -> str: Validates a given name and returns the lowercase version.
        is_name_in_matrix(target: str, filter: Optional[bool]) -> bool: Checks if a name is present in the matrix.
        update_guesses(): Updates the displayed guesses and the guess count.
        update_plot(): Updates the plot and checks if the entered name is in the matrix.
    """

    def __init__(self, master):
        """
        Initialize the GuessNameGameGUI.

        Args:
            master (tkinter.Tk): The root Tkinter window.
        """
        self.master = master
        self.alphabet = [chr(n).lower() for n in range(ord('A'), ord('Z') + 1)]
        self.alphabet_mapping = {v: idx for idx, v in enumerate(self.alphabet)}
        self.names = []
        self.matrix = []
        self.count_names = []
        self.letters = []
        self.name = ""

        self.create_gui()

    def create_gui(self):
        """
        Create and configure the GUI elements.
        """
        # self.master.geometry('400x400')
        self.master.title('Guess My Name')

        # Label for "Guess a Name"
        self.master.config(bg='black')
        self.label_name = tk.Label(
            self.master, text='Guess a Name', font=('Courier New', 20), fg='white', bg='black'
        )
        self.label_name.pack(pady=10)

        # Entry for entering the name
        self.entry_name = tk.Entry(
            self.master, font=('Courier New', 16), fg='white', bg='black', insertbackground='white'
        )
        self.entry_name.pack(pady=5)

        # Button to update the plot and check the name
        self.b_update = tk.Button(
            self.master,
            text='Update',
            command=self.update_plot,
            font=('Courier New', 16),
            fg='white',
            bg='black',
            activeforeground='white',
            activebackground='dark green',
            relief=tk.FLAT,
            highlightthickness=0
        )
        self.b_update.pack(pady=5)

        # Figure and canvas for the plot
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.ax.set_facecolor('black')
        self.ax.tick_params(axis='x', colors='black')
        self.ax.tick_params(axis='y', colors='white')
        self.ax.spines['bottom'].set_color('white')
        self.ax.spines['top'].set_color('white')
        self.ax.spines['right'].set_color('white')
        self.ax.spines['left'].set_color('white')

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

        # Labels for displaying guesses and guess count
        self.guesses_label = tk.Label(
            self.master,
            text="Your guesses:",
            font=('Courier New', 12),
            fg='white',
            bg='black'
        )
        self.guesses_label.pack(anchor='w', padx=10, pady=5)

        self.guess_count_label = tk.Label(
            self.master,
            text=0,
            font=('Courier New', 12),
            fg='white',
            bg='black'
        )
        self.guess_count_label.pack(anchor='e', padx=10, pady=5)

        self.generate_names()
        self.create_matrix(self.names)
        self.update_guesses()
        self.draw_bar_plot()

    def generate_names(self):
        """
        Generate a list of random names.
        """
        self.names = [choice(self.alphabet) + n + choice(self.alphabet) for n in self.alphabet]
        self.names.sort()

    def create_matrix(self, names):
        """
        Create a matrix representation of names grouped by their starting letters.

        Args:
            names (List[str]): A list of names.
        """
        self.matrix = [[] for _ in range(len(self.alphabet))]
        for idx, name in enumerate(names):
            first_letter = name[0].lower()
            col_idx = self.alphabet_mapping[first_letter]
            self.matrix[col_idx].append(name)
        self.matrix = list(filter(lambda n: n, self.matrix))

    def extract_letter(self):
        """
        Extract the unique starting letters from the matrix.
        """
        self.letters = []
        for sublist in self.matrix:
            if sublist:
                first_letter = sublist[0][0]
                self.letters.append(first_letter)

    def get_x_y_to_plot(self):
        """
        Retrieve the x and y data for plotting the bar chart.

        Returns:
            Tuple[np.ndarray, np.ndarray]: The x and y data for plotting.
        """
        self.extract_letter()
        x = np.arange(len(self.letters))
        y = self._count_names(self.matrix)
        return x, y

    def draw_bar_plot(self):
        """
        Draw and update the bar chart visualization.
        """
        self.ax.clear()
        x, y = self.get_x_y_to_plot()
        self.ax.bar(x, y, color='cyan')
        self.ax.set_xticks(x)
        self.ax.set_xticklabels(self.letters, fontdict={'fontsize': 12, 'fontweight': 'bold'})
        self.ax.set_title('Filtering and Sorting Names', fontdict={'fontsize': 18, 'fontweight': 'bold'}, color='white')
        self.ax.set_xlabel('Letters', fontdict={'fontsize': 12, 'fontweight': 'bold'}, color='black')
        self.ax.set_ylabel('Count', fontdict={'fontsize': 12, 'fontweight': 'bold'}, color='black')
        self.ax.set_facecolor('black')
        self.canvas.draw()

    def _count_names(self, matrix):
        """
        Count the number of names for each starting letter.

        Args:
            matrix (List[List[str]]): The matrix representation of names.

        Returns:
            List[int]: The count of names for each starting letter.
        """
        output = [len(names) for names in matrix]
        return output

    def validate_given_name(self, name):
        """
        Validate a given name and return the lowercase version.

        Args:
            name (str): The name to be validated.

        Returns:
            str: The lowercase version of the validated name.

        Raises:
            ValueError: If the name contains non-alphabet characters or starts with a digit.
        """
        if name.isdigit() or name[0].isdigit():
            raise ValueError('Only alphabet letters are allowed')
        elif len(name) >= 3:
            name = name[:3].lower()
        return name

    def is_name_in_matrix(self, target, filter=None):
        """
        Check if a name is present in the matrix.

        Args:
            target (str): The name to be checked.
            filter (Optional[bool]): Whether to filter empty sublists in the matrix.

        Returns:
            bool: True if the name is found, False otherwise.
        """
        if not filter:
            output = any(target in names for names in self.matrix)
        elif filter:
            output = bool(list(filter(lambda names: target in names, self.matrix)))
        else:
            return False
        return output

    def update_guesses(self):
        """
        Update the displayed guesses and the guess count.
        """
        guesses = self.guesses_label.cget("text")
        self.guesses_label.config(text=guesses, fg='white')

        guess_count = str(len(guesses.split("\n")))
        self.guess_count_label.config(text=guess_count, fg='white')

    def update_plot(self):
        """
        Update the plot and check if the entered name is in the matrix.
        """
        name = self.entry_name.get()
        if name:
            name = self.validate_given_name(name)
        self.generate_names()
        self.create_matrix(self.names)
        self.draw_bar_plot()
        if name and self.is_name_in_matrix(name):
            messagebox.showinfo("Name", name)
        elif not name:
            ...
        else:
            messagebox.showerror('Error', 'Invalid name!')


# Create the GUI
root = tk.Tk()
game_gui = GuessNameGameGUI(root)
root.mainloop()
