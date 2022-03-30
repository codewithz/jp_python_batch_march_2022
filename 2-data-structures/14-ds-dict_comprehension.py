values=[]

for x in range(5):
    values.append(x*2)

print(values)

# [expression for item in items]

values=[x*2 for x in range(5)]
print(values)

#-------- Dictionary Comprehension --------------

# {key:expression for item in items}

value_dict={x:x*3 for x in range(1,11)}
print(value_dict)

value_dict={"A"+str(x):x*3 for x in range(1,11)}
print(value_dict)



