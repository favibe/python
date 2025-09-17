#Iterators in Python
"""An iterator in Python is an object used to traverse through all the elements of a collection 
(like lists, tuples or dictionaries) one element at a time. It follows the iterator protocol, 
which involves two key methods:

__iter__(): Returns the iterator object itself.
__next__(): Returns the next value from the sequence. Raises StopIteration when the sequence ends."""

s = "GFG"
it = iter(s)

print(next(it)) #G
print(next(it)) #F
print(next(it)) #G

#Creating a Custom Iterator
"""Creating a custom iterator in Python involves defining a class that implements 
the __iter__() and __next__() methods according to the Python iterator protocol."""
class EvenNumbers:
    def __iter__(self):
        self.n = 2 #start from the first even number
        return self
    
    def __next__(self):
        x = self.n
        self .n += 2 #Increment by 2 to get the next even number
        return x
    
#Create an instance of EvenInstance
even = EvenNumbers()
it = iter(even)

#print the first  five even  number
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

#StopIteration Exception
"""StopIteration exception is integrated with Python's iterator protocol. 
It signals that the iterator has no more items to return. Once this exception 
is raised, further calls to next() on the same iterator will continue raising StopIteration."""
li = [100, 200, 300]
it = iter(li)

# Iterate until StopIteration is raised
while True:
    try:
        print(next(it))
    except StopIteration:
        print("End of iteration")
        break

#Difference between Iterator and Iterable
"""Although the terms iterator and iterable sound similar, they are not the same.
 An iterable is any object that can return an iterator, 
 while an iterator is the actual object that performs iteration one element at a time."""
# Iterable: list
numbers = [1, 2, 3]

# Iterator: created using iter()
it = iter(numbers)
print(next(it)) 
print(next(it))  
print(next(it))