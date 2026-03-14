# SIMPLE PASSWORD GENERATOR USING PYTHON :

           Simple-Password-Generator

# DESCRIPTION :

           This is a Random Password Generator built using Python. This program generates a secure random password based on the length provided by the user.

# FEATURES :

           * Generates random passwords.
           * Uses letters, numbers, and symbols.
           * Allows the user to choose the password length.
           * Simple and beginner-friendly command line program. 

# CONCEPT USED : 

           * Random module.
           * Loops.
           * Conditional statements.
           * User input handling.

# HOW TO RUN : 

           * Install Python on your system.
           * Save the file with extension .py (example password.py).
           * Run the code.

# WORKING :

           * import random – This line imports Python's random module which helps generate random characters.
           * letters – Stores all lowercase and uppercase alphabet characters.
           * digits – Stores numbers from 0 to 9.
           * symbols – Stores special characters that can be used in the password.
           * all_chars = letters + digits + symbols – Combines all characters into one variable so the password can include any of them.
           * Now , it prints the title RANDOM PASSWORD GENERATOR.
           * The program asks the user to enter the password length.
           * if (length <= 0) – Checks whether the entered value is valid.
           * for i in range(length) – A loop runs based on the length entered by the user.
           * random.choice(all_chars) – Selects a random character from the available characters.
           * Each random character is added to the password.
           * The password can be mixture of alphabets ( Uppercase or Lowercase ) , digits ( 0 to 9 ) and special characters.
           * Finally, the program displays the generated password.

# AUTHOR :

Sajiyya Fathima N

BE CSE Student | Python Beginner | Learning Programming

Oasis Internship | Easwari Engineering College
