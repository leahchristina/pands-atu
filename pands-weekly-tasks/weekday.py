# weekday.py
## This program outputs whether or not the current day is a weekday.
## I'm using this import & strftime method from w3 schools [1]: https://www.w3schools.com/python/python_datetime.asp
# Author: Leah Curran

# 1. Import the datetime module
import datetime

# 2. Get today's date from my machine
today = datetime.date.today()

# 3. Weekday() assigns a number - Monday=0, Tuesday=1, Saturday=5... [1]
day_number = int(today.strftime("%w")) #convert to integer

# 4. If it's Sunday (0) or Saturday (6), it's the weekend, else it's a weekday
if day_number == 0 or day_number ==6:
    print("Stay in bed, it's the weekend!")
else:
    print("Get to work, it's a weekday.")