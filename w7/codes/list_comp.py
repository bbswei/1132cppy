# List Comprehensions

vec = [2, 4, 6]

print([3*x for x in vec])

print([[x, x**2] for x in vec])

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]

print([x*y for x in vec1 for y in vec2])
print([x+y for x in vec1 for y in vec2])

print([vec1[i]*vec2[i] for i in range(len(vec1))])

# List comprehensions are much more flexible than map()

print([str(round(355/113.0, i)) for i in range(1, 6)])

# Nested List Comprehensions

mat = [[1,2,3], [4,5,6], [7,8,9]]

print([[row[i] for row in mat] for i in [0, 1, 2]])

#for i in [0, 1, 2]:
    #for row in mat:
        #print row[i],
    #print

print(zip(*mat))

# The del statement

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a

# Tuples and Sequences
#Tuples, like strings, are immutable: it is not possible to assign to the
#individual items of a tuple 

t = 12345, 54321, 'hello!'

x, y, z = t # sequence unpacking 

# Sets
# A set is an unordered collection with no duplicate elements. Basic
# uses include membership testing and eliminating duplicate entries.
# Set objects also support math operations like union, intersection,
# difference and symmetric difference.

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)               # create a set without duplicates
print(fruit)

print('orange' in fruit)
print('crabgrass' in fruit )

a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

#  Dictionaries

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127

print(tel)
print(tel['jack'])

del tel['sape']

tel['irv'] = 4127
print(tel)
print(tel.keys())
print('guido' in tel)

# dict() constructor builds dictionaries directly from lists of key-value
# pairs stored as tuples

print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
print(dict([(x, x**2) for x in (2, 4, 6)]))

## Looping Techniques

# When looping through dictionaries, the key and corresponding value can be
# retrieved at the same time using the iteritems() method.

knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for k, v in knights.items():
    print(k, v)

# When looping through a sequence, the position index and corresponding value
# can be retrieved at the same time using the enumerate() function.

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# To loop over two or more sequences at the same time, the entries can be
# paired with the zip() function.

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


# To loop over a sequence in reverse, first specify the sequence in a
# forward direction and then call the reversed() function.

for i in reversed(range(1,10,2)):
    print(i)

# To loop over a sequence in sorted order, use the sorted() function which
# returns a new sorted list while leaving the source unaltered.

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

###################################################

