import re


"""
Level 1 Exercises
"""
# Question 1: 
paragraph = '''I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'''

most_frequent_word = {}

paragraph = paragraph.replace('.', '').split()
for p in paragraph:
    if p in most_frequent_word:
        most_frequent_word[p] += 1
    else:
        most_frequent_word[p] = 1

l = [(v, k) for k,v in most_frequent_word.items()]  
l.sort(reverse=True)  
print(l)


# Question 2: The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.

sentence = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles."

reg_pattern = r'[-]?\d+'
points = re.findall(reg_pattern, sentence)
print(points)

distance = int(points[-1]) - int(points[1])
print(distance)

"""
Level 2 exercises
"""

# Question 1: Write a pattern which identifies if a string is a valid python variable

def is_valid_variable(word):
    reg_pattern = r'^[a-z_]\w*$'
    if  re.search(reg_pattern, word, re.IGNORECASE):
        return True
    return False

print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True

"""
    Level 3
"""

# Question 1: Clean the following text. After cleaning, count three most frequent words in the string.

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(sentence = sentence):
    clean = re.sub('[%@$#&;!?,]', "", sentence).split()
    return clean

print(*clean_text())

def most_frequent_word(words, number_of_words):
    freq_word = {}

    for word in words:
        if word in freq_word:
            freq_word[word] += 1
        else:
            freq_word[word] = 1
    

    list = [(val,key) for key,val in freq_word.items()]
    list.sort(reverse=True)
    
    return list[:number_of_words]

print(most_frequent_word(clean_text(), 3))
print()
