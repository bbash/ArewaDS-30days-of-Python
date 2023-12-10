"""_
    EXERCISES: Day 16
"""
from datetime import datetime

# Question 1:Get the current day, month, year, hour, minute and 
# timestamp from datetime module
current = datetime.now()
current_day = current.day
current_month = current.month
current_year = current.year
current_hour = current.hour
current_minute = current.minute
current_timestamp = current.timestamp()

print(current_year, current_month, current_day, current_hour, current_minute, current_timestamp)

# Question 2: Format the current date using this format: 
# "%m/%d/%Y, %H:%M:%S")
formatted_current_Date = current.strftime("%m/%d/%Y, %H:%M:%S")
print(formatted_current_Date)

# Question 3: Today is 5 December, 2019. Change this 
# time string to time.
today = datetime(year=2019, month = 12, day = 5)
print(today)

# Question 4: Calculate the time difference between now and new year.
new_year = datetime(year=2024, month=1, day=1, minute=0, second=0)
diff = new_year - current
print(f"The time difference between now and new year is: {diff}")

# Question 5: Calculate the time difference between 1 January 1970 and now.
past_year = datetime(year=1970, month=1, day=1)
diff = current - past_year
print(f"The time difference betwween now and 1970 is: {diff}")

# Question 6: Think, what can you use the datetime module for? Examples:
    # Time series analysis
    # To get a timestamp of any activities in an application
    # Adding posts on a blog