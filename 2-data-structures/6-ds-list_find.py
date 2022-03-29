letters=["a","b","c","d","e"]

print(letters.index("a"))

#Way-1 to make sure if element is not found program doesn't break
if "f" in letters:
    print(letters.index("f"))
#Way-2  to make sure if element is not found program doesn't break
count=letters.count("d")
if count>0:
    print(letters.index("d"))
