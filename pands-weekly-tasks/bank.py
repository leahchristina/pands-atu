# bank.py
## Weekly Task 02 
## This sums two cent monetary amounts inputted by the user, adds them, stores the total as an integer and prints out the answer in human format. 
## Author: Leah Curran

# 1. Read amount 1 (cents) and convert to integer
amount1 = int(input("Enter the first amount in cents: "))

# 2. Read the second amount (in cents) and convert to integer
amount2 = int(input("Enter the second amount in cents: "))

# 3. Add them
total_cents = amount1 + amount2

# 4. Convert cents into €#.## format
euros = total_cents // 100 # whole euros
cents = total_cents % 100 #leftover cents

# 5. Print formatting
print(f"Total: €{euros}.{cents:02d}") # formatted to ensure padding with zeros occurs when necessary