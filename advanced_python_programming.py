# -*- coding: utf-8 -*-
"""Advanced Python Programming.ipynb

"""

list_1 = ["BMW", "Lemborgini", "Baleno"]
print(list_1)

# Or create an empty list with the list function
list_2 = list()
print(list_2)

# Lists allow different data types
list_3 = [5, True, "Baleno"]
print(list_3)

# Lists allow duplicates
list_4 = [0, 0, 1, 1]
print(list_4)

#Access Elements

item = list_1[0]
print(item)

item = list_1[-1]
print(item)

item = list_1[-2]
print(item)

#Change Item

list_1[2] = "Audi Q7"
print(list_1)

my_list = ["BMW", "Lemborgini", "Baleno"]

# len() : get the number of elements in a list
print("Length:", len(my_list))

# append() : adds an element to the end of the list
my_list.append("Creta")

# insert() : adds an element at the specified position
my_list.insert(1, "Land Rover")
print(my_list)

# pop() : removes and returns the item at the given position, default is the last item
item = my_list.pop()
print("Popped item: ", item)

# remove() : removes an item from the list
my_list.remove("Lemborgini") # Value error if not in the list
print(my_list)

# clear() : removes all items from the list
my_list.clear()
print(my_list)

# reverse() : reverse the items
my_list = ["BMW", "Lemborgini", "Baleno"]
my_list.reverse()
print('Reversed: ', my_list)

# sort() : sort items in ascending order
my_list.sort()
print('Sorted: ', my_list)

my_list = ["BMW", "Lemborgini", "Baleno"]
new_list = sorted(my_list)

# create list with repeated elements
list_with_zeros = [0] * 5
print(list_with_zeros)

# concatenation
list_concat = list_with_zeros + my_list
print(list_concat)

# convert string to list
string_to_list = list('Over')
print(string_to_list)

#Copy list

list_org = ["BMW", "Lemborgini", "Baleno"]

# this just copies the reference to the list, so be careful
list_copy = list_org

# now modifying the copy also affects the original
list_copy.append(True)
print(list_copy)
print(list_org)

# use copy(), or list(x) to actually copy the list
# slicing also works: list_copy = list_org[:]
list_org = ["BMW", "Lemborgini", "Baleno"]

list_copy = list_org.copy()
# list_copy = list(list_org)
# list_copy = list_org[:]

# now modifying the copy does not affect the original
list_copy.append(True)
print(list_copy)
print(list_org)

# Iterating
for i in list_1:
    print(i)

#Item Existing check
if "BMW" in list_1:
    print("yes")
else:
    print("no")

#Slicing
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = a[1:3] # Note that the last index is not included
print(b)
b = a[2:] # until the end
print(b)
b = a[:3] # from beginning
print(b)
a[0:3] = [0] # replace sub-parts, you need an iterable here
print(a)
b = a[::2] # start to end with every second item
print(b)
a = a[::-1] # reverse the list with a negative step:
print(a)
b = a[:] # copy a list with slicing
print(b)

#List Comprehension
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [i * i for i in a] # squares each element
print(b)

#Nested List
a = [[1, 2], [3, 4]]
print(a)
print(a[0])

"""Tuple"""

tuple_1 = ("Max", 28, "New York")
tuple_2 = "Linda", 25, "Miami" 
tuple_3 = (25,)
print(tuple_1)
print(tuple_2)
print(tuple_3)
tuple_4 = tuple([1,2,3])
print(tuple_4)

item = tuple_1[0]
print(item)
item = tuple_1[-1]
print(item)

del tuple_2

# Iterating over a tuple by using a for in loop
for i in tuple_1:
    print(i)

if "New York" in tuple_1:
    print("yes")
else:
    print("no")

my_tuple = ('a','p','p','l','e',)

# len() : get the number of elements in a tuple
print(len(my_tuple))

# count(x) : Return the number of items that is equal to x
print(my_tuple.count('p'))

# index(x) : Return index of first item that is equal to x
print(my_tuple.index('l'))

# repetition
my_tuple = ('a', 'b') * 5
print(my_tuple)

# concatenation
my_tuple = (1,2,3) + (4,5,6)
print(my_tuple)

# convert list to a tuple and vice versa
my_list = ['a', 'b', 'c', 'd']
list_to_tuple = tuple(my_list)
print(list_to_tuple)

tuple_to_list = list(list_to_tuple)
print(tuple_to_list)

# convert string to tuple
string_to_tuple = tuple('Hello')
print(string_to_tuple)

# a[start:stop:step], default step is 1
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[1:3] # Note that the last index is not included
print(b)
b = a[2:] # until the end
print(b)
b = a[:3] # from beginning
print(b)
b = a[::2] # start to end with every second item
print(b)
b = a[::-1] # reverse tuple
print(b)

# number of variables have to match number of tuple elements
tuple_1 = ("Max", 28, "New York")
name, age, city = tuple_1
print(name)
print(age)
print(city)

# tip: unpack multiple elements to a list with *
my_tuple = (0, 1, 2, 3, 4, 5)
item_first, *items_between, item_last = my_tuple
print(item_first)
print(items_between)
print(item_last)

a = ((0, 1), ('age', 'height'))
print(a)
print(a[0])

# compare the size
import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

# compare the execution time of a list vs. tuple creation statement
import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))

"""Dictionaries"""

my_dict = {"name":"Max", "age":28, "city":"New York"}
print(my_dict)

# or use the dict constructor, note: no quotes necessary for keys
my_dict_2 = dict(name="Lisa", age=27, city="Boston")
print(my_dict_2)

name_in_dict = my_dict["name"]
print(name_in_dict)

# add a new key
my_dict["email"] = "max@xyz.com"
print(my_dict)

# or overwrite the now existing key
my_dict["email"] = "coolmax@xyz.com"
print(my_dict)

# delete a key-value pair
del my_dict["email"]

# this returns the value and removes the key-value pair
print("popped value:", my_dict.pop("age"))

# return and removes the last inserted key-value pair 
# (in versions before Python 3.7 it removes an arbitrary pair)
print("popped item:", my_dict.popitem())

print(my_dict)

