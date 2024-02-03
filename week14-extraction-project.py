import os  # This is what grants our interaction with the operating system that lays dormant

# this is the current working directory (cwd)
cw_dir = os.getcwd() 

# This will list all of the files in that directory
files = os.listdir(cw_dir)

# Creating a new list that we'll be adding to
file_data_list = []

for file in files: # Loop that will return the list of files from our current working directory that was given
    file_path = os.path.realpath(file) # Displays the path for each of the files
    file_size = os.path.getsize(file) # Gathers our file size for display
    file_data_list.append({'path': file_path, 'size:': file_size}) # Adding/nesting our dictionaries into our file_data_list

print (*file_data_list, sep='\n')  # As this prints our key-value pairs, they'll be organized on seperate lines for a better visiual
