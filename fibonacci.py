#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
def get_positive_input():
  while True:
    user_input = input()
    if user_inpur.isdigit() and int(user_input) > 0:
      return int(user_input)
    else:
      print("Please enter a positive integer.")

def fibonacci_sequence(n):
  a, b = 0,1
  sequence = []
  for _ in range(n):
    sequence.append(str(a))
    a, b = b, a + b
  return " ".join(sequence)

def main():
  n = get_positive_integer()
  print(fibanacci_sequence(n))

if __name__ == "--main--":
  main()
