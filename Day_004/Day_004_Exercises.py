# Question 1: Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
sentence = 'Thirty' + ' ' + 'Days' + ' ' + 'of' + ' ' + 'Python'
print(sentence)


# Question 2: Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
text = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(text)


# Question 3: Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding for All'

# Question 4: Print the variable company using print().
print(company)

# Question 5: Print the length of the company string using len() method and print().
len_company = len(company)
print(f'The length of the company string is {len_company}')


# Question 6: Change all the characters to uppercase letters using upper() method.
print(company.upper())


# Question 7: Change all the characters to lowercase letters using lower() method.
print(company.lower())


# Question 8: Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
text = 'Coding For All'
print(f'Capitalize() : {text.capitalize()}')
print(f'Title()      : {text.title()}')
print(f'Swapcase()   : {text.swapcase()}')

# Question 9: Cut(slice) out the first word of Coding For All string.
text = 'Coding For All'
print(f'The first word:  {text[:6]}')

# Question 10: Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(f'using index: {text.index("Coding")}')
print(f'find index: {text.find("Coding")}')


# Question 11: Replace the word coding in the string 'Coding For All' to Python.
print(f'Replace coding with Python: {text.replace("Coding", "Python")}')

# Question 12: Change Python for Everyone to Python for All using the replace method or other methods.
text = 'Python for Everyone'
print(f"Replace Every to All: {text.replace('Everyone', 'All')}")

# Question 13: Split the string 'Coding For All' using space as the separator (split()) .
text = 'Coding For All'.split()
print(text)

# Question 14: "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
text = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(',')
print(text)

# Question 15: What is the character at index 0 in the string Coding For All.
text = 'Coding For All'
print(f"The character at index 0 is: {text[0]}")

# Question 16: What is the last index of the string Coding For All.
print(f"The last index od the string 'Coding For All' is: {text.rindex('l')}")


# Question 17: What character is at index 10 in "Coding For All" string.
text = 'Coding For All'
print(f"What character is at index 10 in 'Coding For All': {text[10]}")

# Question 18: Create an acronym or an abbreviation for the name 'Python For Everyone'.
text = 'Python For Everyone'
print(f"Acronym {text[:3] + text[-3:]}")

# Question 19: Create an acronym or an abbreviation for the name 'Coding For All'.
text = 'Coding For All'
print(f"Acronyms: {text[:3] + text[-3:]}")

# Question 20: Use index to determine the position of the first occurrence of C in Coding For All.
text = 'Coding For All'
print(f"Position of the first occurrenece of C: {text.index('C')}")

# Question 21: Use index to determine the position of the first occurrence of F in Coding For All.
text = 'Coding For All'
print(f"Position of the first occurrenece of C: {text.index('F')}")

# Question 22: Use rfind to determine the position of the last occurrence of l in Coding For All People.
text = 'Coding For All People'
print(f'The position of the last occurence of l in this text is {text.rfind("l")}')

# Question 23: Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(f"This first occurrence of the word becauses is in {sentence.index('because')}")

# Question 24: Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(f"The last occurence of because in the sentence is {sentence.rfind('because')}")

# Question 25: Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
slic_phrase = sentence[31:54]
print(slic_phrase)

# Question 26: Find the position of the first occurrence of the word
# 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction' 
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(f"The first occurence of the word 'bacause ': {sentence.index('because')}")
# Question 27: Slice out the phrase 'because because because' in the 
# following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
start = sentence.index('because')
last = sentence.rfind('because')
print(sentence[start: 54])
# Question 28: Does ''Coding For All' start with a substring Coding?
text = 'Coding For All'
print(f"Does the word coding start the sentence {text.startswith('Coding')}")

# Question 29: Does 'Coding For All' end with a substring coding?
text = "Coding For All"
print(f"Does 'Coding For All' end with a substring coding: {text.endswith('coding')} ")


# Question 30: '   Coding For All      '  , remove the left and right trailing spaces in the given string.
text = '   Coding For All      ' 
print(text.strip())

# Question 31: Which one of the following variables return True when we use the method isidentifier():
print(f"Is 30DaysOfPython an identifier: {'30DaysOfPython'.isidentifier()}")
print(f"Is thirty_days_of_python an identifier: {'thirty_days_of_python'.isidentifier()}")

# Question 32: The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
text = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(f"Joing with #: {'# '.join(text)}")

# Question 33: Use the new line escape sequence to separate the following sentences
"""
    I am enjoying this challenge.
    I just wonder what is next.
"""
sentence = "I am enjoying this challenge. \nI just wonder what is next."
print(sentence)

# Question 34: Use a tab escape sequence to write the following lines.
"""
    Name      Age     Country   City
    Asabeneh  250     Finland   Helsinki
"""
title = "Name\t\tAge\tCountry\t\tCity"
entry = "Asabeneh\t250\tFinland\t\tHelsinki"
print(title)
print(entry)

# Question 35: Use the string formatting method to display the following:
"""
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
"""
radius = int(input("radius = "))
print(f"area = 3.14 * radius ** 2")
area = 3.14 * radius ** 2
print(f"The area of a circle with raius {radius} is {area} meters square.")


# Question 36: Make the following using string formatting methods:
"""
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 26144
"""
print(f" 8 + 6 = {8 + 6}")
print(f" 8 - 6 = {8 - 6}")
print(f" 8 * 6 = {8 * 6}")
print(f" 8 / 6 = {8 / 6:.2f}")
print(f" 8 % 6 = {8 % 6}")
print(f" 8 // 6 = {8 / 6:.0f}")
print(f" 8 ** 6 = {8 ** 6}")