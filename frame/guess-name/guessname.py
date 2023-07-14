import tkinter as tk
from tkinter import ttk
from random import choice


class GuessName:
    """
    A class representing the Guess Name game GUI.

    Attributes:
        master (Tk): The root Tkinter window.
        alphabet (List[str]): The list of alphabet letters.
        names (List[str]): The list of generated names.

    Methods:
        __init__(master): Initializes the GuessName instance.
        build_gui(): Builds the GUI for the game.
        create_labels_entries_buttons(): Creates labels, entries, and buttons in the GUI.
        generate_alphabet(): Generates the list of alphabet letters.
        generate_names(): Generates a list of random names.
        show_all_names(): Displays all the generated names.
        validate_and_show_names(): Validates input and shows all the generated names.
        create_top_window(): Creates a new top-level window to display all names.
        get_num_columns(): Retrieves the number of columns from the entry field.
        center_frame(): Centers the frame within the top-level window.
        run_game(): Runs the main event loop for the game.

    """

    def __init__(self, master):
        """
        Initializes the GuessName instance.

        Args:
            master (Tk): The root Tkinter window.

        """
        self.master = master
        self.alphabet = []
        self.names = []
        self.build_gui()

    def build_gui(self):
        """
        Builds the GUI for the game.

        """
        self.master.geometry("250x100")
        self.create_labels_entries_buttons()
        self.generate_alphabet()
        self.generate_names()

    def create_labels_entries_buttons(self):
        """
        Creates labels, entries, and buttons in the GUI.

        """
        self.label = tk.Label(self.master, text='Guess Name')
        self.label.pack()

        self.entry_label = tk.Label(self.master, text='Choice Columns:')
        self.entry_label.pack()

        self.entry_column = tk.Entry(self.master)
        self.entry_column.pack()

        self.button = tk.Button(self.master, text='Show All Names', command=self.show_all_names)
        self.button.pack()

    def generate_alphabet(self):
        """
        Generates the list of alphabet letters.

        """
        self.alphabet = [chr(n).lower() for n in range(ord('A'), ord('Z') + 1)]

    def generate_names(self):
        """
        Generates a list of random names.

        """
        self.names = [choice(self.alphabet) + n + choice(self.alphabet) for n in self.alphabet]

    def show_all_names(self):
        """
        Displays all the generated names.

        """
        self.validate_and_show_names()

    def validate_and_show_names(self):
        """
        Validates input and shows all the generated names.

        """
        if not hasattr(self, "top") or not self.top.winfo_exists():
            self.create_top_window()
            num_names = len(self.names)
            num_columns = self.get_num_columns()

            num_rows = (num_names + num_columns - 1) // num_columns

            for idx, name in enumerate(self.names):
                row = idx % num_rows
                col = idx // num_rows

                label = ttk.Label(self.frame, text=name, style="NameLabel.TLabel")
                label.grid(row=row, column=col, sticky="w")

            self.center_frame()

    def create_top_window(self):
        """
        Creates a new top-level window to display all names.

        """
        self.top = tk.Toplevel(self.master)
        self.top.title('All Names')
        self.top.geometry('+%d+%d' % (self.master.winfo_rootx() + self.master.winfo_width(),
                                       self.master.winfo_rooty()))
        self.frame = tk.Frame(self.top)
        self.frame.pack(padx=10, pady=10)

        style = ttk.Style()
        style.configure("NameLabel.TLabel", font=("Arial", 14, "bold"))

    def get_num_columns(self):
        """
        Retrieves the number of columns from the entry field.

        Returns:
            int: The number of columns.

        """
        entry_column = self.entry_column.get()
        if not entry_column:
            return 3
        try:
            num_columns = int(entry_column)
        except ValueError:
            num_columns = 3
        if num_columns > 10:
            num_columns = 3
        return num_columns

    def center_frame(self):
        """
        Centers the frame within the top-level window.

        """
        self.frame.update_idletasks()
        self.frame.place(relx=0.5, rely=0.8, anchor="center")

    def run_game(self):
        """
        Runs the main event loop for the game.

        """
        self.master.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    game = GuessName(root)
    game.run_game()
