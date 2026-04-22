# accounts.py
## Weekly Task 03
## This program masks a 10-digit account number so only the last 4 digits show.
## Author: Leah Curran

account = input("Enter your 10-digit account number: ")

# Return error message if less than 10 digits are entered or non-integer entered
# For the extra task, I'm assuming that we do not want more than 10 digits to be entered due to the 10 character string. So rather than making the program cope with an account number of any length, I am limiting the amount that can be inputted.
while len(account) != 10 or not account.isdigit():
    print("Invalid. Please enter exactly 10 digits.")
    account = input("Enter your 10-digit account number: ")
# Ensuring the prompt is asked again if required (Forgot this originally and ended up getting stuck)


# Mask the first 6 digits only (slicing)
masked = "X" * 6 + account[6:]

print("Account Number (Masked)", masked)