from collections import Counter 
#Create a  counter from a list, string, dict, (any iterable)
ctr1 = Counter([1,2,3,4,5,6,2,1,2,3])
ctr2 = Counter({1:3, 2:2, 3:1})
ctr3 = Counter("Hello")
print(ctr1)
print(ctr2)
print(ctr3)
#Acessing  Counter Elements
print(ctr1[1]) # 2
print(ctr1[22]) #elemnt not present > 0
#Updating conuter
ctr4 = Counter([1,2,2])
#Adding new elemnt
ctr4.update([2,3,3,3])
print(ctr4)
#Counter Methods
#elements 
"""Returns an iterator over elements, repeating each element as many times as its count.
Order is not guaranteed (depends on insertion)"""
ctr1 = Counter([1,2,3,4,5,6,2,1,2,3])
items  = list(ctr1.elements())
print(f"print the element order for {ctr1} using element method : {items}")
#most_common()
c = Counter("banana")
print(c)
# Counter({'a': 3, 'n': 2, 'b': 1})
print(c.most_common())    # all in descending order
# [('a', 3), ('n', 2), ('b', 1)]
print(c.most_common(1))   # only the top 1
# [('a', 3)]
common = ctr1.most_common(2)
print(f"most common in {ctr1} is {common}")
#subtract
"""Subtracts counts from another iterable or mapping.
Counts can go negative."""
c = Counter(a=4, b=2, c=0)
c.subtract({'a': 2, 'b': 3, 'c': 1})
print(c)
# Counter({'a': 2, 'c': -1, 'b': -1})
#ex2 on subtract
ctr = Counter([1, 2, 2, 3, 3, 3])
ctr.subtract([2, 3, 3])
print(ctr)
#Arithmetic Operations on Count
"""Counters support addition, subtraction, intersection union operations, 
allowing for various arithmetic operations."""
ctr5 = Counter([1,2,2,3])
ctr6 = Counter([2,3,3,4])
print(ctr5 +ctr6)
print(ctr5 - ctr6)
print(ctr5 | ctr6)#union(Takes the maximum of counts for each key.) =only keys that exist in both counters are kept.
print(ctr5 & ctr6) #Intersection(Takes the minimum of counts for each key)=Here, all keys from both counters are kept.
"""Key Difference
Intersection (&) → only keys in both, counts = min
Union (|) → all keys, counts = max"""
#OrderedDict in Python
#from collections import OrderedDict
print("---OrderedDict---")
from collections import OrderedDict
od = OrderedDict()
od['apple'] = 2 #like key['apple] value =2
od['banana'] = 2
od['cherry'] = 3
print(list(od.items()))
print("Comparing with dict though py 3.7 updward comed in order of created")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
for key, val in d.items():
    print(key, val)

print("ordered dict compared")
od = OrderedDict()
od['d'] = 4
od['b'] = 2
od['a'] = 1
od['c'] = 3
for key, val in od.items():
    print(key, val)
#changing value does not affect order
od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
od['c'] = 5  
for k, v in od.items():
    print(k, v)
#Equality Check
od1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od2 = OrderedDict([('c', 3), ('b', 2), ('a', 1)])
print(od1 == od2)
#reverse
d1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
d2 = OrderedDict(reversed(list(d1.items())))
for k, v in d2.items():
    print(k, v)
#pop last or first item
d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
res = d.popitem(last=True)  # Remove last inserted item
print(res)
# move_to_end
d = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

d.move_to_end('a')         # Move 'a' to end
d.move_to_end('b', last=False)  # Move 'b' to front

for k, v in d.items():
    print(k, v)
# deleting re-inserting key
od.pop('c')    # Delete 'c'

for k, v in od.items():
    print(k, v)

od['c'] = 3    # Re-insert 'c' at end
for k, v in od.items():
    print(k, v)
#more OrderedDict practice
d = OrderedDict()
d["cake"] = 3
d["Ballons"] = 20
d["drinks"] = 23
print(d)
print(list(d.items()))
#using for loop (NOTICE THE.items() for printiong)
for k,v in d.items():
    print(k,v)
