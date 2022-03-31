import  time

print(time.time())

def send_mail():
    for x in range(10000):
        print("z")

start=time.time()
send_mail()
end=time.time()

duration=end-start
print("Duration:",duration)
