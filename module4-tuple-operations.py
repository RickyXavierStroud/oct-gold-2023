user_data = ('John', 'American', 1964)
print(len(user_data))

user_data = ('John', 'American', 1964)
if 'American' in user_data:
    print('This peerson comes from the US!')

user_data = ('John', 'American', 1964)
for element in user_data:
    print(element)

# Can be added and multiplied
user_data = ('John', 'American', 1964) + ('teacher', 'male')
print(user_data)

numbers = (0, 1) * 10
print(numbers)

# Lists are usually used when you want to have many values of the same data type, when the values represent the examples of the same c;ass or phenomenom
male_name = ['Adam', 'Jerry', 'Mark']
berlin_temps = [13.0, 17.5, 12.0]

# Tuples are often used when you want to group together values of different types that are somehow related and for a structure
user_data = ('John', 'American', 1964)

# Often used to perform pyhon operations quicker
first = 5
second = 7
first, second = second, first