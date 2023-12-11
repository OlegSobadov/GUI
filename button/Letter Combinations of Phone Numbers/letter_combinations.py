import tkinter as tk
from tkinter import ttk
from itertools import product

class PhoneKeypadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Phone Keypad Word Combinations")

        # Dictionary to store selected letters for each button
        self.selected_letters = {}

        # Create a style for the buttons
        style = ttk.Style()
        style.configure("Calculator.TButton", font=('Helvetica', 14), padding=5)

        # Create buttons for digits 2 to 9 with a calculator-style appearance
        for digit in range(2, 10):
            button = ttk.Button(root, text=f"{digit}", style="Calculator.TButton",
                                command=lambda d=digit: self.toggle_button(d))
            button.grid(row=(digit - 2) // 3, column=(digit - 2) % 3, sticky="nsew", padx=5, pady=5)

        # Set row and column weights to make buttons expand equally
        for i in range(3):
            root.grid_columnconfigure(i, weight=1)
            root.grid_rowconfigure(i, weight=1)

        # Result label
        self.result_label = tk.Label(root, text="Result: ")
        self.result_label.grid(row=3, column=0, columnspan=3, pady=10)

        # Generate Words button
        self.generate_button = ttk.Button(root, text="Generate Words", style="Calculator.TButton",
                                          command=self.generate_words)
        self.generate_button.grid(row=4, column=0, columnspan=3, pady=10)

    def toggle_button(self, digit):
        # Toggle the button's state (selected or not selected)
        if digit not in self.selected_letters:
            self.selected_letters[digit] = []
        else:
            del self.selected_letters[digit]

    def generate_words(self):
        # Get the digits for which buttons are clicked
        selected_digits = list(self.selected_letters.keys())

        if selected_digits:
            result = self.letter_combinations(selected_digits)
            self.result_label.config(text=f"Result: {result}")
        else:
            self.result_label.config(text="Please select at least one digit.")

        # Reset selected letters after generating words
        self.selected_letters = {}

    def letter_combinations(self, selected_digits):
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # Generate all possible combinations of selected letters
        letters_list = [self.selected_letters[digit] or digit_map[str(digit)] for digit in selected_digits]
        combinations = [''.join(combination) for combination in product(*letters_list)]

        return combinations

if __name__ == "__main__":
    root = tk.Tk()
    app = PhoneKeypadApp(root)
    root.mainloop()
