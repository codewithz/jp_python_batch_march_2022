letters=["a","b","c","d","e"]

for letter in letters:
    print(letter)
# -----------------------------------


for letter in enumerate(letters):
    print(letter,type(letter))

#--------------------------------------

# item=(0,'a')
# index,letter=item;
#
# print(index,letter)
for index,letter in enumerate(letters):
    print(index,'-',letter)


# ----------------------------------------------

test_list=[[0,1],[2,3]]

for index,element in enumerate(test_list):
    print(index,"-",element)
    for index,letter in enumerate(element):
        print(index,'-',letter)