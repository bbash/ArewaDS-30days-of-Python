"""
    Day 7 of 30 Days of Python Exercise
    @ Abubakar
"""
"""
    Excerise Level 1
"""
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Question 1: Find the length of the set it_companies
print(f"The length of the set it_companies is : {len(it_companies)}")
print()

# Question 2: Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
print()

# Question 3: Insert multiple IT companies at once to the set it_companies
new_it = ['Whatapp', 'X_clone']
it_companies.update(new_it)
print(it_companies)
print()

# Question 4: Remove one of the companies from the set it_companies
it_companies.remove('Whatapp')
print(it_companies)
print()

# Question 5: What is the difference between remove and discard
"""
    remove return raise an error exception when the item you are to remove is absent 
        while
    card does not raise an error exception when the item if not found in the set.
"""

"""
    Excerise Level 2
"""

# Question 1: Join A and B
C = A.union(B)
print(C)
print()

# Question 2: Find A intersection B
print(A.intersection(B))
print()

# Question 3: Is A subset of B
print(f"Is A subset of B: {A.issubset(B)}")
print()

# Question 4: Are A and B disjoint sets
print(f"Are A and B disjoint sets: {A.isdisjoint(B)}")
print()

# Question 5: Join A with B and B with A

# Question 6: What is the symmetric difference between A and B
print(A.symmetric_difference(B))
print()
# Question 7: Delete the sets completely
del A
#print(f"Delete the sets completely A: {A}")

"""
    Excerise Level 3
"""

# Question 1: Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(f" Is the length of set age and list age the same: {len(age) == len(age_set)}")

# Question 2: Explain the difference between the following data types: string, list, tuple and set
"""
 The key differences are mutability, order, uniqueness, and indexing support among 
 these data types. Strings and tuples are immutable, while lists are mutable. 
 Lists and tuples are ordered, but sets are unordered. Sets only contain unique elements,
 and strings and lists support indexing.

"""
# Question 3: I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people.".split()
print(sentence)
unique_words = set(sentence)
print(unique_words)
print(len(unique_words))
print()

