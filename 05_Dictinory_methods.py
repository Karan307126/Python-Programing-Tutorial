myDict={
    "fast":"In a Quick Manner",
    "karan":"A Coder",
    "marks":[1,4,7],
    "anodherdict":{'Karan':'Cricketer'},
    1: 2}

print(myDict.keys())   # prints the keys of the dictionary
print(myDict.values()) # prints the keys of the dictionary
print(myDict.items()) # prints the keys of the dictionary
print(myDict)
updatedict={
    "Tushar":"Brother"
}
myDict.update(updatedict)  # Add or change a new updates in dictionary
print(myDict)

print(myDict.get("karan")) # prints values assosiated with key "karan"
print(myDict["karan"]) #  prints values assosiated with key "karan"

# The different between .get and [] syntx in dictionary
print(myDict.get("karan1")) # returns none as karan1 is not present in dictionery
# print(myDict["karan1"])  # throws an error as karan1 is not present in dictionary