emails = {
    'Anne Stahl': 'astahl@gmail.com',
    'Peter Small': 'peters@yandex.com',
    'Mark Steel': 'mark@steel.com'
}
print(emails['Mark Steel'])

spanish_animals = {
    'dog': 'el perro',
    'cat': 'el gato',
    'horse': 'el caballo',
    'bird': 'el pájaro'
     }
print(spanish_animals['bird'])

# Can't have the same given key
spanish_animals = {
    'dog': 'el perro',
    'cat': 'el gato',
    'horse': 'el caballo',
    'bird': 'el pájaro',
    'bird': 'el ave'
    }
print(spanish_animals)

# Dictionary can't find key using value, one way street. Also given error if it can't find key
spanish_animals = {
    'dog': 'el perro',
    'cat': 'el gato',
    'horse': 'el caballo',
    'bird': 'el pájaro'
     }
print(spanish_animals['el perro'])
     
# Integers, floats and tuples as keys. Not lists
tennis_ranking = {
    1: 'Ashleigh Barty',
    2: 'Naomi Osaka',
    3: 'Simona Halep'
    }
    
# This will not work
tennis_ranking = {
    [1]: 'Ashleigh Barty',
    [2]: 'Naomi Osaka',
    [3]: 'Simona Halep'
    }
    
# Key must be immutable, the value can be of any data type in python
# List can't be a key but it can be a value
city_ratings = {
    'Bangkok': [7, 4, 7, 5],
    'Hanoi': [7, 6, 4, 5],
    'Manila': [6, 6, 4, 4, 5]
    }
