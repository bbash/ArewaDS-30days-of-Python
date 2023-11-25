"""
    Day 5 of 30 Days of Python Exercise
    @ Abubakar
"""
"""
    Excerise Level 1
"""
# Question 1: Declare an empty list
empty_list_1 = []
print(empty_list_1)
empty_list_2 = list()
print(empty_list_2)


# Question 2: Declare a list with more than 5 items
abinci = ['Tuwo', 'Waina', 'Shinkafa', 'Dambu', 'Dan wake', 'Alala']
print(abinci)

# Question 3: Find the length of your list
print(f"The length of my list is: {len(abinci)}")

# Question 4: Get the first item, the middle item and the last item of the list
first_item = abinci[0]
middle_item = abinci[2]
last_item = abinci[-1]

# Question 5: Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_type = ['Bashir', 20, 1.7, True, 'Kano']

# Question 6: Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Question 7: Print the list using print()
print(it_companies)

# Question 8: Print the number of companies in the list
print(f"The number of companies in the list is: {len(it_companies)}")
print()

# Question 9: Print the first, middle and last company
print(it_companies[0])
print(it_companies[3])
print(it_companies[len(it_companies) - 1])

# Question 10: Print the list after modifying one of the companies
it_companies[0] = 'New_Facebook'
print(it_companies)

# Question 11: Add an IT company to it_companies
it_companies.append('Twitter')
print(it_companies)

# Question 12: Insert an IT company in the middle of the companies list
it_companies.insert(4, 'Whatapp')
print(it_companies)

# Question 13: Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)

# Question 14: oin the it_companies with a string '#;  '
text = '# '.join(it_companies)
print(text)

# Question 15: Check if a certain company exists in the it_companies list.
print('Whatapp' in it_companies)

# Question 16: Check if a certain company exists in the it_companies list.
it_companies.sort()
print(it_companies)

# Qustion 17: Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Question 18: Slice out the first 3 companies from the list
print(it_companies[:3])

# Question 19: Slice out the last 3 companies from the list
print(it_companies[-3:])


# Question 20: Slice out the middle IT company or companies from the list
print(it_companies[4])

# Question 21: Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# Question 22: Remove the middle IT company or companies from the list
it_companies.remove('Microsoft')
print(it_companies)

# Question 23: Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# Question 24: Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Question 25: Destroy the IT companies list

# Question 26: Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

# Question 27: After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)


"""
    Excerise Level 2
"""
import statistics

# Question 1: The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# a: Sort the list and find the min and max age
ages.sort()
print(f"The minimum is {ages[0]}")
print(f"The maximum is {ages[-1]}")

# b: Add the min age and the max age again to the list
ages.append(19)
ages.append(26)

# c: Find the median age (one middle item or two middle items divided by two)
print(statistics.median(ages))

# d: Find the average age (sum of all items divided by their number )
print(statistics.mean(ages))

# e: Find the range of the ages (max minus min)
ages.sort()
print(f"The range is {ages[-1] - ages[0]}")

# f: Compare the value of (min - average) and (max - average), use abs() method

# Question 1: Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]
middle = int(len(countries) / 2)
print(f"The middle country in the list is {countries[middle]}")

# Question 2: Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_part = countries[:middle]
second_part = countries[middle:]

# Question 3: ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

ch, ru, usa, *scandic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(ch)

