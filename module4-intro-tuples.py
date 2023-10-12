# Empty tuple
empty_tuple = ()

# One element tuple
one_el_tuple_a = (1,)
one_el_tuple_b = 1,

# More than one value in your tuple means the comma st the end is optional
three_el_tuple = 1, 2, 3
print(three_el_tuple)

# Mutable data can be updated
user_data = ('John', 'American', 1964)
user_data = ('Katya', 'Russian', 1980)
# Can't append like with lists  -user_data.append('teacher')
# can't delete -del user_data[0]

# Can slice when it comes to reading/printing element of tuple
print(user_data[0])

# Can't change it using indexing -user_data[0] = 'Mark'

# Strings in python are also immutable
# You can assign new string to the same variable
message = 'welcome'
message = 'Welcome'

# Can't change the existing string
message[0] = 'w'