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
#