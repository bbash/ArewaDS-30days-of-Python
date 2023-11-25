"""
    Day 11 of 30 Days of Python Exercise
    @ Abubakar
"""
"""
    Excerise Level 1
"""
# Question 1: Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1, num2):
    return num1 + num2
print(f'The sum of two numbers; 2 and 4 is {add_two_numbers(2,4)}')

# Question 2: Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(radius):
    return 3.14 * radius * radius
print(f"The area of a circle with 5 radius is {area_of_circle(5):.0f}")
print()

# Question 3: Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

import sys
def add_all_nums(*args):
    total = 0
    for i in args:
        if str(i).isdigit(): # if type(i) == int/float # isinstance(i, int)
            total += int(i)
        else:
            return sys.exit("You are to enter number only. Try again")
    return total

print(f" Add 8 and 5: {add_all_nums(8, 5)}")

# Question 4: Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(c):
    return (c * (9/5)) + 2
print(f"The temperature is {convert_celsius_to_fahrenheit(9)} in F")

# Question 5: Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in ['September', 'October', 'November']:
        return 'autum'
    elif month in ['December', 'January', 'February']:
        return 'winter'
    elif month in ['March', 'April', 'May']:
        return 'spring'
    elif month in ['June', 'July', 'August']:
        return 'summer'
    else:
        return 'invalid input'

print(f"The season is {check_season('May')}")

# Question 6: Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, x2, y1, y2):
    return (y2 - y1) / (x2 - x1)

print(f"The slope of x1 =2, x2 =3, y1 = 4 and y2 = 5 is : {calculate_slope(2,3,4,5):.2f}")

# Question 7: Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
import math
def solve_quadratic(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        r1 = - b + math.sqrt(d / (2 * a))
        r2 = -b - math.sqrt(d / (2 * a))
        return r1, r2
    elif d == 0:
        r1 = - b / (2 * a)
        r2 = - b / (2 * a)
        return r1, r2
    else:
        return 'Imaginary root'

print(f"The solution to the equation is {solve_quadratic(1,4,3)}")
# Question 8: Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(para_lists):
    for para_list in para_lists:
        print(para_list)

print_list([3,2,4,2,'bello', 'erson'])

# Question 9: Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(para_lists):
    for i in range(1, len(para_lists)+1):
        print(para_lists[-i])

reverse_list([3,2,5,7,8,3,8])

# Question 10: Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lists):
    return [list.capitalize() for list in lists]
print(capitalize_list_items(['m','bello','sani', 'jamil']))

# Question 11: Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(p_list,itm):
    p_list.append(itm)
    return p_list

print(add_item([4,2,4], 'sani'))
# Question 12: Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(p_list, item):
    p_list.remove(item)
    return p_list

print(remove_item([3,4,7,5], 5))

# Question 13: Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_number(number):
    total = 0
    for i in range(number+1):
        total += i
    return total
print(f"The sum of 0 to 100 is: {sum_of_number(100)}")

# Question 14: Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(number):
    total = 0
    for i in range(1, number + 1):
        if i % 2 != 0:
            total += i
        else:
            continue
    return total

print(f"The sum of odd numbers btw 0 and 10 is {sum_of_odds(10)}")

# Question 15: Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(number):
    total = 0
    for i in range(1, number+1):
        if i % 2 == 0:
            total += i
        else:
            continue
    return total

print(f"The sum of even numbers btw o and 10 is {sum_of_even(10)}")

"""
    Excerise Level 2
"""
# Question 1: Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(number):
    odd_count = 0
    even_count = 0
    for i in range(number+1):
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(f"The number of odds are: {odd_count} ")
    print(f"The number of evens are: {even_count}")
evens_and_odds(100)

# Question 2: all your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(number):
    factorial = 1
    while number > 0:
        factorial *= number
        number -= 1
    return factorial

print(factorial(10))
print()
# Question 3: Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(x):
    return 'False' if len(x) > 0 else 'True'

print(is_empty([]))
print(is_empty([1, 2, 3, 4]))
print()

# Question 4: Write different functions which take lists. They should calculate_mean, calculate_median,
# calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
import numpy as np
import statistics as st
def stat(x):
    calculate_mean = np.mean(x) #sum (x)/len(x)
    calculate_median = np.median(x)
    calculate_mode = st.mode(x)
    calculate_range = max(x) - min(x)
    calculate_variance = np.var(x)
    calculate_std = np.std(x)
    
    print(f"The mean of the list is: {calculate_mean:.2f}")
    print(f"The median of the list is: {calculate_median}")
    print(f"The mode of the list is: {calculate_mode}")
    print(f"The range of the list is: {calculate_range}")
    print(f"The variance of the list is: {calculate_variance:.2f}")
    print(f"The STD of the list is: {calculate_std:.2f}")
    print()
    
stat([1,2,2,3,4,5,2,6,7,8,2,8,9,10])
    
"""Exercises: Level 3
"""
# Question 1: Write a function called is_prime, which checks if a number is prime.
def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return "Not a Prime number"
    else:
        return "Not a Prime number"
    return "Prime number"
    
print(is_prime(3))
print()

# Question 2: Write a functions which checks if all items are unique in the list.
def unique_item(lists):
    for list in lists:
        if lists.count(list) != 1:
            return "Not Unique Items"
    return "Unique Items"

list = [1,2,6,7,8]
print(unique_item(list))
list = [1,2,6,7,8,6]
print(unique_item(list))
print()

# Question 3: Write a function which checks if all the items of 
# the list are of the same data type.
def same_datatype(lists):
    for i in range(1, len(lists)):
        if isinstance(lists[0], type(lists[i])):
            continue
        else:
            return "Not of the same data type"
    return "Same data type"

test_list = [5, 6, 2, 5, 7, 9, 'same']
print(same_datatype(test_list))

test_list = [5, 6, 2, 2, 5, 7, 9]
print(same_datatype(test_list))

print()

# Question 4: Write a function which check if provided variable 
# is a valid python variable

import re
def check_valid_variable(variable):
    if variable.isidentifier():
        print(f"The variable: {variable} is a valid variable")
    else:
        print(f"The variable: {variable} is not a valid variable")
   
        
        
check_valid_variable('2bagc')
check_valid_variable('fhnmm2')
check_valid_variable('g@dgd')
check_valid_variable('_fg hh')
check_valid_variable('_man')
print()

# Question 5: Go to the data folder and access the counries-data.py file

# Create a function called the most_spoken_langauges in the world. it should return 10 or 20 
# most spoken languages in the world in descending order.
import countries_data
data = countries_data.countries
def most_spoken_language(data=data): # parameter: List of countries and their information 
    
    total_languages = []
    
    for i in range(len(data)):
        total_languages.extend(data[i]['languages'])
    
    languages = {}
    
    for lan in total_languages:
        if lan not in languages:
            languages[lan] = 1
        else:
            languages[lan] += 1

    return dict(sorted(languages.items(), key=lambda x:x[1], reverse=True)[:10])

print(most_spoken_language())
print()
# Create a function called the most_populated_countries. it should
# return 10 or 20 most populated countries in descending

def most_populated_countries(data = data):
    
    populated = {}
    
    for i in range(len(data)):
        populated[data[i]['name']] = data[i]['population']
        
    return dict(sorted(populated.items(), key=lambda x: x[1], reverse=True)[:10])
 
    
print(most_populated_countries())
