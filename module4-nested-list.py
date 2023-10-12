# list with integers
numbers = [1, 2, 3, 4]

# list with string
countries = ['UK', 'US', 'Germany']

# can even mix data types in  a list(not recommended)
countries = [1, 'UK', 2, 'US']

# lists can have other lists as elements
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
print(cells[0])

# Accessing a specific element in this sub-list
print(cells[0][0])

# Accessing A2
print(cells[0][1])

# Accessing B3
print(cells[1][2])

# Use "for" loop to  iterate the list and print the elements
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    print('Element:', x)

# Accessing individual string elements inside the sub-list(nested "for" loop)
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for x in cells:
    for y in x:
        print('Element:', y)
        
# Nested lists are multidimentional lists(lists as rows and individual items as x or rows)
table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for row in table:
    for cell in row:
        print('Element:', cell)
        
# Print to rsemble table
table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for row in table:
    for cell in row:
        print(cell, '', end='')
    print()
    
# Can use nested list comprehensions to initialize multidimensional lists
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5

table = [[i for i in range(1, 6)] for j in range(4)]
print(table)