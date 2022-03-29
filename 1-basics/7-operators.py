# and
# or
# not

#Loan Processing System

high_income=False
good_credit=True
student=True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")


if(high_income or good_credit) and student:
    print("Eligible")
else:
    print("Not Eligible")

#----------------------------------------------------
print("-------------------Ternary Operator -----------------")

age=19;
# message=''
# if age>=18:
#     message='Elgible Age'
# else:
#     message="Uneligible Age"

message="Eligible Age" if age>18 else "Uneligible Age";
print("Age:",age,message)


# ------------------------------------------
#  Chaining Comparision Operators

# age  is between 18 and 65

# 18 <= age <= 65

# age >=18 and age<=65:

age=20

if 18 <= age <= 65:
    print("----eligible")