# clear() : remove all pairs
# my_dict.clear()

my_dict = {"name":"Max", "age":28, "city":"New York"}
# use if .. in ..
if "name" in my_dict:
    print(my_dict["name"])

# use try except
try:
    print(my_dict["firstname"])
except KeyError:
    print("No key found")

# loop over keys
for key in my_dict:
    print(key, my_dict[key])

# loop over keys
for key in my_dict.keys():
    print(key)

# loop over values
for value in my_dict.values():
    print(value)

# loop over keys and values
for key, value in my_dict.items():
    print(key, value)

dict_org = {"name":"Max", "age":28, "city":"New York"}

# this just copies the reference to the dict, so be careful
dict_copy = dict_org

# now modifying the copy also affects the original
dict_copy["name"] = "Lisa"
print(dict_copy)
print(dict_org)

# use copy(), or dict(x) to actually copy the dict
dict_org = {"name":"Max", "age":28, "city":"New York"}

dict_copy = dict_org.copy()
# dict_copy = dict(dict_org)

# now modifying the copy does not affect the original
dict_copy["name"] = "Lisa"
print(dict_copy)
print(dict_org)

# Use the update() method to merge 2 dicts
# existing keys are overwritten, new keys are added
my_dict = {"name":"Max", "age":28, "email":"max@xyz.com"}
my_dict_2 = dict(name="Lisa", age=27, city="Boston")

my_dict.update(my_dict_2)
print(my_dict)

# use numbers as key, but be careful
my_dict = {3: 9, 6: 36, 9:81}
# do not mistake the keys as indices of a list, e.g my_dict[0] is not possible here
print(my_dict[3], my_dict[6], my_dict[9])

# use a tuple with immutable elements (e.g. number, string)
my_tuple = (8, 7)
my_dict = {my_tuple: 15}

print(my_dict[my_tuple])

my_dict_1 = {"name": "Max", "age": 28}
my_dict_2 = {"name": "Alex", "age": 25}
nested_dict = {"dictA": my_dict_1,
               "dictB": my_dict_2}
print(nested_dict)

"""Sets"""

my_set = {"apple", "banana", "cherry"}
print(my_set)

# or use the set function and create from an iterable, e.g. list, tuple, string
my_set_2 = set(["one", "two", "three"])
my_set_2 = set(("one", "two", "three"))
print(my_set_2)

my_set_3 = set("aaabbbcccdddeeeeeffff")
print(my_set_3)

a = {}
print(type(a))
a = set()
print(type(a))

my_set = set()

# use the add() method to add elements
my_set.add(42)
my_set.add(True)
my_set.add("Hello")

# note: the order does not matter, and might differ when printed
print(my_set)

# nothing happens when the element is already present:
my_set.add(42)
print(my_set)

my_set = {"apple", "banana", "cherry"}
my_set.remove("apple")
print(my_set)

# KeyError:
# my_set.remove("orange")

# discard(x): removes x, does nothing if element is not present
my_set.discard("cherry")
my_set.discard("blueberry")
print(my_set)

# clear() : remove all elements
my_set.clear()
print(my_set)

# pop() : return and remove a random element
a = {True, 2, False, "hi", "hello"}
print(a.pop())
print(a)

my_set = {"apple", "banana", "cherry"}
if "apple" in my_set:
    print("yes")

my_set = {"apple", "banana", "cherry"}
for i in my_set:
    print(i)

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

i = odds.intersection(primes)
print(i)

i = evens.intersection(primes)
print(i)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

# difference() : returns a set with all the elements from the setA that are not in setB.
diff_set = setA.difference(setB)
print(diff_set)

# A.difference(B) is not the same as B.difference(A)
diff_set = setB.difference(setA)
print(diff_set)

# symmetric_difference() : returns a set with all the elements that are in setA and setB but not in both
diff_set = setA.symmetric_difference(setB)
print(diff_set)

# A.symmetric_difference(B) = B.symmetric_difference(A)
diff_set = setB.symmetric_difference(setA)
print(diff_set)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

# update() : Update the set by adding elements from another set.
setA.update(setB)
print(setA)

# intersection_update() : Update the set by keeping only the elements found in both
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.intersection_update(setB)
print(setA)

# difference_update() : Update the set by removing elements found in another set.
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.difference_update(setB)
print(setA)

# symmetric_difference_update() : Update the set by only keeping the elements found in either set, but not in both
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setA.symmetric_difference_update(setB)
print(setA)

set_org = {1, 2, 3, 4, 5}

# this just copies the reference to the set, so be careful
set_copy = set_org

# now modifying the copy also affects the original
set_copy.update([3, 4, 5, 6, 7])
print(set_copy)
print(set_org)

# use copy() to actually copy the set
set_org = {1, 2, 3, 4, 5}
set_copy = set_org.copy()

# now modifying the copy does not affect the original
set_copy.update([3, 4, 5, 6, 7])
print(set_copy)
print(set_org)

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
# issubset(setX): Returns True if setX contains the set
print(setA.issubset(setB))
print(setB.issubset(setA)) # True

# issuperset(setX): Returns True if the set contains setX
print(setA.issuperset(setB)) # True
print(setB.issuperset(setA))

# isdisjoint(setX) : Return True if both sets have a null intersection, i.e. no same elements
setC = {7, 8, 9}
print(setA.isdisjoint(setB))
print(setA.isdisjoint(setC))

#Frozenset

a = frozenset([0, 1, 2, 3, 4])
odds = frozenset({1, 3, 5, 7, 9})
evens = frozenset({0, 2, 4, 6, 8})
print(odds.union(evens))
print(odds.intersection(evens))
print(odds.difference(evens))

"""Strings"""

my_string = 'Hello'
my_string = "Hello"
my_string = "I' m  a 'Geek'"

# escaping backslash
my_string = 'I\' m  a "Geek"'
my_string = 'I\' m a \'Geek\''
print(my_string)

# triple quotes for multiline strings
my_string = """Hello
World"""
print(my_string)

# backslash if you want to continue in the next line
my_string = "Hello \
World"
print(my_string)

my_string = "Hello World"

# get character by referring to index
b = my_string[0]
print(b)

