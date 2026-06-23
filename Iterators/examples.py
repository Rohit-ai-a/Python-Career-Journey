"""
Day 2 - Iterables and Iterators

Topics Covered:
1. Memory usage: List vs Range
2. Iterable vs Iterator
3. iter() and next()
4. Internal working of for loops
5. Custom implementation of a for loop
6. Iterator identity: iter(iterator)
7. Custom implementation of range()
"""

# Iteartion is a term of taking each item of something one after another.
import sys
#
num = [1,2,3,4,5]
for i in num:
    print(i)

# Special thing about an Iterator is it never stored entire data in the memory.
# eg:

L = [x for x in range(1,1000000)]
print(sys.getsizeof(L)/1024)
#
# If we use a iterator with same task
X = range(1,1000000)
print(sys.getsizeof(X)/1024)
# We see diff outputs with the impact of iterations in programming language.

# How we can check wheather the ibject is itrable or not ?
# we have two wways to checks the object is iterable or not:
# a) By using for loop
a = 2
for i in a:
    print(i) # TypeError: 'int' object is not iterable

# b) by usnig dir() method
b = [12,3,4,5,]
print(dir(b))
# in output we can see the '__iter__', which means it is an iterable object.
# If not then the object is not iterable.

# How will we know the object is iterator or not ?
# a) same by using directory '__next__' this helps us to know the obj is iterator or not
#     but twist is we have to user iter function with the help of it creates in memory.
J = [1,2,3,4,5]
print(dir(iter(J)))

# How Loops works:
num = [1,2,3]
# here is the simple code-snippet of loops working
for i in num:
    print(i)

# but Actually
# for loops follows iter() function to execute the for loop
# until it gets the Stop Iterataion error.
num1 = [1,2,3]
iter_num = iter(num)
print(next(iter_num)) #  to fetch first index value
print(next(iter_num)) # same for second index value
print(next(iter_num)) # same for third one
# print(next(iter_num)) # but here it will gie an error cause we have only three arguments.


# How we can create our own for loop
def self_created_for_loop(iterable):
    iterator = iter(iterable)

    while True:
        try:
            ele = next(iterator)
            print(ele)
        except StopIteration:
            break

# this is how we can iterates every object.
a = [1,2,3,4,5]
b = {1,2,3,4,5}
c = (1,2,3,4,5)
d = {1:0,2:2}
e = range(1,11)
self_created_for_loop(a)
self_created_for_loop(b)
self_created_for_loop(c)
self_created_for_loop(d)
self_created_for_loop(e)

# This is how we can create aour own for loop function


#  A Confusing Point:
num =[1,2,3,4]
iter_obj = iter(num)

print(id(iter_obj), end = ' The address of Iterator 1')

iter_obj2 = iter(iter_obj)
print(id(iter_obj2), end = ' The address of Iterator 2')

# what we did we create an obj and we creating a iterator to follow the loop and then we created
# a another iterator of the first one iterator,
# We expecting the addresss should be diff but iterrator following Iterotor to execute the Itearation.
# It nwver created another object. That means Gangadhar hii shaktiman hai 🥲🥲
# We saw the bothe object memory address is same


# Also We cam create a Range function mechanism
class self_created_range:

    def __init__(self,start,end):
        self.start= start
        self.end= end

    def __iter__(self):
        return self_created_range_iterator(self)

class self_created_range_iterator:
    # what is the work of this class is:
        # the given range of starting and ending between generating values one by one.

    def __init__(self,iterable_obj):
        self.iterable = iterable_obj

    def __iter__(self):
        # if you run iteratot on iter it will return self
        return self

    def __next__(self):

        if self.iterable.start >= self.iterable.end:
            raise StopIteration

        current = self.iterable.start
        self.iterable.start+=1
        return current

for i in self_created_range(1,11):
    print(i)