import random
import string

print('''
=============================
=== Random Name Generator ===
=============================
''')

n = int(input('EC2 instances needed:'))
dept = input('Your dept (Accounting, Marketing, and/or FinOps): ').lower()

if (dept == 'marketing' or dept == 'accounting' or dept == 'finops'):
    for suffix in range(0,n):
        print(dept, random.randrange(0,100,1))
else:
    print('Generating Not Allowed! ')