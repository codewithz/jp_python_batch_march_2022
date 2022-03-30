# Set --> NO DUPLICATES | UNORDERED
# {}
numbers= [1,1,2,3,4,4]
first=set(numbers)
print(first)

unique_clone={*numbers}
print(unique_clone)

print("First:",first)
second={1,4,5}
print("Second:",second)

second.add(6)
print("Second:",second)
second.add(5)
print("Second:",second)
second.remove(4)
print("Second:",second)
# second.remove(5)
# print("Second:",second)
second.discard(6)
print("Second:",second)
second.discard(6)
print("Second:",second)

print("------------------ Set Operations -----------------")

print("First:",first)
print("Second:",second)

print("Union",first.union(second))
print("Union",first | second)

print("Intersection:",first.intersection(second))
print("Intersection:",first & second)

print("Difference:",first.difference(second))
print("Difference:",first - second)

print("Difference:",second.difference(first))
print("Difference:",second - first)

print("Symmentric Difference:",first.symmetric_difference(second))
print("Symmentric Difference:",first^second)


