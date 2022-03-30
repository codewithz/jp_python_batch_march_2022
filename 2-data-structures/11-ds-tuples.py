# Tuples are Read Only Lists
# ()
# Way to define a tuple

point=(1,2)
print(type(point))
print(point)

point=1,2
print(type(point))
print(point)

point=1,
print(type(point))
print(point)

point=(1,2)+(3,4)
print(type(point))
print(point)

point=(1,2)*3
print(type(point))
print(point)

#-----------------------------------

point=(1,2,3)

print("Index 1:",point[1])

print("Range Access:",point[0:2])

x,y,z=point

print("X:",x)
print("Y:",y)
print("Z:",z)

if 10 in point:
    print("10 is in tuple")
else:
    print("10 is not in tuple")

#---------------------------------

# point[1]=10
# TypeError: 'tuple' object does not support item assignment

point_list=list(point)

print(point_list)

point_list.append(4)
print(point_list)

point=tuple(point_list)
print(point)