# Substrings with slicing
b = my_string[1:3] # Note that the last index is not included
print(b)
b = my_string[:5] # from beginning
print(b)
b = my_string[6:] # until the end
print(b)
b = my_string[::2] # start to end with every second item
print(b)
b = my_string[::-1] # reverse the string with a negative step:
print(b)

# concat strings with +
greeting = "Hello"
name = "Tom"
sentence = greeting + ' ' + name
print(sentence)

# Iterating over a string by using a for in loop
my_string = 'Hello'
for i in my_string:
    print(i)

if "e" in "Hello":
    print("yes")
if "llo" in "Hello":
    print("yes")

my_string = "     Hello World "

# remove white space
my_string = my_string.strip()
print(my_string)

# number of characters
print(len(my_string))

# Upper and lower cases
print(my_string.upper())
print(my_string.lower())

# startswith and endswith
print("hello".startswith("he"))
print("hello".endswith("llo"))

# find first index of a given substring, -1 otherwise
print("Hello".find("o"))

# count number of characters/substrings
print("Hello".count("e"))

message = "Hello World"
new_message = message.replace("World", "Universe")
print(new_message)

# split the string into a list
my_string = "how are you doing"
a = my_string.split() # default argument is " "
print(a)
my_string = "one,two,three"
a = my_string.split(",")
print(a)

# join elements of a list into a string
my_list = ['How', 'are', 'you', 'doing']
a = ' '.join(my_list) # the given string is the separator, e.g. ' ' between each argument
print(a)

# use braces as placeholders
a = "Hello {0} and {1}".format("Bob", "Tom")
print(a)

# the positions are optional for the default order
a = "Hello {} and {}".format("Bob", "Tom")
print(a)

a = "The integer value is {}".format(2)
print(a)

# some special format rules for numbers
a = "The float value is {0:.3f}".format(2.1234)
print(a)
a = "The float value is {0:e}".format(2.1234)
print(a)
a = "The binary value is {0:b}".format(2)
print(a)

# old style formatting by using % operator
print("Hello %s and %s" % ("Bob", "Tom")) # must be a tuple for multiple arguments
val =  3.14159265359
print("The decimal value is %d" % val)
print("The float value is %f" % val)
print("The float value is %.2f" % val)

name = "Eric"
age = 25
a = f"Hello, {name}. You are {age}."
print(a)
pi = 3.14159
a = f"Pi is {pi:.3f}"
print(a)
# f-Strings are evaluated at runtime, which allows expressions
a = f"The value is {2*60}"
print(a)

from timeit import default_timer as timer
my_list = ["a"] * 1000000

# bad
start = timer()
a = ""
for i in my_list:
    a += i
end = timer()
print("concatenate string with + : %.5f" % (end - start))

# good
start = timer()
a = "".join(my_list)
end = timer()
print("concatenate string with join(): %.5f" % (end - start))

"""Collection"""

from collections import Counter
a = "aaaaabbbbcccdde"
my_counter = Counter(a)
print(my_counter)

print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())

my_list = [0, 1, 0, 1, 2, 1, 1, 3, 2, 3, 2, 4]
my_counter = Counter(my_list)
print(my_counter)

# most common items
print(my_counter.most_common(1))

print(list(my_counter.elements()))

from collections import namedtuple
Point = namedtuple('Point','x, y')
pt = Point(1, -4)
print(pt)
print(pt._fields)
print(type(pt))
print(pt.x, pt.y)

Person = namedtuple('Person','name, age')
friend = Person(name='Tom', age=25)
print(friend.name, friend.age)

from collections import OrderedDict
ordinary_dict = {}
ordinary_dict['a'] = 1
ordinary_dict['b'] = 2
ordinary_dict['c'] = 3
ordinary_dict['d'] = 4
ordinary_dict['e'] = 5
# this may be in orbitrary order prior to Python 3.7
print(ordinary_dict)

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5
print(ordered_dict)
# same functionality as with ordinary dict, but always ordered
for k, v in ordinary_dict.items():
    print(k, v)

from collections import defaultdict

d = defaultdict(int)
d['yellow'] = 1
d['blue'] = 2
print(d.items())
print(d['green'])

# initialize with a default list value, i.e an empty list
d = defaultdict(list)
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 5)]
for k, v in s:
    d[k].append(v)

print(d.items())
print(d['green'])

from collections import deque
d = deque()

# append() : add elements to the right end 
d.append('a')
d.append('b')
print(d)

# appendleft() : add elements to the left end 
d.appendleft('c')
print(d)

# pop() : return and remove elements from the right
print(d.pop())
print(d)

# popleft() : return and remove elements from the left
print(d.popleft())
print(d)

# clear() : remove all elements
d.clear()
print(d)

d = deque(['a', 'b', 'c', 'd'])

# extend at right or left side
d.extend(['e', 'f', 'g'])
d.extendleft(['h', 'i', 'j']) # note that 'j' is now at the left most position
print(d)

# count(x) : returns the number of found elements
print(d.count('h'))

# rotate 1 positions to the right
d.rotate(1)
print(d)

# rotate 2 positions to the left
d.rotate(-2)
print(d)

"""Itertools"""

from itertools import product

prod = product([1, 2], [3, 4])
print(list(prod)) # note that we convert the iterator to a list for printing

# to allow the product of an iterable with itself, specify the number of repetitions 
prod = product([1, 2], [3], repeat=2)
print(list(prod))

from itertools import permutations

perm = permutations([1, 2, 3])
print(list(perm))

# optional: the length of the permutation tuples
perm = permutations([1, 2, 3], 2)
print(list(perm))

from itertools import combinations, combinations_with_replacement

# the second argument is mandatory and specifies the length of the output tuples.
comb = combinations([1, 2, 3, 4], 2)
print(list(comb))

comb = combinations_with_replacement([1, 2, 3, 4], 2)
print(list(comb))

from itertools import accumulate

# return accumulated sums
acc = accumulate([1,2,3,4])
print(list(acc))

# other possible functions are possible
import operator
acc = accumulate([1,2,3,4], func=operator.mul)
print(list(acc))