d2 = OrderedDict([("cake", 3), ("drinks",23),("Ballons",20)])
d3 = OrderedDict([("cake", 3),("Ballons", 20), ("drinks",23)])
#equality check( now d3 will be fslse in orderedDict cause order must be same, but in normal dict woold be True)
print(d == d2)
print(d==d3)
#changing value does ot affect the order of creation
d2["Ballons"] = 33
print(f"the value of {d2} didn't change")
d2.move_to_end("cake") #move cake to end
d2.move_to_end("Ballons", last=False)  # move ballons to front
print(d2)
#can reverse order of creation
d4 =OrderedDict(reversed(list(d3.items())))
for k,v in d4.items():
    print(k,v)
#popitem
pops = d4.popitem(last=True) #Pop last item. IF False pop first item
print(pops) #code removes and return the last item
# Deleting and re-inserting keys
d3.pop("Ballons") # delecte/remobve like popitem
print(d3)
d3['Ballons'] = 30 #reinsert it
print(d3)

print("____--DefaultDict Here..--____")
#DefaultDict
"""In Python, defaultdict is a subclass of the built-in dict class from the collections module.
 It automatically assigns a default value to keys that do not exist, which means you 
 don't have to manually check for missing keys and avoid KeyError."""
from collections import defaultdict 
dd= defaultdict(list)
dd['fruits'].append('apple')
dd['vegetables'].append('carrot')
print(dd)
print(dd['juices']) #not assign would not throw keyerror would be []
#ex2
dd1 = defaultdict(int)
a = [1,2,3,4,2,1,1,2]
for x in a:
    dd1[x] +=1 #count oocurance in the list and update
print(dd1)
#using for grouping stuff
from collections import defaultdict
words = ["apple", "ant", "banana", "bat", "carrot", "cat", "drone", "brocolii"]
grouped = defaultdict(list)
for word in words:
    grouped[word[0]].append(word)
print(grouped)
# Using str as the factory function
sd = defaultdict(str)
sd['greeting'] = 'Hello'
print(sd)
#ex3
tuple_list = [("A",5), ("B",3),("A",4),("C",3),("D",4),("A",5),("B",5)]
grouped_data = defaultdict(list)
for key,value in tuple_list:
    grouped_data[key].append(value)
print(grouped_data)
#if you want to sym them up
grouped_data = {k:sum(v) for k, v in grouped_data.items()}
print(grouped_data)

#deque
print("-----Deque-----")
"""A deque stands for Double-Ended Queue. It is a special type of data structure 
that allows you to add and remove elements from both ends efficiently.
Unlike normal queues (which usually follow First In, First Out), a deque 
supports both FIFO and LIFO operations. This makes it very flexible and useful in 
real-world applications like task scheduling, sliding window problems and real-time data processing."""
#aAppending and delelting element from a deque
from collections import deque
dq = deque([])
#add elemnt to the right
dq.append(50)
#adds elemnt to the left
dq.appendleft(40)
print(dq)
#extend[iterable] #more than 1 elemnt to the right
dq.extend([60,70,80])
print("After extend(right):",dq)
##extendleft[iterable] #more than 1 elemnt to the left
dq.extendleft([30,20,10])# cause extend adds in reverse order
print("After extendlenft:",dq)
#remove method
dq.remove(70)
print("After remove(70):", dq)
# Remove elements from the right
dq.pop()
# Remove elements from the left
dq.popleft()  
print("After pop and popleft:", dq)
#clear all elemnt
dq.clear()  # deque: []
print("After clear():", dq)

#Accessing Item and length of deque
dq =deque([1,2,3,3,4,2,4])
#acessing by index can be +ve or -ve
print(dq[0])
print(dq[-1])
#find length 
print(len(dq))

#Count, Rotation and Reversal of a deque
dq = deque([10, 20, 30, 40, 50, 20, 30, 20])
#Counting occurrences of a value
print(dq.count(20))  # Occurrences of 20
print(dq.count(30))  # Occurrences of 30
#rotating of deque
dq.rotate(2)  # Rotate the deque 2 steps to the right
print(dq)
dq.rotate(-3)  # Rotate the deque 3 steps to the left
print(dq)
# 3. Reversing the deque
dq.reverse()  # Reverse the deque
print(dq)

"""
Counter ✔
OrderDict ✔
DefaultDict ✔
UserList
UserString
NamedTuple
Deque
Heapq
UserDict
ChainMap"""