"""
    Day 8 of 30 Days of Python Exercise
    @ Abubakar
"""
"""
    Excerise Level 1
"""
# Question 1: Create an empty dictionary called dog
dog = {}
print(dog)
dog_2 = dict()
print(dog_2)
print()

# Question 2: Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'puppy'
dog['color'] = 'red'
dog['breed'] = 'German Shephard'
dog['age'] = 20
print(dog)
print()

# Question 3: Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name' : 'Sani',
    'last_name' : 'Bello',
    'gender' : 'Male',
    'marital_status' : 'married',
    'skills' : ['Programming', 'Welding', 'Waching'],
    'country' : 'Nigeria',
    'city' : 'Kaduna',
    'address' : 'Kaduna South'
}
print(student)
print()

# Question 4: Get the length of the student dictionary
print(len(student))
print()

# Question 5: Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))
print()

# Question 6: Modify the skills values by adding one or two skills
student['skills'].append('Football')
student['skills'].append('Swmin')
print(student['skills'])
print()

# Question 7: Get the dictionary keys as a list
print(student.keys())
print()

# Question 8: Get the dictionary values as a list
print(student.values())
print()

# Question 9: Change the dictionary to a list of tuples using items() method
print(student.items())
print()

# Question 10: Delete one of the items in the dictionary
del student['city']
print(student)

# Question 11: Delete one of the dictionaries

print(dog)
del dog
#print(dog)