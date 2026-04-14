# es.py
# # This program outputs the number of e's in a txt file provided on the command line
## Author: Leah Curran

import sys

# 1. Check that a filename was provided on the command line
if len(sys.argv) < 2:
    print("Error: No filename provided.")
    print("Usage: python es.py <filename>")
    sys.exit(1)

# 2. Get the filename from the command line arguments
filename = sys.argv[1]

try:
    # 3. Open the file and read its contents
    with open(filename, "r", encoding="utf-8", errors="ignore") as file:
        text = file.read()

    # 4. Count the number of lowercase 'e' characters
    count = text.count("e")

    # 5. Output the result
    print(count)

except FileNotFoundError:
    print(f"Error: File '{filename}' does not exist.")

except IsADirectoryError:
    print(f"Error: '{filename}' is not a file.")