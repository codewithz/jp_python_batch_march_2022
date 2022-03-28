i=10
print(i)
print(type(i))

f=4.5
print(f)
print(type(f))

c=10+5j;
print(c)
print(type(c))

# Convert the types o variables

f1=float(i)
print(i)
print(f1)

i1=int(f)
print(f)
print(i1)

c1=complex(f)
print(f)
print(c1)

# iN built funtions

min_value=min(1,2,3,4,5,6,0)
print("min:",min_value)

max_value=max(1,2,3,4,5,6,0)
print("max:",max_value)

a=-3
print(a)
a=abs(a)
print(a)

cube_of_four=pow(4,3)
print('4 to the power of 3 is',cube_of_four)

import math;

print(dir(math))

print("PI:",math.pi)

square_root_of_64=math.sqrt(64)

print("Square Root of 64 is",square_root_of_64)

print("If we divide 5 by 2 remainder will be ",math.remainder(5,2))

number=3.4

print("floor Value",math.floor(number))
print("Cieling Value",math.ceil(number))

number=4

factorial_of_four=math.factorial(number)
print("Factorial of 4 is ",factorial_of_four)

#Trignometry Functions
rad=math.radians(90)
print("Radian of 90 is",rad)
print("Sin 90:",math.sin(rad))