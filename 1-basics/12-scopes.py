message="Hello All"

def greet(name):
    message="Hello"
    print(name)

def send_email():
    global message
    message="hi"


print(message)
greet("Zartab")
print(message)
send_email()
print(message)

#------- Python doesn;t support block scopes

for number in range(3):
    print(number)

print("number--",number)