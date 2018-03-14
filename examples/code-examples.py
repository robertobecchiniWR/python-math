# Slide : Basic variables types and operations
# To run this block : ctrl + enter or

# Integer
n = 1
m = 7 % 3  # m = 1

# Float: By default, double precision!
x = 0.5
y = x/7  # y = 0.07142857142857142

# Complex
z = 1+1j
w = z + x + n  # Automatic conversion, w = 2.5 + 1j

# String
s = 'salut'
t = 'toi'
r = s + t  # r = 'saluttoi'

# Boolean
p = True
q = (n != 1)*p + (n == 1)*(x < 10)*(y >= 0)  # q = True = 1

# %% Slide : Lists

# Lists
l = [1, 2, 5, 6]
# Access elements : l[0] = 1, l[2] = 5, l[-1] = 6
# Slice : l[1:3] = [2, 5]

# Nested list
nl = [['vive', 'la'], ['saucisse', 2], 'Toulouse']
# Access sublist element : nl[0] = ['vive', 'la']
# Access final element : nl[0][1] = 'la', nl[1][0] = 'saucisse'

# List comprehension
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [3 * n + 1 for n in l1 if n % 2 == 0]
# l2 = [7, 13, 19, 25, 31]
# %% Slide : Dictionaries

# Dictionaries
d = {'first': 1,
     'second': 'two',
     'third': {'A': [3, 4, 5], 'B': True}}
# Access elements : d['first'] = 1, d['second'] = 'two'
#                   d['third'] = {'A': [3, 4, 5], 'B': True}
#                   d['third']['A'] = [3, 4, 5]
#                   d['third']['A'][1] = 4
#                   d['third']['B'] = True


# %% Slide : Conditional structures

# If clause
if 1 == 2:
    print('Tocard')
elif 1 == 0:  # Not mandatory
    print('Toujours pas')
else:  # Not mandatory
    print("OK d'accord")

# For loop
for i in range(5):
    print('i = {}'.format(i))

# While loop
i = 0
while i < 10:
    print('TAIHOOO-' + str(i))
    i += 1
    if i == 5:
        break  # Allows to escape from the while loop


# %% Slide : Function definition
def funcA(a, b=1):
    return a + b


print(funcA(1))  # Print 2, default value (1) used for b
print(funcA(0.5, 2))  # Print 2.5, 2 is used for b
print(funcA(0.5, b=2))  # Equivalent way to set b=2
# funcA() -> ERROR : at least a must be given


# Arguments can be passed as dictionnary for multi-argument functions like :
def funcB(x, y, p1=None, p2=1, p3='o', p4=False):
    return '{}, {} -- p1={}, p2={}, p3={}, p4={}'.format(x, y, p1, p2, p3, p4)


# -- Arguments are only written once
kwargs = {'p1': 12, 'p2': 2, 'p3': 'i', 'p4': True}
print(funcB(1, 2, **kwargs))  # Print 1, 2 -- p1=12, p2=2, p3=i, p4=True
print(funcB('a', 'b', **kwargs))  # Print a, b -- p1=12, p2=2, p3=i, p4=True