acc = accumulate([1,5,2,6,3,4], func=max)
print(list(acc))

from itertools import groupby

# use a function as key
def smaller_than_3(x):
    return x < 3

group_obj = groupby([1, 2, 3, 4], key=smaller_than_3)
for key, group in group_obj:
    print(key, list(group))
    
# or use a lamda expression, e.g. words with an 'i':
group_obj = groupby(["hi", "nice", "hello", "cool"], key=lambda x: "i" in x)
for key, group in group_obj:
    print(key, list(group))
    
persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, 
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

for key, group in groupby(persons, key=lambda x: x['age']):
    print(key, list(group))

from itertools import groupby

# use a function as key
def smaller_than_3(x):
    return x < 3

group_obj = groupby([1, 2, 3, 4], key=smaller_than_3)
for key, group in group_obj:
    print(key, list(group))
    
# or use a lamda expression, e.g. words with an 'i':
group_obj = groupby(["hi", "nice", "hello", "cool"], key=lambda x: "i" in x)
for key, group in group_obj:
    print(key, list(group))
    
persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, 
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

for key, group in groupby(persons, key=lambda x: x['age']):
    print(key, list(group))

from itertools import count, cycle, repeat
# count(x): count from x: x, x+1, x+2, x+3...
for i in count(10):
    print(i)
    if  i >= 13:
        break
# cycle(iterable) : cycle infinitely through an iterable
print("")
sum = 0
for i in cycle([1, 2, 3]):
    print(i)
    sum += i
    if sum >= 12:
        break
# repeat(x): repeat x infinitely or n times
print("")
for i in repeat("A", 3):
    print(i)

"""Lambda Function"""

# a lambda function that adds 10 to the input argument
f = lambda x: x+10
val1 = f(5)
val2 = f(100)
print(val1, val2)

# a lambda function that multiplies two input arguments and returns the result
f = lambda x,y: x*y
val3 = f(2,10)
val4 = f(7,5)
print(val3, val4)

def myfunc(n):
    return lambda x: x * n

doubler = myfunc(2)
print(doubler(6))

tripler = myfunc(3)
print(tripler(6))

points2D = [(1, 9), (4, 1), (5, -3), (10, 2)]
sorted_by_y = sorted(points2D, key= lambda x: x[1])
print(sorted_by_y)

mylist = [- 1, -4, -2, -3, 1, 2, 3, 4]
sorted_by_abs = sorted(mylist, key= lambda x: abs(x))
print(sorted_by_abs)

a  = [1, 2, 3, 4, 5, 6]
b = list(map(lambda x: x * 2 , a))

# However, try to prefer list comprehension
# Use map if you have an already defined function
c = [x*2 for x in a]
print(b)
print(c)

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = list(filter(lambda x: (x%2 == 0) , a))

# However, the same can be achieved with list comprehension
c = [x for x in a if x%2 == 0]
print(b)
print(c)

from functools import reduce
a = [1, 2, 3, 4]
product_a = reduce(lambda x, y: x*y, a)
print(product_a)
sum_a = reduce(lambda x, y: x+y, a)
print(sum_a)

"""Exceptions"""

try:
    a = 5 / 0
except:
    print('some error occured.')
    
# You can also catch the type of exception
try:
    a = 5 / 0
except Exception as e:
    print(e)
    
# It is good practice to specify the type of Exception you want to catch.
# Therefore, you have to know the possible errors
try:
    a = 5 / 0
except ZeroDivisionError:
    print('Only a ZeroDivisionError is handled here')
    
# You can run multiple statements in a try block, and catch different possible exceptions
try:
    a = 5 / 1 # Note: No ZeroDivisionError here
    b = a + '10'
except ZeroDivisionError as e:
    print('A ZeroDivisionError occured:', e)
except TypeError as e:
    print('A TypeError occured:', e)

try:
    a = 5 / 1
except ZeroDivisionError as e:
    print('A ZeroDivisionError occured:', e)
else:
    print('Everything is ok')

try:
    a = 5 / 1 # Note: No ZeroDivisionError here
    b = a + '10'
except ZeroDivisionError as e:
    print('A ZeroDivisionError occured:', e)
except TypeError as e:
    print('A TypeError occured:', e)
else:
    print('Everything is ok')
finally:
    print('Cleaning up some stuff...')

# minimal example for own exception class
class ValueTooHighError(Exception):
    pass

# or add some more information for handlers
class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(a):
    if a > 1000:
        raise ValueTooHighError('Value is too high.')
    if a < 5:
        raise ValueTooLowError('Value is too low.', a) # Note that the constructor takes 2 arguments here
    return a

try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e.message, 'The value is:', e.value)

"""Logging"""

import logging
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
# Now also debug messages will get logged with a different format.
logging.debug('Debug message')

import logging
logger = logging.getLogger(__name__)
logger.info('HELLO')

import logging
logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')
import helper

import logging
logger = logging.getLogger(__name__)
logger.propagate = False
logger.info('HELLO')

import logging
logging.basicConfig(level=logging.INFO, format='%(name)s - %(levelname)s - %(message)s')
import helper

import logging

logger = logging.getLogger(__name__)

# Create handlers
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file.log')

# Configure level and formatter and add it to handlers
stream_handler.setLevel(logging.WARNING) # warning and above is logged to the stream
file_handler.setLevel(logging.ERROR) # error and above is logged to a file

stream_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(stream_format)
file_handler.setFormatter(file_format)

# Add handlers to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.warning('This is a warning') # logged to the stream
logger.error('This is an error')

class InfoFilter(logging.Filter):
    
    # overwrite this method. Only log records for which this
    # function evaluates to True will pass the filter.
    def filter(self, record):
        return record.levelno == logging.INFO

# Now only INFO level messages will be logged
stream_handler.addFilter(InfoFilter())
logger.addHandler(stream_handler)

# logging.conf
[loggers]
keys=root,simpleExample

[handlers]
keys=consoleHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_simpleExample]
level=DEBUG
handlers=consoleHandler
qualname=simpleExample
propagate=0

[handler_consoleHandler]
class= StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s

# Then use the config file in the code
import logging
import logging.config

