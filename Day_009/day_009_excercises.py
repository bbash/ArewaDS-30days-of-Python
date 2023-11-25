"""
    Day 9 of 30 Days of Python Exercise
    @ Abubakar
"""
"""
    Excerise Level 1
"""

# Question 1: Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

age = int(input("Enter your age: "))
print(f"You are old enough to drive") if age >= 18  else print(f"You need {18 - age} more years to learn to drive.")
print()
# Question 2: Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

my_age = 25
your_age = int(input("Enter your age: "))
if my_age > your_age:
    age_diff = my_age - your_age
    print(f"I am {my_age - your_age} year younger than you.") if age_diff == 1 else print(f"I am {my_age - your_age} years younger than you.")
else:
    age_diff = your_age - my_age
    print(f"You are {your_age - my_age} year years older than me.") if age_diff == 1 else print(f"You are {your_age - my_age} years years older than me.")

# Question 3: Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

if first == second:
    print(f"The numbers are the same.")
elif first > second:
    print(f"The first number is greater than the first number")
else:
    print(f"The second number is greater than the first number.")

"""
    Excerise Level 2
"""
"""
   Question 1: Write a code which gives grade to students according to theirs scores:
   80-100, A
    70-79, B
    60-69, C
    50-59, D
    0-49, F
"""
score = int(input("Enter your score: "))
if score >= 80:
    print("A")
elif score >= 70:
    print("B")
elif score >= 60:
    print("C")
elif score >= 50:
    print("D")
else:
    print("F")


# Question 2: Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
autum = ['September', 'October', 'November']
winter = ['December', 'January', 'February']
spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']

sesson_name = input("Enter month name: ")
if sesson_name in autum:
    print('The sesson is Autum')
elif sesson_name in winter:
    print("The sesson is winter")
elif sesson_name in spring:
    print("The sesson is spring")
elif sesson_name in summer:
    print("The sesson is summer")
else:
    print("No month like that")


# Qustion 3: The following list contains some fruits
fruits = ['banana', 'orange', 'mango', 'lemon']

"""
    Level 3
"""
# Here we have a person dictionary. Feel free to modify it!
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if "skills" in person.keys():
    middle_skill = int(len(person["skills"])/2)
    print(person["skills"][middle_skill])
    
#* Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
print("Yes Python is present") if "skills" in person.keys() and "Python" in person["skills"] else print("Not present")
   
#* If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
frontend_developer = ['JavaScript', 'React']
backend_developer = ['Node', 'Python', 'MongoDB']
fullstack_developer = ['React','Node','MongoDB']


#If the person is married and if he lives in Finland, print the information in the following format:
if person['is_marred'] == True and person['country'] == 'Finland':
    print(f"{person['last_name']} {person['first_name']} lives in {person['country']}. He is married.")