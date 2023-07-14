## `Show Names in the Frame` based on the Game GuessName

GuessName is a game where players need to guess names based on provided clues. This repository provides a graphical user interface (GUI) for playing the game.

### Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Code Example](#code-example) # `formula`
- [Contributing](#contributing)
- [License](#license)

### Installation

To install and run GuessName, follow these steps:

1. Clone this repository to your local machine.
2. Ensure you have Python 3.x installed.
3. Install the required dependencies using the following command:

```
pip install -r requirements.txt
```


### Usage

To play GuessName, run the following command:
```
python guessname.py
```


### Features

- Graphical user interface (GUI) for an interactive gaming experience.
- Randomly generated names for a unique gameplay session.
- Clues and hints to assist players in guessing the names.
- Score tracking to keep a record of the player's performance.

### Code Example

## Formulas
GuessName also includes the following formulas for specific functionalities:

The following example demonstrates how to use `hasattr()` in the context of GuessName:

- ### Using hasattr() to Apply Button Multiple Times
    In the GuessName game, the "Show All Names" button allows you to display all the names available. However, `clicking the button multiple times` should `not open new windows for each click`. The hasattr() function is used to check if the button's attribute top exists or if the top-level window is already open. If it exists, the previous window is reused instead of creating a new one.

    ```python
    def show_all_names(self):
        # Check if an object has a certain attribute
        if not hasattr(self, "top") or not self.top.winfo_exists():
            self.top = tk.Toplevel(self.master)
            # self.create_top_window()
            # Rest of the code...

    ```

- ### Column Numbers Formula:
    The formula calculates the number of columns to display items from the data:
    ```python
     def validate_and_show_names(self):
        # code upper()
        num_names = len(self.names)
        num_columns = self.get_num_columns()

        num_rows = (num_names + num_columns - 1) // num_columns

        for idx, name in enumerate(self.names):

            # formula
            row = idx % num_rows
            col = idx // num_rows

            label = ttk.Label(self.frame, text=name, style="NameLabel.TLabel")
            label.grid(row=row, column=col, sticky="w")
        # code below()
        # Rest of the code...
    ```


- ### Frame Windows Position Formula
    The formula positions the frame windows to display the frame windows within the top-level `window on the right corner`, the place() method is used. Additionally, you can set the geometry of the top-level window `using the formula`:

    ```python
    self.top.geometry('+%d+%d' % (self.master.winfo_rootx() + self.master.winfo_width(), self.master.winfo_rooty()))
    ```

    This formula sets the geometry of the top-level window by calculating the position relative to the master window's right corner. It ensures that the top-level window is positioned adjacent to the master window, aligned with the right edge.

    By using this formula, the frame windows will be displayed on the right corner of the top-level window, providing a visually appealing layout for the GuessName game.

## Contributing
Contributions to GuessName are welcome! Please follow these guidelines when contributing:

- Fork the repository.
- Create a new branch.
- Make your changes and ensure the code is well-documented.
- Test the changes thoroughly.
- Open a pull request and describe the changes you've made.

## License
This project is licensed under the MIT License. See the [LICENSE](#) file for more details.