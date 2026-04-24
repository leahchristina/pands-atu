# es.py
## This program outputs the number of e's in a txt file provided on the command line
## Author: Leah Curran
## Program handles the following errors: no filename provided, filename does not exist, the file cannot be read.
## Assumption - only lowercase e's are counted. 

import sys # opening access to command-line arguments

# 1. Check that a filename was provided on the command line & only one argument was given
if len(sys.argv) < 2: # if sys.argv > 2 then there is more than one argument
    print("Error: No filename provided.")
    print("Usage: python es.py <filename>")
    sys.exit(1) # Stop the program if this check fails (no continuous loop)

# 2. Get the filename from the command line arguments
filename = sys.argv[1] # store the file name supplied by the user

try:
    # 3. Open the file and read its contents ("r = read mode")
    with open(filename, "r", encoding="utf-8", errors="ignore") as file: # ensuring the file is read assuming it uses utf-8 rules. adding ignore to avoid unicode decode errors.
        text = file.read()

    # 4. Count the number of lowercase 'e' characters
    count = text.count("e") # note: possible option/enhancement? count both upper & lowercase: e_count = contents.lower().count('e')

    # 5. Output the result
    print(count)

except FileNotFoundError:
    print(f"Error: File '{filename}' does not exist.")

except IsADirectoryError:
    print(f"Error: '{filename}' is not a file.")

## References: 
## For my testing file - I used download of Little Women from Project Gutenberg: https://www.gutenberg.org/ebooks/37106
## For learning how to do command line arguments I used Real Python https://realpython.com/python-command-line-arguments/ & Python Software Foundation https://docs.python.org/3/library/sys.html#sys.argv