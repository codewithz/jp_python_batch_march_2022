if True:
    print("Hello")
print("I am here")

#----------------------------------------------
print("-----------------------")
x=2

if x>3:
    print("Hello Tom")
else:
    print("Hello Alex")

#----------------------------------------------------

a=300
b=330

if a>b:
    print(a,"is greater than",b)
else:
    print(b,"is greater than",a)

#----------------------------------------------------
print("--------------------------------------------")
a=int(input("Enter first value:"))
b=int(input("Enter second value:"))
c=int(input("Enter third value:"))

if (a>b and a>c):
    print(a,"is greater than",b,"and",c)
elif (b>a and b>c):
    print(b,"is greater than",a,"and",c)
else:
    print(c,"is greater than",a,"and",b)

#--------------------------------------------------------

a=10
b=10

if a==b: print("a is equal to b")

a=11
b=10

print("A") if a>b else print("B")

a=50
b=50

print("A") if a>b else print("=") if a==b else print("B")