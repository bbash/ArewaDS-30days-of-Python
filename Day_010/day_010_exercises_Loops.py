"""
    Day 10 of 30 Days of Python Exercise
    @ Abubakar
"""
"""
    Excerise Level 1
"""
# Question 1: terate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print(f'for loop {i}')
else:
    print('end of for loop')

count = 0
while count < 10:
    print(f'while loop {count}')
    count += 1
else:
    print('end of for loop')

# Question 2: Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10,-1, -1):
    print(f'10 to 0 for loo {i}')

count = 10
while count >= 0:
    print(count)
    count -= 1

# Question 3: Write a loop that makes seven calls to print(), so we get on the output the following triangle:
"""
  #
  ##
  ###
  ####
  #####
  ######
  #######
""" 
for i in range(8):
    print('#' * i)
print()

# Question 4: Use nested loops to create the following:
"""
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""
for _ in range(9):
    print('# ' * 9 )
print()

# Question 5: Print the following pattern:
"""

0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
"""
for i in range(11):
   print(f"{i} x {i} = {i * i}")
print()

# Question 6: Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
for skill in ['Python', 'Numpy','Pandas','Django', 'Flask']:
    print(skill)

print()

# Question 7: Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i > 0 and i % 2 == 0:
        print(f'even number: {i}')
print()
# Question 8: Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i > 0 and i % 2 != 0:
        print(f'odd number: {i}')
    
print()

"""
    Excerise Level 2
"""
# Question 1: Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.

total = 0
for i in range(101):
    total += i
print(f"The sum of the numbers is {total}")
print()

# Question 2: Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.
evens_total = 0
odds_total = 0

for i in range(101):
    if i == 0:
        continue
    elif i % 2 == 0:
        evens_total += i
    else:
        odds_total += i
print(f"The sum of all evens is {evens_total}. And the sum of all odds is {odds_total}")
print()

"""
    Excerise Level 3
"""

# Question 1: Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
import countries

for country in countries.countries:
    if 'land' in country:
        print(country)

print()

# Question 2: This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
for fruit in sorted(['banana', 'orange', 'mango', 'lemon'], reverse=True):
    print(fruit)

print()
# Question 3: Go to the data folder and use the countries_data.py file.
import countries_data

#print(countries_data.countries[0])
#print(len(countries_data.countries))

add_countries =[]
for i in range(len(countries_data.countries)):
    add_countries.extend(countries_data.countries[i]['languages'])

# What are the total number of languages in the data
unique_language = set(add_countries) # remove duplicate languge
print(f'The total number if languges in the data is : {len(unique_language)}')

#Find the ten most spoken languages from the data
#print(add_countries)

most_spoken_l = {}

for i in add_countries:
    if i in most_spoken_l:
        most_spoken_l[i] +=1
    else:
        most_spoken_l[i] = 1

sorted_language = dict(sorted(most_spoken_l.items(), key=lambda x: (-x[1], x[0])))
#print(sorted_language)
m = list(sorted_language.keys())
print(m[:10])

# Find the 10 most populated countries in the world
pop_country = {}
for i in countries_data.countries:
    pop_country[i['name']] = i['population']

#print(pop_country)
sorted_pop = dict(sorted(pop_country.items(), key=lambda x: (-x[1], x[0])))
#print(sorted_pop)
m = list(sorted_pop.keys())
print(m[:10])