logging.config.fileConfig('logging.conf')

# create logger with the name from the config file. 
# This logger now has StreamHandler with DEBUG Level and the specified format
logger = logging.getLogger('simpleExample')

logger.debug('debug message')
logger.info('info message')

import logging

try:
    a = [1, 2, 3]
    value = a[3]
except IndexError as e:
    logging.error(e)
    logging.error(e, exc_info=True)

import logging
import traceback

try:
    a = [1, 2, 3]
    value = a[3]
except:
    logging.error("uncaught exception: %s", traceback.format_exc())

import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over after 2KB, and keep backup logs app.log.1, app.log.2 , etc.
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info('Hello, world!')

import logging
import time
from logging.handlers import TimedRotatingFileHandler
 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# This will create a new log file every minute, and 5 backup files with a timestamp before overwriting old logs.
handler = TimedRotatingFileHandler('timed_test.log', when='m', interval=1, backupCount=5)
logger.addHandler(handler)
 
for i in range(6):
    logger.info('Hello, world!')
    time.sleep(50)

import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger()

logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

"""JSON"""

{
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "swimming", "singing"],
    "age": 28,
    "children": [
        {
            "firstName": "Alex",
            "age": 5
        },
        {
            "firstName": "Bob",
            "age": 7
        }
    ]
}

import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# convert into JSON:
person_json = json.dumps(person)
# use different formatting style
person_json2 = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True)

# the result is a JSON string:
print(person_json) 
print(person_json2)

import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

with open('person.json', 'w') as f:
    json.dump(person, f)

import json
person_json = """
{
    "age": 30, 
    "city": "New York",
    "hasChildren": false, 
    "name": "John",
    "titles": [
        "engineer",
        "programmer"
    ]
}
"""
person = json.loads(person_json)
print(person)

import json

with open('person.json', 'r') as f:
    person = json.load(f)
    print(person)

import json
def encode_complex(z):
    if isinstance(z, complex):
        # just the key of the class name is important, the value can be arbitrary.
        return {z.__class__.__name__: True, "real":z.real, "imag":z.imag}
    else:
        raise TypeError(f"Object of type '{z.__class__.__name__}' is not JSON serializable")

z = 5 + 9j
zJSON = json.dumps(z, default=encode_complex)
print(zJSON)

from json import JSONEncoder
class ComplexEncoder(JSONEncoder):
    
    def default(self, o):
        if isinstance(z, complex):
            return {z.__class__.__name__: True, "real":z.real, "imag":z.imag}
        # Let the base class default method handle other objects or raise a TypeError
        return JSONEncoder.default(self, o)
    
z = 5 + 9j
zJSON = json.dumps(z, cls=ComplexEncoder)
print(zJSON)
# or use encoder directly:
zJson = ComplexEncoder().encode(z)
print(zJSON)

# Possible but decoded as a dictionary
z = json.loads(zJSON)
print(type(z))
print(z)

def decode_complex(dct):
    if complex.__name__ in dct:
        return complex(dct["real"], dct["imag"])
    return dct

# Now the object is of type complex after decoding
z = json.loads(zJSON, object_hook=decode_complex)
print(type(z))
print(z)

class User:
    # Custom class with all instance variables given in the __init__()
    def __init__(self, name, age, active, balance, friends):
        self.name = name
        self.age = age
        self.active = active
        self.balance = balance
        self.friends = friends
        
class Player:
    # Other custom class
    def __init__(self, name, nickname, level):
        self.name = name
        self.nickname = nickname
        self.level = level
          
            
def encode_obj(obj):
    """
    Takes in a custom object and returns a dictionary representation of the object.
    This dict representation also includes the object's module and class names.
    """
  
    #  Populate the dictionary with object meta data 
    obj_dict = {
      "__class__": obj.__class__.__name__,
      "__module__": obj.__module__
    }
  
    #  Populate the dictionary with object properties
    obj_dict.update(obj.__dict__)
  
    return obj_dict


def decode_dct(dct):
    """
    Takes in a dict and returns a custom object associated with the dict.
    It makes use of the "__module__" and "__class__" metadata in the dictionary
    to know which object type to create.
    """
    if "__class__" in dct:
        # Pop ensures we remove metadata from the dict to leave only the instance arguments
        class_name = dct.pop("__class__")
        
        # Get the module name from the dict and import it
        module_name = dct.pop("__module__")
        
        # We use the built in __import__ function since the module name is not yet known at runtime
        module = __import__(module_name)
        
        # Get the class from the module
        class_ = getattr(module,class_name)

        # Use dictionary unpacking to initialize the object
        # Note: This only works if all __init__() arguments of the class are exactly the dict keys
        obj = class_(**dct)
    else:
        obj = dct
    return obj

# User class works with our encoding and decoding methods
user = User(name = "John",age = 28, friends = ["Jane", "Tom"], balance = 20.70, active = True)

userJSON = json.dumps(user,default=encode_obj,indent=4, sort_keys=True)
print(userJSON)

user_decoded = json.loads(userJSON, object_hook=decode_dct)
print(type(user_decoded))

# Player class also works with our custom encoding and decoding
player = Player('Max', 'max1234', 5)
playerJSON = json.dumps(player,default=encode_obj,indent=4, sort_keys=True)
print(playerJSON)

player_decoded = json.loads(playerJSON, object_hook=decode_dct)
print(type(player_decoded))

"""Random Numbers"""

import random

# random float in [0,1)
a = random.random()
print(a)

# random float in range [a,b]
a = random.uniform(1,10)
print(a)

# random integer in range [a,b]. b is included
a = random.randint(1,10)
print(a)

# random integer in range [a,b). b is excluded
a = random.randrange(1,10)
print(a)

# random float from a normal distribution with mu and sigma
a = random.normalvariate(0, 1)
print(a)

# choose a random element from a sequence
a = random.choice(list("ABCDEFGHI"))
print(a)

# choose k unique random elements from a sequence
a = random.sample(list("ABCDEFGHI"), 3)
print(a)

# choose k elements with replacement, and return k sized list
a = random.choices(list("ABCDEFGHI"),k=3)
print(a)

