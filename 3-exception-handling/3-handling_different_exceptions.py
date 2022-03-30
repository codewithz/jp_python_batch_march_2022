try:
    age=int(input("Enter Age:"));
    xfactor=10/age;
    print(f"Age is {age} and xfactor is {xfactor}")
    numbers=[1,2]
    print(numbers[3])
except ValueError as ex:
    print("Invalid Age entered")
except ZeroDivisionError as ex:
    print("You seem to enter age as zero")
except BaseException as ex:
    print("Some other exception occurred")
    print("Reason:",ex)
else:
    print("No exception occurred")

print("\n\nExecution continues.....")