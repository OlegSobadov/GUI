
## Table of Contents:

- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Problem Explanation](#problem-Explanation)
- [Intuition](#intuition)
- [Implementation](#implementation)
- [Complexity Analysis](#complexity-Analysis)
- [Conclusion](#conclusion)



## Introduction
Classic algorithm of generating all possible combinations, and it can be solved using recursion. Each digit corresponds to a set of letters, and you want to find all possible combinations of these letters.

## Problem Statement
Given a string containing digits from 2–9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

<img src="img/Phone Keypad Word Combinations.png" alt="Phone Keypad Word Combinations">


## Implementation

- Buttons for digits 2 to 9 are created, and clicking a button toggles its state (selected or not selected).
- The `selected_letters` dictionary keeps track of the selected letters for each button.
- The `toggle_button` method is called when a button is clicked, updating the selected letters for that button.
- The `generate_words` method generates combinations based on the selected digits and displays the result in the label.

-  the `ttk` module for creating themed widgets, and it configures a style named "Calculator.TButton" with a specific font and padding. The ttk.Button widgets in the calculator grid use this style for a cleaner appearance.


