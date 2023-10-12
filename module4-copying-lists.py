name_original = 'Jon Snow'
name_new = name_original
name_original = 'Daenerys Targaryen'
print(name_original, name_new)

# Name of list is a memory reference so when modifying, it'll modify both b/c they use the same reference point
list_original = [1, 2, 3]
list_new = list_original
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)

# Use slicing to modify independently
list_original = [1, 2, 3]
list_new = list_original[:]
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)

# Modifying/copying the first 2 elements into a new list
list_original = [1, 2, 3]
list_new = list_original[:2]
list_original[0] = -5
print('Original:', list_original, '\nNew:', list_new)

# To create a new variable that points to the very same list(they point/refernce the same list so when one is modified, the other is modified)
# list_original = [1, 2, 3]
# list_new = list_original

# Copying a list to have 2 different lists and variables
# list_original = [1, 2, 3]
# list_new = list_original[:]