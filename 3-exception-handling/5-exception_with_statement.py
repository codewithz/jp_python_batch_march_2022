try:
    with open("1-exceptions.py") as source, open("2-exception-handling.py") as target:
        x=10/1;
        print("operations inside the with block")
        print("Source Inside with",source.closed)
        print("Target Inside with",target.closed)

    print("Source OUTSIDE with",source.closed)
    print("Target OUTSIDE with",target.closed)

except BaseException as ex:
    print("Some other exception occurred")
    print("Reason:",ex)
else:
    print("No exception occurred")
finally:
    print("executes in all conditions [Exceptions occurred or not]")



print("\n\nExecution continues.....")