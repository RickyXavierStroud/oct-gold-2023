import sys

# System Exit
user_name = input('What is your name? ')
if user_name == '':
  print('Empty name? I cannot work with that. I am closing the program. Bye!')
  sys.exit()
print('Hello,', user_name)
print('Let us get started...')

# Keyboard Interrupt
 #while True:
  #print('hi!')
  
# Index Error
#programming_languages = ["Java", "Python", "C++"]
#print(programming_languages[10])

# Key Error
#ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
#ages['Michael']

# Type Error
#age = input('What is your age? ')
#print('In 10 years, you will be', age + 10)

# Value Error
age = int(input('What is your age? '))