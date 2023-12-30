# Dictionary
# empty dictioary
d = {}
print(d)
# Or
a = dict()
print(a)

# dictionary ={'key1':'value1', 'key2':"value2"....}
d1 = {"Name" : "Yash", "Age" : 18, "Class" : "12th"}
print(d1)

# dic keys can't be mutable but values can be mutable
# dic we can call specific values by their assigned keys
print(d1["Age"])

# it is unorderd
d2 = {"1" : 1, "2" : 2}
d3 = {"2" : 2,"1": 1}
print(d2==d3)
# delete the element
del d2["1"]
print(d2)
# adding elements
d4 = {}
print('d4',d4)
d4["3"] = 3
d4["2"] = 2
print('d4 after adding ',d4)



# SETS

# Sets have unique values
# sets can be defined using {}
# dict and sets have different syntax
# for creating empty set we need to use "set()"
s = set()
print(s)
s1 = set([1,2,4,5,6])
print(s1)
s2 = {1,3,5,5,3,4,6}
print(s2)
print(type(s2))
s3 = set('hello')
print(s3)
# duplicate values are ignored in sets
# set is also unordered
# set only contains immutable type elements
# set itself is mutable
s3.add("abd")
print(s3)
