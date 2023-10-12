# We can use indexing and slicing with strings to read individual characters or groups of characters
# Gives the sixth letter
fav_band = 'Green Day'
print(fav_band[6])

# Gives the first 6 letters
print(fav_band[:6])

# Can not use inndexing to change individual characters within a string
# Gives error
# fav_band[6] = 'M'

# We have string methods that tranfsorms string and gives new string back
text = 'please capitlize me'
text_cap = text.upper()
print(text_cap)

# String method returns true or false
user_number = input('Please provide a number: ')
if user_number.isnumeric():
    print('Thank you, that\'s a correct number!')
else:
    print('Sorry,', user_number, 'is not a number!')