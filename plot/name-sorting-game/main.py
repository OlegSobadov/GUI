import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from random import choice


def generator_names(size, desired_letters):
    """
    Generate names with modified occurrence of letters.

    Args:
        size (int): The number of names to generate.
        desired_letters (list): List of letters with desired higher occurrence.

    Returns:
        list: Generated names.
    """
    names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "George", "Alex", "Eleanor"]
    alphabet = [chr(n).lower() for n in range(ord('A'), ord('Z') + 1)]
    
    # desired_letters = ['a', 'z', 'b', 'g']
    other_letters = [letter for letter in alphabet if letter not in desired_letters]
    
    generated_names = []
    
    while len(generated_names) < size:
        if len(generated_names) % 4 == 0: # 25% of all letters of alphabet
                                        # approximately 25% of all letters of the alphabet
            letter = choice(desired_letters)
        else:
            letter = choice(other_letters)
        name = f"{letter}{choice(names)}"
        generated_names.append(name)
    
    generated_names.sort()
    
    return generated_names


def create_matrix(names, alphabet):
    """
    Create a matrix of names sorted by the first letter.

    Args:
        names (list): List of names.
        alphabet (list): List of letters in the alphabet.

    Returns:
        list: Name matrix sorted by the first letter.
    """
    alphabet_mapping = {n: idx for idx, n in enumerate(alphabet)}
    m = [[] for _ in range(len(alphabet))]

    for n in names:
        first_letter = n[0].lower()
        if first_letter in alphabet_mapping:
            col_idx = alphabet_mapping[first_letter]
            m[col_idx].append(n)


    matrix = list(filter(lambda n: n, m))

    return matrix


def plot_name_distribution(alphabet, matrix):
    """
    Plot the name distribution by the first letter.

    Args:
        alphabet (list): List of letters in the alphabet.
        matrix (list): Name matrix sorted by the first letter.

    Returns:
        tuple: Figure and axes objects for the plot.
    """
    letters = alphabet.copy()
    counts = [len(names) for names in matrix]

    fig, ax = plt.subplots()
    ax.bar(letters, counts)
    ax.set_xlabel('Letters')
    ax.set_ylabel('Count')
    ax.set_title('Name Distribution by First Letter')
    plt.close(fig)

    return fig, ax


def update_plot():
    """
    Update the plot based on the filter letter and desired letters.
    """
    global size, alphabet, fig, ax, canvas, alphabet_mapping

    filter_letter = validate_filter_letter(filter_entry.get().lower())
    print(f'filter letter: {filter_letter}')
    
    letters = alphabet.copy()
    desired_letter = list(desired_entry.get()) # 'abc'
    names = generator_names(size=size, desired_letters=desired_letter)
    m = create_matrix(names=names, alphabet=alphabet)

    if filter_letter in letters and desired_letter:
        col_index = alphabet_mapping[filter_letter]
        filtered_names = m[col_index]

        ax.clear()
        ax.bar(letters, [len(names) for names in m])
        ax.bar(filter_letter, len(filtered_names), color='red')
        ax.set_xlabel('Letters')
        ax.set_ylabel('Count')
        ax.set_title('Name Distribution by First Letter')

        canvas.draw()

        messagebox.showinfo("Filtered Names", "\n".join(filtered_names))
    else:
        messagebox.showerror("Error", "Invalid filter letter!")


def get_random_name():
    """
    Get a random name from the generated names.
    """
    random_name = choice(names)
    messagebox.showinfo("Random Name", random_name)


# utils
def validate_filter_letter(choisen_letter: str):
    if choisen_letter.isdigit() or choisen_letter[0].isdigit():
        raise ValueError('only alphabet letter')
    elif len(choisen_letter) > 1:
        choisen_letter = choisen_letter[0]

    filter_letter = choisen_letter.lower()

    return filter_letter

# initialization
size = 10 ** 4
desired_letters = 'v d e'.split()
names = generator_names(size, desired_letters=desired_letters)
alphabet = [chr(n).lower() for n in range(ord('a'), ord('z') + 1)]
m = create_matrix(names=names, alphabet=alphabet)

# create the gui
root = tk.Tk()
root.title("Name Sorting and Filtering Game")

filter_label = tk.Label(root, text="Filter Letter:")
filter_label.pack()

filter_entry = tk.Entry(root)
filter_entry.pack()

desired_label = tk.Label(root, text='Desired Letter:')
desired_label.pack()

# new_entry = tk.Entry(root)
# new_entry.pack()
desired_entry = tk.Entry(root)
desired_entry.pack()

# visualisation
# fig, ax = plot_name_distribution(letters, m)
fig, ax = plot_name_distribution(alphabet, m)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

update_button = tk.Button(root, text="Update", command=update_plot)
update_button.pack()

instructions_label = tk.Label(root, text="Enter a letter and click 'Update' to filter names.\n"
                                          "Click 'Random Name' to get a random name.")
instructions_label.pack()

random_name_button = tk.Button(root, text="Random Name", command=get_random_name)
random_name_button.pack()

root.mainloop()
