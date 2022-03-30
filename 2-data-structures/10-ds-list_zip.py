list1=[1,2,3,4,5]
list2=[10,20,30,40,50]

[(1,10),(2,20),(3,30),(4,40),(5,50)]

zipped_list=list(zip(list1,list2,"abcde"))

for item in zipped_list:
    print(item)
    print(type(item))

print(zipped_list)

