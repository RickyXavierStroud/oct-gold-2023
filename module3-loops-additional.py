# pass does nothing but you have to have something inside the loops body
for i in range(11):
    pass

# nested loops
for a in range(1,6):
    for b in range(1,6):
        print(a, 'x', b, '=', a * b)

# loops with else statements(rarely used)
i = 2
while i < 5:
    print(i)
    i += 1
else:
    print('else:', i)