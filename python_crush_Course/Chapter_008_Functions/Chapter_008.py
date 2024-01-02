# 8-1 Message
def display_message():
    """A function that display what I am learning
    """
    print("I am learning hpw to write a function in Python")

# calling the function
display_message()

# 8-2 Favourite Book
def favourite_book(title):
    """Display the title of my favourite book
    Args:
        title: The name of my favourite book
    """
    print(f"One of my favourite books is {title}")

# calling the function
favourite_book('Alice in Wonderland')

# 8-3 T-Shirt
def make_shirt(size, message):
    """A function to print the size of shirt and a messageto print
    Args:
        size : T-Shirt size
        message : Message to print on the short
    """
    print(f"The size of the T-Short is {size}, {message}")

# calling function
make_shirt('large', 'Welcome to Python')
make_shirt(size='medium', message='Welcome to Python')

# 8-4 Large Shirt
def make_shirt(size='large', message='I love Python'):
    """display T-short information
    Args:
        size (str, optional): _description_. Defaults to 'large'.
        message (str, optional): _description_. Defaults to 'I love Python'.
    """
    print(f"The size of the T-Short is {size}, {message}")

# calling function
make_shirt()
make_shirt(size='medium')
make_shirt(size='small', message='I love coding..')

# 8-5 Cities
def describe_city(name_of_city, country=None):
    print(f'{name_of_city} is in {country}')

# calling function
describe_city('Delta')
describe_city(name_of_city='Abuja', country='Nigeria')
describe_city(name_of_city='Cairp', country='Egypt')

# 8-6 Ciyt Names
def city_country(name_of_city, country):
    """A function that return name of city and its country
    Args:
        name_of_city (str): City name
        country (str): it country
    """
    return f"{name_of_city}, {country}"

# calling function
city_name = city_country(name_of_city='Abuja', country='Nigeria')
print(city_name)
city_name = city_country(name_of_city='London', country='UK')
print(city_name)
city_name = city_country(name_of_city='Accra', country='Ghana')
print(city_name)

# 8-7 Album
def make_album(artisit_name, album_title, number_of_song=None):
    """Store the artist name and album title in a dictionary
    Args:
        artisit_name (_type_): _description_
        album_title (_type_): _description_
    """
    result = {'name': artisit_name, 'title':album_title}
    if number_of_song:
        result['number'] = number_of_song
    return result

# calling function
album_info = make_album(artisit_name='Shata', album_title='Bakandamiya')
print(album_info)
album_info = make_album(artisit_name='Nazifi', album_title='Inda Rai')
print(album_info)
album_info = make_album(artisit_name='Umar M', album_title='Ni da ke')
print(album_info)
album_info = make_album(artisit_name='Umar M', album_title='Ni da ke', number_of_song=5)
print(album_info)

# 8-8 User Albums
while True:
    print('Please, tell me the information about the album or "q" to quit')
    name = input('Enter the name of the Artist: ')
    if name == 'q':
        break
    title = input("Enter the title of the album: ")
    if title == 'q':
        break

    info = make_album(artisit_name=name, album_title=title)
    print(info)

# 8-9 Message
message = ['I love Python', 'Functions are awesome']

def show_message(lst):
    for i in lst:
        print(i)

#calling function
show_message(lst=message)

# 8-10 Sending Messages
def send_message(message, sent_message):

    while message:
        current_message = message.pop()
        print(f"Send message: {current_message}")
        sent_message.append(current_message)

message = ['Hello world', 'I ate rice', 'Money is good']
sent_messages = [] 

send_message(message=message, sent_message=sent_messages)
show_message(lst=sent_messages)

# 8 - 11 Archived Messages
message2 = ['Hello world_2', 'I ate rice_2', 'Money is good_2']
send_message(message=message2[:], sent_message=sent_messages)
print('Original List')
print(message2)

# 8 - 12 Sandwiches
def sandwiches(*args):
    print('Sandwish summary:')
    for arg in args:
        print(arg)

# calling function
sandwiches('a','c','r','w')
sandwiches('a')
sandwiches('CAKE', 'MEATPIE')

# 8 - 13
def build_profile(first, last, **userprofile):
    userprofile['firstname'] = first
    userprofile['lastname'] = last
    return userprofile

# calling function
person1 = build_profile('sani', 'bello')
print(person1)
person2 = build_profile('sani', 'bello', city ='Abuja', country ='Nigeria')
print(person2)
person3 = build_profile('sani', 'bello', is_married = 'True')
print(person3)

# 8- 14 Cars
def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

# calling function
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

# 8 -15 Printing Models: created a file printing_functions and printing_models in the dir

# 8 - 16: Import
import build_profile
from build_profile import build_profile
from build_profile import build_profile as bf
import build_profile as uf
from build_profile import *

# 8-17 Styling Functions: Done