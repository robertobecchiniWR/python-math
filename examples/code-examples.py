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
# funcA(0.5, 2) = funcA(0.5, b=2) = 2.5
# funcA(1) = 2
# funcA() -> ERROR


def funcB(*args, **kwargs):
    # args = list of argument = list
    for elt in args:
        print(elt)
    # kwargs = list of keyword arguments = dict
    for key in kwargs.keys():
        print('{}-{}'.format(key, kwargs[key]))
# Try: funcB(1, 2, 3, 5, b=10, c=45), funcB(1, 2, a=10, bb=45), ...
# WARNING: funcB(1, 2, b=10, c=45, 5) => ERROR


# Example of kwargs use
kwargs = {'b': 12}
print(funcA(1, **kwargs))  # Returns 13
kwargs['b'] = 0
print(funcA(1, **kwargs))  # Returns 1
