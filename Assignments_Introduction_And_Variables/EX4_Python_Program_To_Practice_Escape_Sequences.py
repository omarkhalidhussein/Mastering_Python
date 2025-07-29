# ======================================================================================================================
# Name        : EX4_Python_Program_To_Practice_Escape_Sequences.py
# Author      : Omar Khalid
# Created on  : July 29, 2025
# Description : Python Programming >> Assignment 1 Python - Introduction And Variables >> EX4 Practice escape sequences
# ======================================================================================================================



# Backspace(removes the character before it - here it removes 'o')
print("Hello\bWorld")  # Output: HellWorld

# Escape newline using backslash for line continuation(prints as one line)
print("Hello \
I Love \
Python")  # Output: Hello I Love Python

# Escape backslash(prints a single backslash)
print("I Love Back Slash \\")  # Output: I Love Back Slash \

# Escape single quote inside single - quoted string
print('I Love Single Quote \'Test\' ')  # Output: I Love Single Quote 'Test'

# Escape double quotes inside double - quoted string
print("I Love Double Quotes \"Test\" ")  # Output: I Love Double Quotes "Test"

# New line(line feed)
print("Hello World\nSecond Line")
# Output:
# Hello World
# Second Line

# Carriage return (returns to the beginning of the line and overwrites)
print("123456\rAbcde")  # Output: Abcde6

# Horizontal tab(adds a tab space)
print("Hello\tPython")  # Output: Hello    Python

# Print characters using hexadecimal ASCII values(4F = 'O', 73 = 's')
print("\x4F\x73")  # Output: Os
