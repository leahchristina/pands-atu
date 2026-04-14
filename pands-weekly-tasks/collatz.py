# collatz.py
## This program prints the Collatz sequence from a positive integer chosen by the user.
## Author: Leah Curran

# 1. Ask the user for input
inputted_integer = int(input("Enter a positive integer: ")) # converted string input to integer

# 2. Check the input is positive (show error when negative or zero is entered)
while inputted_integer <= 0:
    print("Please enter a number greater than 0.")
    inputted_integer = int(input("Enter a positive integer: "))
# Prompt re-entry

# 3. Using a while loop to repeat steps until the number is 1
while inputted_integer !=1:
    print(inputted_integer) #Show current value

# 4. Apply Collatz rules
    if inputted_integer % 2 == 0: #is even
     inputted_integer = inputted_integer // 2 
    else:
     inputted_integer = 3 * inputted_integer + 1 # odd rule
# I learned how important the indentation is here when my program returned infinite integers.

# 5. When the loop ends, n must be 1
print(inputted_integer)