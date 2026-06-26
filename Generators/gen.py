# Python generators are simple way of creating Iterators.

# benefits :
#     Ease of Implementations
#     MemoryEfficient
#     representing Infinite Streams


# python generator is nothing but it is a function
# a)
def geb_deno():

    yield "First Statement"
    yield "Second Statement"
    yield ("Third Statement")

gen = geb_deno()

print(next(gen))
print(next(gen))
print(next(gen))

# so here we create a function and we access the values in yeild instead of return

# diff between yeild and return :

# b)
def square(num):
    for i in range(1,num+1):
        yield i**2

gen2 = square(10)
print(next(gen2))
print(next(gen2))

# here we will get the values but the diff is yeild is a clever, we printed
# already two values of square if we use loop to print then it will never goes to
# starting point it will check which values he has printed and then it will print ahead
# from that point

for i in gen2:
    print(i)

# from the output we see that it does not printed repeated values

# now we will look how to create range functions we already done it in iterators
# but how it will be in generators, we will see that:

def self_range_func(start, end):
    for i in range(start, end):
        yield  i

for i in self_range_func(10, 20):
    print(i)

# here is the simple way we can genrate the functio like range square
# and many functions

# generator Expression:
# we have to print the squres of number
# in list comprehension
L = [i ** 2 for i in range(1,11)]

for i in L:
    print(i)

# but in generator
# output must be same but its a generator expression
# we dont have to create function for it and also it calls anonymos function
# we can dirctly use it
gen = (i ** 2 for i in range(1,11))

for i in gen:
    print(i)

