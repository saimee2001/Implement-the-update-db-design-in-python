# Python Functions: Comprehensive Guide

"""
Samira Saimee
ID: C193214
Email: c193214@ugrad.iiuc.ac.bd
"""

# Section 1: Basic Functions
# --------------------------
# Functions are defined using the `def` keyword. They allow you to encapsulate code for reuse.
# Assignments
# -----------
# Assignment 1: Write a function that calculates the factorial of a number and handles any potential errors.
def factorial(n):
    if not isinstance(n, int) or n < 0:
        print("Error: The number must be a non-negative integer.")
        return None
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 10:", factorial(10))

# Congratulations on completing the advanced section on Python functions!
# Review the assignments, try to solve them, and check your understanding of function concepts.
