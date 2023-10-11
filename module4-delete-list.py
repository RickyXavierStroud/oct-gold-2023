top_cities = ['NYC', 'LA', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
del top_cities[2]
print(top_cities)

# Elements to the right shift to the left of the list as one is deleted
print(top_cities[2])

# We want to keep the first 3 elements of the list and delete th remaining 2.
top_cities = ['NYC', 'LA', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
del top_cities[3:]
print(top_cities)

# Delete all elements in list with a slice with both indexes omitted.
top_cities = ['NYC', 'LA', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
del top_cities[:]
print(top_cities)

# Can delete list by running del with the list name (Gives back an error)
top_cities = ['NYC', 'LA', 'Singapore', 'Chicago', 'Houston', 'Phoenix']
del (top_cities)
print(top_cities)