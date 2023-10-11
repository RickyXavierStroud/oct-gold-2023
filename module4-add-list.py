# Data provided to the print output but is not related
print('Hello')

# Function can give data back to you that you give it, but input function has no control over the data
name = input('name?')

# Method is owned by the data it works for, method exists alongside the method it belongs to
# If its no data then can't use its method
book_ratings = [7, 9, 5, 6, 8]

# Use append method to add 4(adds to end of the list)
book_ratings.append(4)
print(book_ratings)

# append(4) on its own wouldn't work b/c append isn't a function and there's no method partnered with it, and will give an error.
# append(4)

# insert method can add to particular spot in the list
# This one adds 10 in index 1 location of the list
book_ratings = [7, 9, 5, 6, 8]
book_ratings.insert(1, 10)
print(book_ratings)