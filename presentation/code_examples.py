# %% Slide : Basic variables types and operations
# To run this block : ctrl + enter or
# Integer
i1 = 1
i2 = 7 % 3  # i2 = 1

# Float -- by default, double precision !
f1 = 0.5
f2 = f1/7  # f2 = 0.07142857142857142

# Complex
c1 = 1+1j
c2 = c1 + f1 + i1  # Automatic conversion, c2 = 2.5 + 1j

# String
s1 = 'salut'
s2 = 'toi'
s3 = s1 + s2  # s3 = 'saluttoi'

# Boolean
b1 = True
b2 = (i1 != 1)*b1 + (i1 == 1)*(f1 < 10)*(f2 >= 0)  # b2 = True = 1

# %% Slide : Lists
# List
l1 = [1, 2, 5, 6]
# Access elements : l1[0] = 1, l1[2] = 5, l1[-1] = 6
# Slice : l1[1:3] = [2, 5]

# Nested list
l2 = [['vive', 'la'], ['saucisse', 2], 'Toulouse']
# Extract sub-list : l2[0] = ['vive', 'la']
# Access element : l2[0][1] = 'la', l2[1][0] = 'saucisse'

# %% Slide : basic structures
# For loop
for i in range(5):
    print('i = {}'.format(i))

# If condition
if 1 == 2:
    print('Tocard')
elif 1 == 0:  # Not mandatory
    print('Toujours pas')
else:  # Not mandatory
    print("OK d'accord")

# While loop
i = 0
while i < 10:
    print('TAIHOOO-'+str(i))
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