# shuffle list in place
a = list("ABCDEFGHI")
random.shuffle(a)
print(a)

print('Seeding with 1...\n')

random.seed(1)
print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))

print('\nRe-seeding with 42...\n')
random.seed(42)  # Re-seed

print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))

print('\nRe-seeding with 1...\n')
random.seed(1)  # Re-seed

print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))

print('\nRe-seeding with 42...\n')
random.seed(42)  # Re-seed

print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))

import secrets

# random integer in range [0, n).
a = secrets.randbelow(10)
print(a)

# return an integer with k random bits.
a = secrets.randbits(5)
print(a)

# choose a random element from a sequence
a = secrets.choice(list("ABCDEFGHI"))
print(a)

import numpy as np

np.random.seed(1)
# rand(d0,d1,…,dn)
# generate nd array with random floats, arrays has size (d0,d1,…,dn)
print(np.random.rand(3))
# reset the seed
np.random.seed(1)
print(np.random.rand(3))

# generate nd array with random integers in range [a,b) with size n
values = np.random.randint(0, 10, (5,3))
print(values)

# generate nd array with Gaussian values, array has size (d0,d1,…,dn)
# values from standard normal distribution with mean 0.0 and standard deviation 1.0
values = np.random.randn(5)
print(values)

# randomly shuffle a nd array.
# only shuffles the array along the first axis of a multi-dimensional array
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
np.random.shuffle(arr)
print(arr)

"""Decorators"""

def start_end_decorator(func):
    
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper

def print_name():
    print('Alex')
    
print_name()

print()

# Now wrap the function by passing it as argument to the decorator function
# and asign it to itself -> Our function has extended behaviour!
print_name = start_end_decorator(print_name)
print_name()

@start_end_decorator
def print_name():
    print('Alex')
    
print_name()

def start_end_decorator_2(func):
    
    def wrapper(*args, **kwargs):
        print('Start')
        func(*args, **kwargs)
        print('End')
    return wrapper

@start_end_decorator_2
def add_5(x):
    return x + 5

result = add_5(10)
print(result)

def start_end_decorator_3(func):
    
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator_3
def add_5(x):
    return x + 5

result = add_5(10)
print(result)

print(add_5.__name__)
help(add_5)

import functools
def start_end_decorator_4(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator_4
def add_5(x):
    return x + 5
result = add_5(10)
print(result)
print(add_5.__name__)
help(add_5)

import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result
    return wrapper

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")
    
greet('Alex')

# a decorator function that prints debug information about the wrapped function
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

@debug
@start_end_decorator_4
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

# now `debug` is executed first and calls `@start_end_decorator_4`, which then calls `say_hello`
say_hello(name='Alex')

import functools

class CountCalls:
    # the init needs to have the func as argument and stores it
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0
    
    # extend functionality, execute function, and return the result
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello(num):
    print("Hello!")
    
say_hello(5)
say_hello(5)

"""Generators"""

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

# this will not print 'Starting'
cd = countdown(3)

# this will print 'Starting' and the first value
print(next(cd))

# will print the next values
print(next(cd))
print(next(cd))

# this will raise a StopIteration
print(next(cd))

# you can iterate over a generator object with a for in loop
cd = countdown(3)
for x in cd:
    print(x)

# you can use it for functions that take iterables as input
cd = countdown(3)
sum_cd = sum(cd)
print(sum_cd)

cd = countdown(3)
sorted_cd = sorted(cd)
print(sorted_cd)

# without a generator, the complete sequence has to be stored here in a list
def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)
import sys
print(sys.getsizeof(firstn(1000000)), "bytes")

# with a generator, no additional sequence is needed to store the numbers
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)
import sys
print(sys.getsizeof(firstn(1000000)), "bytes")

def fibonacci(limit):
    a, b = 0, 1 # first two fibonacci numbers
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)
# generator objects can be converted to a list (only used for printing here)
print(list(fib))

# generator expression
mygenerator = (i for i in range(1000) if i % 2 == 0)
print(sys.getsizeof(mygenerator))

# list comprehension
mylist = [i for i in range(1000) if i % 2 == 0]
print(sys.getsizeof(mylist))

class firstn:
    def __init__(self, n):
        self.n = n
        self.num = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num < self.n:
            cur = self.num
            self.num += 1
            return cur
        else:
            raise StopIteration()
             
firstn_object = firstn(1000000)
print(sum(firstn_object))

"""Threading v/s Multiprocessing"""

from threading import Thread

def square_numbers():
    for i in range(1000):
        result = i * i

        
if __name__ == "__main__":        
    threads = []
    num_threads = 10

    # create threads and asign a function for each thread
    for i in range(num_threads):
        thread = Thread(target=square_numbers)
        threads.append(thread)

    # start all threads
    for thread in threads:
        thread.start()

    # wait for all threads to finish
    # block the main thread until these threads are finished
    for thread in threads:
        thread.join()

from multiprocessing import Process
import os


def square_numbers():
    for i in range(1000):
        result = i * i


if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count()

    # create processes and asign a function for each process
    for i in range(num_processes):
        process = Process(target=square_numbers)
        processes.append(process)

    # start all processes
    for process in processes:
        process.start()

    # wait for all processes to finish
    # block the main thread until these processes are finished
    for process in processes:
        process.join()

"""Threading in Python"""

from threading import Thread

def square_numbers():
    for i in range(1000):
        result = i * i

        
if __name__ == "__main__":        
    threads = []
    num_threads = 10

    # create threads and asign a function for each thread
    for i in range(num_threads):
        thread = Thread(target=square_numbers)
        threads.append(thread)

    # start all threads
    for thread in threads:
        thread.start()

    # wait for all threads to finish
    # block the main thread until these threads are finished
    for thread in threads:
        thread.join()

from threading import Thread
import time


# all threads can access this global variable
database_value = 0

def increase():
    global database_value # needed to modify the global value
    
    # get a local copy (simulate data retrieving)
    local_copy = database_value
        
    # simulate some modifying operation
    local_copy += 1
    time.sleep(0.1)
        
    # write the calculated new value into the global variable
    database_value = local_copy


