dictionary={"me":"myself", 1:"one", 2:"two", 3:"three"}
print(dictionary)

dictionary.pop(1)
print(dictionary)

dictionary.popitem()
print(dictionary)

del dictionary["me"]
print(dictionary)
