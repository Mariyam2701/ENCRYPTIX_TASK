# ENCRYPTIX_TASK
DOING TASK THAT'S ASSIGNED BY ENCRYPTIX AS PART OF THE PYTHON PROGRAMMING VIRTUAL INTERNSHIP

##
# TASK 1: TO-DO-LIST
This project aims to create a To-Do List application using Python, allowing users to efficiently manage and organize their tasks. The application provides a command-line interface for users to create, update, and track their to-do lists.

## Key Features
- Create and manage to-do lists
- Add new tasks
- Update existing tasks
- Delete tasks
- Display the current to-do list

## Code Overview
## The code is organized into four main functions:
- display_tasks(): Displays the current to-do list
- add_task(): Adds new tasks to the list
- update_task(): Updates existing tasks
- delete_task(): Deletes tasks from the list
The code uses a simple menu-driven interface, where users can choose to view, add, update, or delete tasks. The tasks are stored in a list called tasks, and the code uses indexing to update and delete tasks.

## Key Code Points
- The tasks list stores all the tasks
- The display_tasks() function uses enumeration to display the task number and task name
- The add_task() function uses input to get new tasks and splits them by commas
- The update_task() function uses input to get the task number and new task name
- The delete_task() function uses input to get the task numbers to delete

## Conclusion
This project demonstrates a simple To-Do List application using Python. The code is easy to understand and modify, making it a great starting point for beginners. The application provides a basic but functional interface for managing tasks and can be expanded upon to add more features and functionality.



##
# TASK 2 CALCULATOR
This project is a simple calculator application written in Python, designed to perform basic arithmetic operations. The application provides a command-line interface for users to perform calculations efficiently.

## Key Features
- Addition of two numbers
- Subtraction of two numbers
- Multiplication of two numbers
- Division of two numbers (with error handling for division by zero)
- Continuous operation until the user decides to quit

## Code Overview
The code is structured to repeatedly prompt the user for input and perform calculations based on the selected operation.

- User Input Handling: Prompts users to enter two numbers and choose an arithmetic operation.
- Addition: Adds two numbers and displays the result.
- Subtraction: Subtracts the second number from the first and displays the result.
- Multiplication: Multiplies two numbers and displays the result.
- Division: Divides the first number by the second, with error handling for division by zero.
- Looping Mechanism: Uses a while True loop to continuously prompt the user until they decide to quit by entering 'end'.

## Key Code Points
- User Input: Utilizes input() to gather numbers and the operation choice from the user.
- Error Handling: Includes mechanisms for handling invalid numeric inputs and invalid operation choices.
- Arithmetic Operations: Implements basic arithmetic operations with appropriate prompts and displays for results.

## 
# TASK 3 PASSWORD GENERATOR
This project is a simple password generator application written in Python, designed to create secure passwords based on user-specified criteria. The application provides a command-line interface for users to generate varying lengths and complex passwords.

# Key Features
- Generate passwords of user-specified lengths.
- Choose between low, medium, and high complexity for the password.
- Continuous generation until the user decides to quit.

# Code Overview
- User Input Handling: Prompts users to enter the desired password length and complexity level.
- Password Generation: Creates a password using random ASCII characters, digits, and punctuation based on the chosen complexity.
- Looping Mechanism: Uses a while True loop to continuously prompt the user until they decide to quit by entering 'end'.

# Key Code Points
- User Input: Utilizes input() to gather the password length and complexity from the user.
- Character Sets: Uses the string module to access ASCII letters, digits, and punctuation.
- Random Selection: Implements random.choice() to select characters for the password randomly.
- Loop for Continuation: Continuously generates passwords until the user chooses to stop.
- 

# TASK 4: Rock-Paper-Scissors Game

This is a command-line Rock-Paper-Scissors game built using Python. The game allows users to play against the computer, with the option to play multiple rounds or exit the game.

Key Features

- Play against the computer in a game of Rock-Paper-Scissors
- Choose to play multiple rounds or exit the game
- View the score after each round and at the end of the game

How to Play

1. Run the program and select "Yes" to play or "No" to exit.
2. Choose your move by entering the corresponding number (1 for Rock, 2 for Paper, 3 for Scissor).
3. The computer's move will be generated randomly.
4. The game will display the moves and declare a winner or draw.
5. The score will be updated and displayed after each round.
6. The game will continue for 5 rounds or until you choose to exit.

Code Overview

The code uses a simple menu-driven interface and a while loop to keep the game running. The computer's move is generated using the random module. The game logic is implemented using conditional statements to determine the winner or draw.

Key Code Points

- The game uses a list l to store the possible moves.
- The user's input is validated to ensure a valid move is selected.
- The computer's move is generated using random.choice(l).
- The game logic is implemented using conditional statements to determine the winner or draw.
- The score is updated and displayed after each round.
