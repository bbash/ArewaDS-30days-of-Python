# Question 1: Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filter_list = [number for number in numbers if number <= 0]
print(f"Remove the negative number: {filter_list}")
print()

# Question 2: Flatten the following list of lists of lists to a one dimensional list
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

new_list = [nn for rows in list_of_lists for nns in rows for nn in nns]
print(new_list)
print()

# Question 3: Using list comprehension create the following list of tuples:
list_of_tuple = [  (i, *[(i ** j) for j in range(6)]) for i in range(11)]
print(list_of_tuple)
print()

# Question 4: Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatten_countries = [row for rows in countries for row in rows]
print(flatten_countries)
print()

# Question 5: Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
country_dic = [{'name':row[0], 'city': row[1]} for rows in countries for row in rows]
print(country_dic)
print()

# Question 6: Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
name_lsit = [row[0] + ' ' + row[1] for rows in names for row in rows]
print(name_lsit)
print()

# Question 7: Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1, x2, y1, y2: (y2 - y1) / (x2 - x1)
print(f"The slope is: {slope(1,25,4,5):.2f}")