first = input('Enter first number: ')
second = input('Enter second number :')
print('Before swapping:', first, second)
first = second
second = first
print('After swapping:', first, second)

# Properly swapping
first = input('Enter first number: ')
second = input('Enter second number :')
print('Before swapping:', first, second)
temporary = first
first = second
second = temporary
print('After swapping:', first, second)

# Shortcut
first = input('Enter first number: ')
second = input('Enter second number :')
print('Before swapping:', first, second)
first, second = second, first
print('After swapping:', first, second)

# Can do the same with lists
top_cities = ['NYC', 'LA', 'Chicago', 'Houston', 'Phoenix']
top_cities[0], top_cities[4], = top_cities[4], top_cities[0]
print(top_cities)

# Sort list
top_cities = ['NYC', 'LA', 'Chicago', 'Houston', 'Phoenix']
top_cities.sort()
print(top_cities)

# Sorts numbers too
random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort()
print(random_numbers)

# For reverse argument/pattern/order add reverse=True to sort
random_numbers = [2, 5, 0, -3, 4]
random_numbers.sort(reverse=True)
print(random_numbers)

# Sort method can be more of a permanent change and you might need a list sorted temporarily. This is where the sorted function comes in at.
top_cities = ['NYC', 'LA', 'Chicago', 'Houston', 'Phoenix']
print(sorted(top_cities))
print(top_cities)