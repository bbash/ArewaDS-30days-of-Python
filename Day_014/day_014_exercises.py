"""
    Exercises: Level 1
"""

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Question 1: Explain the difference between map, filter, and reduce.

'''
Map = is a built-in function that takes in two parameters; functions
      and list. It iterating over the list
filter = is also a built-in function that takes int two paramters; functions
        and list. It return boolean for each item in the list
reduce = built-in function with two paramters; function and a list.
        it returns a single number as an output.
'''

# Question 2: Explain the difference between higher order function, 
# closure and decorator 

higher_order_function = ''' Is a function that accept a function 
as a parameter or returning a function as a return value from
another function.
'''

Closure = '''Is the processing of nesting a function inside another 
        function and return the inner function.'''
        
decorators = ''' is a way of adding new functionality to an existing
            object.

'''

# Question 3: Define a call function before map, filter or reduce, 
# see examples.
def cube(x):
    return x ** 3
map_result = map(cube, [1,2,3,4,5])
print(f"Map: {list(map_result)}")

def greater_than_10(x):
    if x >= 10:
        return x
    
filter_result = filter(greater_than_10, [12, 4, 5,34, 10, 8, 9,11])
print(f"These numbers are greater than 10: {list(filter_result)}")

def add_num(x , y):
    return (x) + (y)

import functools as f

reduce_result = f.reduce(add_num, [1,2,3,4,5,67,8])
print(f"Reduce is: {reduce_result}")

# Question 4: Use for loop to print each country in the countries 
# list.
for country in countries:
    print(country)
# Question 5: Use for to print each name in the names list.
for name in names:
    print(name)

# Question 6: Use for to print each number in the numbers list.
for number in numbers:
    print(number)


"""
Level 2 exercises
"""
# Question 1: Use map to create a new list by changing each country to uppercase in the countries list
def change_country_uppercase(country):
    return country.upper()

named_country_upper = map(change_country_uppercase, countries)
print(f"Countries in capital letter: {list(named_country_upper)}")


# Question 2: Use map to create a new list by changing each number to its square in the numbers list
def square_number(number):
    return number ** 2

square_number = map(square_number, numbers)
print(f"The square the item in the list is: {list(square_number)}")


#Question 3: Use map to change each name to uppercase in the names list
def named_upper(name):
    return name.upper()

named_to_upper = map(lambda name: name.upper(), names)
print(f"Change names to Uppercase: {list(named_to_upper)}")

# Question 4: Use filter to filter out countries containing 'land'.
def contain_land(country):
    if 'land' not in country:
        return True
    return False

no_land = filter(contain_land, countries)
print(f"List of countires without land: {list(no_land)}")

# Question 5: Use filter to filter out countries having exactly six characters.
def length_of_six(country):
    if len(country) != 6:
        return 1

length_country = filter(length_of_six, countries)
print(f"Countries with length not exactly six letters: {list(length_country)}")

# Question 6: Use filter to filter out countries containing six letters and more in the country list.
def lenght_six_more(country):
    if len(country) >= 6:
        return False
    else:
        return True

six_less = filter(lenght_six_more, countries)
print(f"Countries less than six letters: {list(six_less)}")

# Question 7: Use filter to filter out countries starting with an 'E'
def start_E(country):
    if country.startswith('E'):
        return 1
    return 0

start_with_E = filter(start_E, countries)
print(f"List of countries that start with E:{list(start_with_E)}")

# Question 8: Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
no_land = filter(contain_land, map(lambda x : x.upper(), countries ))
print(f"Chain filter and map: {list(no_land)}")

# Question 9: Declare a function called get_string_lists which takes a list as a parameter and then
# returns a list containing only string items.
def get_string(p_list):
    if type(p_list) == str:
        return True
    return False

only_string = filter(get_string, [3,'5','r', 'd', 4, 3])
print(f"List contain only string: {list(only_string)}")

# Question 10: Use reduce to sum all the numbers in the numbers list.
def sum_of_number(x,y):
    return int(x) + int(y)

s = f.reduce(sum_of_number, numbers)
print(s)

# Question 11: Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
def c_country(country1, country2):
    return f"{country1+ ', '+ country2}"
north_c = f.reduce(c_country, countries)
print(north_c + 'are noth European countries')

# Question 12: Declare a function called categorize_countries that 
# returns a list of countries with some common pattern (you can find the
# countries list in this repository as countries.js(eg 'land', 'ia', 
# 'island', 'stan')).
from countries import countries as c

def categorize_countries(pattern, countries):
    lst = []
    for country in countries:
        if pattern in country.lower():
            lst.append(country)
    return pattern, lst

pattern , result = categorize_countries('ang', c)
print(f"{pattern}:  {result}")

# Question 13: Create a function returning a dictionary, where keys 
# stand for starting letters of countries and values are the number of 
# country names starting with that letter.
def countries_dict(country):
    dict = {}
    dict[country[:2]] = len(country)
    return dict

result = map(countries_dict, countries)
print(f"Key values of countries and their length: {list(result)}")

# Question 14: Declare a get_first_ten_countries function - it 
# returns a list of first ten countries from the countries.js 
# list in the data folder.

def get_first_ten_countries(countries):
    return countries[:10]
print(f"Return the first 10 countries in the file: {get_first_ten_countries(countries=c)}")

# Question 15:Declare a get_last_ten_countries function that returns the 
# last ten countries in the countries list.
def get_last_ten_countries(countries):
    return countries[-10:]
print(f"Return the last 10 countries in the file: {get_last_ten_countries(countries=c)}")
print()

   
"""
Level 3 exercises

"""
from countries_data import countries_data
# Question 1: Use the countries_data.py (https://github.com/Asabeneh
# /30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:

# Question a : Sort countries by name, by capital, by population
def sorted_by_name(data = countries_data):
    sorted_by_name = sorted(countries_data, key=lambda x: x['name'])
    return sorted_by_name[:2]

def sorted_by_capital(data=countries_data):
    sorted_by_capital = sorted(countries_data, key=lambda x: x['capital'], reverse=True)
    return sorted_by_capital[:2]

def sorted_by_population(data=countries_data):
    sorted_by_population = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    return sorted_by_population[:2]

def higher_fuction_sort(type):
    if type == 'sorted_by_name':
        return sorted_by_name
    elif type == 'sorted_by_capital':
        return sorted_by_capital
    elif type == 'sorted_by_population':
        return sorted_by_population
    
result = higher_fuction_sort('sorted_by_name')
print(f"Sorted by name: {result(data=countries_data)}")
print()

result = higher_fuction_sort('sorted_by_capital')
print(f"Sorted by capital in descending order: {result(data=countries_data)}")
print()

result = higher_fuction_sort('sorted_by_population')
print(f"Sorted by population in descending order: {result(data=countries_data)}")
print()


# Question b : Sort out the ten most spoken languages by location.
def most_spoken_language(data=countries_data): # parameter: List of countries and their information 
    
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

# Question c : Sort out the ten most populated countries.

def most_populated_countries(data = countries_data):
    
    populated = {}
    
    for i in range(len(data)):
        populated[data[i]['name']] = data[i]['population']
        
    return dict(sorted(populated.items(), key=lambda x: x[1], reverse=True)[:10])
    
print(most_populated_countries())
