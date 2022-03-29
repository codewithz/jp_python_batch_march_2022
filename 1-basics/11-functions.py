print("------------- Normal Function --------------------")

def greet():
    print("Hi There")
    print("Welcome Aboard")


greet()

print("--------------- Functions with Parameters-------------------")

def greeting(first_name,last_name):
    print(f"{first_name} {last_name}")


greeting("Zartab","Nakhwa")
greeting("John","Smith")

print("----------- Functions with return type ---------------")

#Type of Function
#  # 1. Performs a Task
#  # 2. Do some processing and return a value

#  1. Perform a Task

def greet(name):
    print(f"Hello {name}")

greet("Tom")

# ---------------------------
def get_greeting(name):
    return  f"HI {name}"

message=get_greeting("Alex");
# Send that in email
# Print to console ? Log
#  Store in DB
# Store it in a file
# Send over network

print(message)

print("--------------- Keyword Arguments ----------")
import math;

def increment(number,by):
    number=math.factorial(number)
    added_values=number+by;
    return added_values;

result=increment(number=4,by=2)
print(result)

print("--------------- Default Arguments --------------")

def increment_numbers(number,by=1):
    return  number+by;

result=increment_numbers(5)
print(result)

result=increment_numbers(6,3)
print(result)

print("----------- Variying Arguments [xargs]-----------------")

def multiply(*numbers):
    print(numbers,type(numbers))
    total=1
    for number in numbers:
        total=total*number;
    return total

print(multiply(6,5))
print(multiply(6,5,4))
print(multiply(6,5,4,5))
#------------------------------------------------
def say_hello(*names):
    for name in names:
        print(f"Hey {name.upper()}")

say_hello("Zartab","Alex","Tom")

print("------------ Varying Argument for Dict [xxargs]------------")

def save_user(**user):
    print(user)
    print(type(user))


save_user(id=1,name="Tom",dept="IT",salary=30000)

