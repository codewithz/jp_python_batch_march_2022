cart=[("Bread",5),("Butter",7),("Jam",4)]
print("Cart:",cart)


# [expression for item in items]

prices=list(map(lambda item:item[1],cart))
print("Prices",prices)

prices_lc=[item[1] for item in cart]
print("Prices LC:",prices_lc)

# [expression for item in items if condition]
filtered_list=list(filter(lambda item:item[1]>=5,cart))
print("Filtered List:",filtered_list)

filtered_list_lc=[item for item in cart if item[1]>=5]
print("Filtered List LC:",filtered_list_lc)

names=["Tom","Alex","Leanord","Sheldon"]

len_list=[len(name) for name in names]
print("Names:",names)
print("Length",len_list)

filtered_names=[name for name in names if len(name)>5]
print("Filtered Names:",filtered_names)


employees=[
    (1,"Tom","IT",30000),
    (2,"Alex","IT",33000),
    (3,"Mike","Finance",43000),
    (4,"John","HR",39000),
]

#  Q1 -- Find the list of departments in employees list
# Q2 -- find those employees whose salary is greater than 32k and work in IT

#  List COmprehension

dept_list=[employee[2] for employee in employees]
print(dept_list)

filtered_employee=[employee for employee in employees if employee[2]=='IT' and employee[3]>32000]
print(filtered_employee)
