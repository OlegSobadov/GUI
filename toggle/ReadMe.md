# Longest Substring Without Repeating Characters App

Table of Contents

- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Features](#features)
- [Example](#example)
- [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Substring App is a graphical user interface (GUI) application that generates random words and finds the maximum length of a substring without repeating characters in each generated word. The application is built using the Python programming language and the tkinter library.
## Problem Statement

Given a randomly generated word, the Substring App aims to find the length of the longest substring without repeating characters.
## Example

````vbnet
Generated Word: "abcabcbb"
Maximum Substring Length: 3
Explanation: The longest substring without repeating characters is "abc" with a length of 3.
````

````vbnet
Generated Word: "bbbbb"
Maximum Substring Length: 1
Explanation: The longest substring without repeating characters is "b" with a length of 1.
````

````vbnet
Generated Word: "pwwkew"
Maximum Substring Length: 3
Explanation: The longest substring without repeating characters is "wke" with a length of 3.
````


## Features
* Generates random words of varying lengths.
* Displays words as checkbuttons in a grid layout.
* Allows users to toggle between words.
* Analyzes the selected word to find the length of the longest substring without repeating characters.
* Updates the GUI to display the selected word and its corresponding maximum substring length.
    
## Installation

1. Clone the repository:
    ````bash
    git clone https://github.com/OlegSobadov/toggle-app.git
    ````


2. Change to the project directory:
    ````arduino
    cd word-app
    ````
3. Install the required dependencies:
    ````css
    pip install -r requirements.txt
    ````

## Usage

1. Run the application:

    ````arduino
    python word_app.py
    ````
2. The Longest Substring Without Repeating Characters app GUI will open, displaying a grid of checkbuttons representing random words.

3. Toggle between the checkbuttons to select a word.

4. The selected word and the length of the longest substring without repeating characters will be displayed.

## Documentation

For detailed documentation on the code and its functionality, please refer to the [docstring](#) file.

## Contributing

Contributions are welcome! If you have any ideas, improvements, or issues, please create a [new issue](#) or submit a pull request.

## License

This project is licensed under the [MIT License](#).