# Lists

city_1 = "NYC"
city_2 = "LA"
city_3 = "Chicago"
city_4 = "Houston"
city_5 = "Phoenix" # Applicable but not the best way

# Much better

empty_lists = []
top_cities = ['NYC', 'LA', 'Chicago', 'Houston', 'Phoenix']
print(top_cities)

# First element has index of 0 
print(top_cities[0])

# Second element has index of 1
print(top_cities[1])

# Fifth element has index of 4
print(top_cities[4])

# Nonexisting element error
    # print(top_cities[5])


# Negative index, negative index of 1 sends you to the last element of the list
print(top_cities[-1])

# Second to last
print(top_cities[-2])

# When you have 5 elements you can go as far as.....
print(top_cities[-5])

# Same error message if we use negative index for nonexisting elements
    # print(top_cities[-6])
    
# Slicing indexes for calling seperate elements 
# Index 0(beginning) is inclusive but index 2(end) isn't so 1st element is inclusive but the 3rd one isn't
print(top_cities[0:2])

# Take all elements starting at index 2 until the very end of the list
print(top_cities[2:])

# Take all elemtns from the start until the index 3 exclusive
print(top_cities[:3])

# Can all of them which equals the same thing as all the elements, sme as print(top_cities)
print(top_cities[:])

# Slicing nonexisting indexes will just end with an empty block/list
print(top_cities[10:15])

# Quick Recap
# Casual standard string variable with a single string insight
top_city = 'NYC'

# Empty list introduced with a square bracket
top_cities = [0]

# List with multiple elements
top_cities = ['NYC', 'LA', 'Chicago', 'Houston', 'Phoenix']

# Will give you access to the fifth element from the end, in this case it is the first element in the list or from the l
print(top_cities[-5])

# Slice gives you 3 elements with inexes 0, 1, and 2
print(top_cities[0:3])
 
# When you access a single element you get a string value
print(top_cities[0])
 
# But if you use slicing here, you get a list with a single string inside
print(top_cities[0:1])