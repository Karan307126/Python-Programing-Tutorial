# creating an empty set
b=set()
print(type(b))

# Adding values to an empty set
b.add(87)
b.add(45)
b.add(67)
b.add(45)
# b.add([97,75,45,24]) # you cannot add list in set
# b.add({6:10})  # you cannot abble to add dictionary in seet
b.add((56,88,2,12,67)) # you can abble to add tuple in set
print(b)

# leanth of the set
print(len(b))  #  prints the leanth of this set 

# removel of an item
# b.remove(67) #  removes 67 from set b
# print(b)

# print(b.pop()) # remove element rendumly in set
# print(b)

# b.clear()   #remove all elements in set
print(b.union({99,21,80}))   #return a new et with all items from both sets
 
print(b.intersection({54,87,45,43}))  #return a set which comtains only items in both set