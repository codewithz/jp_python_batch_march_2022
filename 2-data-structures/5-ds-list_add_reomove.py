letters=["a","b","c"]

print("Original",letters)

letters[0]="air";
letters[1]="ball";
letters[2]="charlie"

print("Original",letters)

#Add
letters.append("d")
print("Append",letters)

#Insert
letters.insert(0,'-')
print("Insert",letters)

#Remove
removed=letters.pop(0)
print("removed element was",removed)
print("Pop(0)",letters)


letters.remove("ball")
print("Remove",letters)

del letters[1]
print("Del",letters)

numbers=list(range(1,10))
print("Numbers",numbers)

del numbers[4:6]
print("Del",numbers)