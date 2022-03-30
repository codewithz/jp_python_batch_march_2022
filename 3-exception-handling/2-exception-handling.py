try:
    age=int(input("Enter Age:"))
    print(f"Age is {age}");
except ValueError as ex:
    print("You entered invalid age")
    print(ex)
    print(type(ex))
else:
    print("Else is executed when no exception occur")

print("Execution continues....")