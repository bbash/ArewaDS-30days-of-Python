"""
    Day 6 of 30 Days of Python Exercise
    @ Abubakar
"""
"""
    Excerise Level 1
"""

# Question 1: Create an empty tuple
name = ()
name = tuple()

# Question 2: Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('sani', 'bello', 'nasir')
sisters = ('asiya', 'maryam')


# Question 3: Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)
print()

# Question 4: How many siblings do you have?
print(len(siblings))
print()

# Question 5: Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_member = list(siblings)
family_member.append('Bello')
family_member.append('Binto')
family_member = tuple(family_member)
print(family_member)
print()

"""
    Excerise Level 2
"""

# Question 1: Unpack siblings and parents from family_members

# Question 2: Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Mango', 'Orange', 'Banana')
vegetables = ('water leaf', 'Zogale')
animal_product = ('Milk', 'Meat')
food_stuff_tp = fruits + vegetables + animal_product
print(food_stuff_tp)
print()

# Question 3: Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_tp = list(food_stuff_tp)
print(type(food_stuff_tp)) 

# Question 4: Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_item = food_stuff_tp[3:4]

# Question 5: Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_tp[:3]
last_three = food_stuff_tp[-3:]

# Question 6: Delete the food_staff_tp tuple completely
del food_stuff_tp

# Question 7: Check if an item exists in tuple:
#print(food_stuff_tp)

# Question 8: Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)

# Question 9: Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)