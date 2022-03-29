numbers=[3,51,2,8,6]
print("O:",numbers)

numbers.sort()
print("Sorted:",numbers)
print("O:",numbers)

numbers.sort(reverse=True)
print("R Sorted:",numbers)
print("O:",numbers)

# ----------------------------------------------
print("-------------------------------------------")
other_numbers=[43,1,67,23,54]
print("O:",other_numbers)

sorted_list=sorted(other_numbers)
print("Sorted:",sorted_list)
print("O:",other_numbers)

reverse_sorted=sorted(other_numbers,reverse=True)
print("R Sorted:",reverse_sorted)
print("O:",other_numbers)

print("------------------------------- Complex Objects-----------------")

cart=[("Bread",5),("Butter",7),("Jam",4)]
print("Cart:",cart)

def sort_cart(item):
    return item[1]

cart.sort(key=sort_cart)
print("Sorted:",cart)

cart.sort(key=sort_cart,reverse=True)
print("R Sorted:",cart)