if __name__ == "__main__":

    print('Start value: ', database_value)

    t1 = Thread(target=increase)
    t2 = Thread(target=increase)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('End value:', database_value)

    print('end main')

# import Lock
from threading import Thread, Lock
import time


database_value = 0

def increase(lock):
    global database_value 
    
    # lock the state
    lock.acquire()
    
    local_copy = database_value
    local_copy += 1
    time.sleep(0.1)
    database_value = local_copy
    
    # unlock the state
    lock.release()


if __name__ == "__main__":

    # create a lock
    lock = Lock()
    
    print('Start value: ', database_value)

    # pass the lock to the target function
    t1 = Thread(target=increase, args=(lock,)) # notice the comma after lock since args must be a tuple
    t2 = Thread(target=increase, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('End value:', database_value)

    print('end main')

def increase(lock):
    global database_value 
    
    with lock: 
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy

from queue import Queue

# create queue
q = Queue()

# add elements
q.put(1) # 1
q.put(2) # 2 1
q.put(3) # 3 2 1 

# now q looks like this:
# back --> 3 2 1 --> front

# get and remove first element
first = q.get() # --> 1
print(first)

from threading import Thread, Lock, current_thread
from queue import Queue

def worker(q, lock):
    while True:
        value = q.get()  # blocks until the item is available

        # do stuff...
        with lock:
            # prevent printing at the same time with this lock
            print(f"in {current_thread().name} got {value}")
        # ...

        # For each get(), a subsequent call to task_done() tells the queue
        # that the processing on this item is complete.
        # If all tasks are done, q.join() can unblock
        q.task_done()


if __name__ == '__main__':
    q = Queue()
    num_threads = 10
    lock = Lock()

    for i in range(num_threads):
        t = Thread(name=f"Thread{i+1}", target=worker, args=(q, lock))
        t.daemon = True  # dies when the main thread dies
        t.start()
    
    # fill the queue with items
    for x in range(20):
        q.put(x)

    q.join()  # Blocks until all items in the queue have been gotten and processed.

    print('main done')

"""Multiprocessing"""

from multiprocessing import Process
import os

def square_numbers():
    for i in range(1000):
        result = i * i

        
if __name__ == "__main__":        
    processes = []
    num_processes = os.cpu_count()
    # number of CPUs on the machine. Usually a good choise for the number of processes

    # create processes and asign a function for each process
    for i in range(num_processes):
        process = Process(target=square_numbers)
        processes.append(process)

    # start all processes
    for process in processes:
        process.start()

    # wait for all processes to finish
    # block the main programm until these processes are finished
    for process in processes:
        process.join()

from multiprocessing import Process, Value, Array
import time

def add_100(number):
    for _ in range(100):
        time.sleep(0.01)
        number.value += 1

def add_100_array(numbers):
    for _ in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            numbers[i] += 1


if __name__ == "__main__":

    shared_number = Value('i', 0) 
    print('Value at beginning:', shared_number.value)

    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('Array at beginning:', shared_array[:])

    process1 = Process(target=add_100, args=(shared_number,))
    process2 = Process(target=add_100, args=(shared_number,))

    process3 = Process(target=add_100_array, args=(shared_array,))
    process4 = Process(target=add_100_array, args=(shared_array,))

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()

    print('Value at end:', shared_number.value)
    print('Array at end:', shared_array[:])

    print('end main')

# import Lock
from multiprocessing import Lock
from multiprocessing import Process, Value, Array
import time

def add_100(number, lock):
    for _ in range(100):
        time.sleep(0.01)
        # lock the state
        lock.acquire()
        
        number.value += 1
        
        # unlock the state
        lock.release()

def add_100_array(numbers, lock):
    for _ in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            lock.acquire()
            numbers[i] += 1
            lock.release()


if __name__ == "__main__":

    # create a lock
    lock = Lock()
    
    shared_number = Value('i', 0) 
    print('Value at beginning:', shared_number.value)

    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('Array at beginning:', shared_array[:])

    # pass the lock to the target function
    process1 = Process(target=add_100, args=(shared_number, lock))
    process2 = Process(target=add_100, args=(shared_number, lock))

    process3 = Process(target=add_100_array, args=(shared_array, lock))
    process4 = Process(target=add_100_array, args=(shared_array, lock))

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()

    print('Value at end:', shared_number.value)
    print('Array at end:', shared_array[:])

    print('end main')

def add_100(number, lock):
    for _ in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1

from multiprocessing import Queue

# create queue
q = Queue()

# add elements
q.put(1) # 1
q.put(2) # 2 1
q.put(3) # 3 2 1 

# get and remove first element
first = q.get() # --> 1
print(first)

from multiprocessing import Process, Queue

def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)

def make_negative(numbers, queue):
    for i in numbers:
        queue.put(i*-1)

