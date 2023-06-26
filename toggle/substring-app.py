# add docstring
# add images to label

import tkinter as tk
from tkinter import messagebox
from random import randint
from PIL import Image, ImageTk


class WordGenerator:
    @staticmethod
    def generate_random_word():
        """
        Generate a random word consisting of lowercase alphabets.

        Returns:
            str: Randomly generated word.
        """
        start_ascii = ord('a')
        end_ascii = ord('z')
        size = randint(6, 10)
        r_word = ""
        for _ in range(size):
            r_n = chr(randint(start_ascii, end_ascii))
            r_word += r_n
        return r_word


class WordAnalyzer:
    @staticmethod
    def get_max_size(word):
        """
        Calculate the length of the longest substring without repeating characters in the given word.

        Args:
            word (str): Input word.

        Returns:
            int: Length of the longest substring without repeating characters.
        """
        max_size = 0
        temp_map = {}
        start = 0
        for end, n in enumerate(word):
            if n in temp_map and temp_map[n] >= start:
                start = temp_map[n] + 1
            temp_map[n] = end
            if end - start + 1 > max_size:
                max_size = end - start + 1
        return max_size


class WordApp:
    def __init__(self, master, size):
        """
        WordApp class represents a tkinter application for word analysis.

        Args:
            master (tkinter.Tk): Root window of the application.
            size (int): Number of words to generate and display.

        Attributes:
            size (int): Number of words to generate and display.
            words (list): List of randomly generated words.
            word_toggles (list): List of toggle variables for checkbuttons.
            word_labels (list): List of labels displaying words.
            master (tkinter.Tk): Root window of the application.
            label_images (list): List to hold PhotoImage objects for labels.
            idx (int): Index to keep track of the current image in label_images.
        """
        self.size = size
        self.words = []
        self.word_toggles = []
        self.word_labels = []
        self.master = master
        self.label_images = []
        self.idx = 1
        self.build_gui()


    def build_gui(self):
        """
        Build the graphical user interface for the WordApp.

        This method creates and configures the necessary GUI elements, such as labels, buttons, and checkbuttons,
        and sets up their respective event handlers.
        """
        self.master.title('Word App')
        self.master.geometry("750x450")
        self.result_label = tk.Label(self.master, text="Result: ", font=('Arial', 14))
        self.result_label.grid(row=0, column=2, padx=10, pady=10, rowspan=self.size, sticky='n')

        self.generate_words()
        
        self.g_button = tk.Button(self.master, text='Toggle Words', command=self.label_words)
        self.g_button.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.create_checkbuttons()
        self.create_labels()

        self.clear_labels_button = tk.Button(self.master, text='Clear Labels', command=self.clear_labels)
        self.clear_labels_button.grid(row=self.size + 1, column=0, columnspan=2, padx=10, pady=10)


    def create_checkbuttons(self):
        """
        Create checkbuttons for each word and associate them with toggle variables.

        This method creates checkbuttons for each word in the words list and associates them with toggle variables.
        The checkbuttons are displayed in a grid layout, with half of them in the first column and the other half
        in the second column.

        Returns:
            list: List of toggle variables for checkbuttons.
        """
        for i in range(self.size):
            toggle_var = tk.BooleanVar()
            toggle_var.set(False)
            toggle = tk.Checkbutton(self.master, text=self.words[i], variable=toggle_var, command=self.toggle_word)
            # toggle.grid(row=1 + i, column=i % 2, padx=1, pady=1, sticky="w")
            if i % self.size // (self.size // 2) == 0:
                toggle.grid(row=1 + i, column=0, padx=5, pady=5, sticky="w")
            else:
                toggle.grid(row=1 + i - (self.size // 2), column=1, padx=5, pady=5, sticky="w")
            self.word_toggles.append(toggle_var)


    def create_labels(self):
        """
        Create labels to display words and configure them with images.

        This method creates labels to display words and configures them with images from the label_images list.
        The labels are displayed in a grid layout, with half of them in the second column and the other half
        in the third column.

        Returns:
            list: List of labels displaying words.
        """
        self.add_images()
        for n in range(self.size):
            label = tk.Label(self.master, text="", width=200, height=35, relief='ridge')
            label.configure(font=('Arial', 8, 'bold'))
            label.configure(bg='#f5f5f5')
            label.configure(fg='black')
            label.configure(borderwidth=2)
            label.configure(image=self.label_images[self.idx], compound='center')
            # label.grid(row=n, column=(n % 2) + 2)

            if n % self.size // (self.size // 2) != 0:
                label.grid(row=n, column=3)
            else:
                label.grid(row=n + (self.size // 2), column=2)
            self.word_labels.append(label)

        self.master.update_idletasks()
        self.label_words()


    def add_images(self):
        """
        Add images to the label_images list and resize them.

        This method adds images to the label_images list and resizes them to a fixed size (200x35 pixels).

        Returns:
            list: List of resized PhotoImage objects for labels.
        """
        image_path = ['img/clear water.jpg', 'img/cloud sky.jpg']
        for path in image_path:
            image = Image.open(path)
            image.resize((200, 35))
            photo = ImageTk.PhotoImage(image)
            
            self.label_images.append(photo)


    def clear_labels(self):
        """
        Clear the labels and reset them to the default image.

        This method clears the labels by resetting their text and image to the default image from the label_images list.
        """
        self.idx = 0
        clear_image = self.label_images[self.idx]
        for label in self.word_labels:
            label.configure(text="")
            label.configure(image=clear_image)

        self.master.update_idletasks()


    def generate_words(self):
        """
        Generate random words and store them in the words list.

        This method generates a random word using the WordGenerator class and stores them in the words list.
        The number of words generated is determined by the size attribute.
        """
        self.words = [WordGenerator.generate_random_word() for _ in range(self.size)]

    def label_words(self):
        """
        Label the words and configure the labels with the default image.

        This method labels the words by updating the text of each label with the corresponding word from the words list.
        The labels are also configured with the default image from the label_images list.
        """
        self.idx = 1
        default_image = self.label_images[self.idx]
        for idx, word in enumerate(self.words):
            label = self.word_labels[idx]
            label.config(text=f"{self.word_toggles[idx]}")
            label.configure(image=default_image)

        self.master.update_idletasks()


    def toggle_word(self):
        """
        Toggle the selected word and update the result label.

        This method toggles the selected word by updating the toggle variables of the checkbuttons.
        It ensures that only one word is selected at a time.
        The method also calls the slice_word method to analyze the selected word and update the result label accordingly.
        """
        selected_word = ""
        for r in range(self.size):
            if self.word_toggles[r].get():
                selected_word = self.words[r]
                for c in range(self.size):
                    if r != c:
                        self.word_toggles[c].set(False)
                break
        self.slice_word(selected_word)

    def slice_word(self, selected_word):
        """
        Analyze the selected word and update the result label.

        This method analyzes the selected word using the WordAnalyzer class.
        It calculates the length of the longest substring without repeating characters in the word.
        The result label is then updated with the selected word and its corresponding maximum substring length.

        Args:
            selected_word (str): Selected word to analyze.
        """
        if selected_word:
            max_size = WordAnalyzer.get_max_size(selected_word)
            self.result_label.config(text=f"{selected_word}: {max_size}")
        else:
            self.result_label.config(text="")

    def run(self):
        """
        Run the WordApp tkinter application.

        This method starts the main event loop of the tkinter application, allowing the user to interact with the GUI.
        """
        self.master.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = WordApp(master=root, size=10)
    app.run()
