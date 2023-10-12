numbers = [1, 2, 3, 4]
numbers = []
for i in range(1, 101):
    numbers.append(i)
    print(numbers)

# List comprehension feature (added controlled variable name in front of the loop)
numbers = [i for i in range(1, 101)]
print(numbers)

# Can be complicated, we want to list numbers between 1-100 again but exclude numbers divisable by 3
numbers = [i for i in range(1, 101) if i % 3 != 0]
print(numbers)

# Think of list comprehensions as an actaul list which is cretaed on the fly when creating python programming