if __name__ == "__main__":
    
    numbers = range(1, 6)
    q = Queue()

    p1 = Process(target=square, args=(numbers,q))
    p2 = Process(target=make_negative, args=(numbers,q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # order might not be sequential
    while not q.empty():
        print(q.get())
        
    print('end main')

from multiprocessing import Pool 
def cube(number):
    return number * number * number
    
if __name__ == "__main__":
    numbers = range(10)    
    p = Pool()
    result = p.map(cube,  numbers)   
    p.close()
    p.join()   
    print(result)

"""Function Argument"""

def print_name(name): # name is the parameter
    print(name)

print_name('Prateek') # 'Prateek' is the argument

def foo(a, b, c):
    print(a, b, c)
    
# positional arguments
foo(1, 2, 3)

# keyword arguments
foo(a=1, b=2, c=3)
foo(c=3, b=2, a=1) # Note that the order is not important here

# mix of both
foo(1, b=2, c=3)

# default arguments
def foo(a, b, c, d=4):
    print(a, b, c, d)

foo(1, 2, 3, 4)
foo(1, b=2, c=3, d=100)

def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg, kwargs[kwarg])

foo(1, 2, 3, 4, 5, six=6, seven=7)
print()

# omitting of args or kwargs is also possible
foo(1, 2, three=3)

def foo(a, b, *, c, d):
    print(a, b, c, d)

foo(1, 2, c=3, d=4)

# arguments after variable-length arguments must be keyword arguments
def foo(*args, last):
    for arg in args:
        print(arg)
    print(last)

foo(8, 9, 10, last=50)

def foo(a, b, c):
    print(a, b, c)


# list/tuple unpacking, length must match
my_list = [4, 5, 6] # or tuple
foo(*my_list)

# dict unpacking, keys and length must match
my_dict = {'a': 1, 'b': 2, 'c': 3}
foo(**my_dict)

def foo1():
    x = number # global variable can only be accessed here
    print('number in function:', x)

number = 0
foo1()

# modifying the global variable
def foo2():
    global number # global variable can now be accessed and modified
    number = 3

print('number before foo2(): ', number)
foo2() # modifies the global variable
print('number after foo2(): ', number)

number = 0

def foo3():
    number = 3 # this is a local variable

print('number before foo3(): ', number)
foo3() # does not modify the global variable
print('number after foo3(): ', number)

def foo(x):
    x = 5 # x += 5 also no effect since x is immutable and a new variable must be created

var = 10
print('var before foo():', var)
foo(var)
print('var after foo():', var)

def foo(a_list):
    a_list.append(4)
    
my_list = [1, 2, 3]
print('my_list before foo():', my_list)
foo(my_list)
print('my_list after foo():', my_list)

def foo(a_list):
    a_list[0] = -100
    a_list[2] = "Paul"
    
my_list = [1, 2, "Max"]
print('my_list before foo():', my_list)
foo(my_list)
print('my_list after foo():', my_list)

def foo(a_list):
    a_list = [50, 60, 70] # a_list is now a new local variable within the function
    a_list.append(50)
    
my_list = [1, 2, 3]
print('my_list before foo():', my_list)
foo(my_list)
print('my_list after foo():', my_list)

def foo(a_list):
    a_list += [4, 5] # this chanches the outer variable
    
def bar(a_list):
    a_list = a_list + [4, 5] # this rebinds the reference to a new local variable

my_list = [1, 2, 3]
print('my_list before foo():', my_list)
foo(my_list)
print('my_list after foo():', my_list)

my_list = [1, 2, 3]
print('my_list before bar():', my_list)
bar(my_list)
print('my_list after bar():', my_list)

"""Copying"""

list_a = [1, 2, 3, 4, 5]
list_b = list_a

list_a[0] = -10
print(list_a)
print(list_b)

import copy
list_a = [1, 2, 3, 4, 5]
list_b = copy.copy(list_a)

# not affects the other list
list_b[0] = -10
print(list_a)
print(list_b)

import copy
list_a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
list_b = copy.copy(list_a)

# affects the other!
list_a[0][0]= -10
print(list_a)
print(list_b)

# shallow copies
list_b = list(list_a)
list_b = list_a[:]
list_b = list_a.copy()

import copy
list_a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
list_b = copy.deepcopy(list_a)

# not affects the other
list_a[0][0]= -10
print(list_a)
print(list_b)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
                
# Only copies the reference
p1 = Person('Alex', 27)
p2 = p1
p2.age = 28
print(p1.age)
print(p2.age)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
                
# Only copies the reference
p1 = Person('Alex', 27)
p2 = p1
p2.age = 28
print(p1.age)
print(p2.age)

import copy
p1 = Person('Alex', 27)
p2 = copy.copy(p1)
p2.age = 28
print(p1.age)
print(p2.age)

class Company:
    def __init__(self, boss, employee):
        self. boss = boss
        self.employee = employee

# shallow copy will affect nested objects
boss = Person('Jane', 55)
employee = Person('Joe', 28)
company = Company(boss, employee)

company_clone = copy.copy(company)
company_clone.boss.age = 56
print(company.boss.age)
print(company_clone.boss.age)

print()
# deep copy will not affect nested objects
boss = Person('Jane', 55)
employee = Person('Joe', 28)
company = Company(boss, employee)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 56
print(company.boss.age)
print(company_clone.boss.age)

"""Context Manager"""

with open('notes.txt', 'w') as f:
    f.write('some todo...')

f = open('notes.txt', 'w')
try:
    f.write('some todo...')
finally:
    f.close()

class ManagedFile:
    def __init__(self, filename):
        print('init', filename)
        self.filename = filename
        
    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        print('exit')
            
with ManagedFile('notes.txt') as f:
    print('doing stuff...')
    f.write('some todo...')

class ManagedFile:
    def __init__(self, filename):
        print('init', filename)
        self.filename = filename
        
    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        print('exc:', exc_type, exc_value)
        print('exit')

# No exception
with ManagedFile('notes.txt') as f:
    print('doing stuff...')
    f.write('some todo...')
print('continuing...')

print()

# Exception is raised, but the file can still be closed
with ManagedFile('notes2.txt') as f:
    print('doing stuff...')
    f.write('some todo...')
    f.do_something()
print('continuing...')

class ManagedFile:
    def __init__(self, filename):
        print('init', filename)
        self.filename = filename
        
    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('Exception has been handled')
        print('exit')
        return True


with ManagedFile('notes2.txt') as f:
    print('doing stuff...')
    f.write('some todo...')
    f.do_something()
print('continuing...')

from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()
        
with open_managed_file('notes.txt') as f:
    f.write('some todo...')

"""Python Tricks

- Value Swapping
"""

a, b = 5, 10
print(a, b)
a, b = b, a
print(a, b)
# also possible in a list
myList = [1, 2, 3, 4, 5]
print("Initial list :", myList)
myList[0], myList[1] = myList[1], myList[0]
print("Modified list:", myList)

"""- Create a single string from list"""

my_list = ["Prateek", "is","a", "AI Developer"]

# bad
a = ""
for i in my_list:
    a += i + " "
print(a)

# good
a = " ".join(my_list)
print(a)

# join method is much faster
from timeit import default_timer as timer
my_list = ["a"] * 1000000

# bad
start = timer()
a = ""
for i in my_list:
    a += i
end = timer()
print(end - start)
#print(a)

# good
start = timer()
a = " ".join(my_list)
end = timer()
print(end - start)
#print(a)

