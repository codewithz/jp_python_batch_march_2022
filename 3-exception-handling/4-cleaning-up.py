try:
    file=open("1-exceptions.py")
    print("File Closed Status:",file.closed)
    age=int(input("Enter Age:"));
    xfactor=10/age;
    print(f"Age is {age} and xfactor is {xfactor}")
except ValueError as ex:
    print("Invalid Age entered")
except ZeroDivisionError as ex:
    print("You seem to enter age as zero")
except BaseException as ex:
    print("Some other exception occurred")
    print("Reason:",ex)
else:
    print("No exception occurred")
finally:
    print("executes in all conditions [Exceptions occurred or not]")
    file.close()
    print("File Closed Status:",file.closed)

print("\n\nExecution continues.....")