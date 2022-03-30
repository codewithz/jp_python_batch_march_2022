#Dictionary
# Key-Values Pairs
#{key:value}
#Contact Book Name-> contact_number

point={"x":1,"y":2}
print(point)

point=dict(x=1,y=2)
print(point)

point["x"]=10
point["y"]=20
point["z"]=30

print(point)

print("-----------------Accessing the Data-------------")

print("X",point.get("x"))
print("A",point.get("a",0))

if "a" in point:
    print("A",point.get("a",0))

if "x" in point:
    print("X",point.get("x"))

for key in point:
    print(key, point[key])

for item in point.items():
    print(item)
    print(type(item))

for key,value in point.items():
    print(key,value)