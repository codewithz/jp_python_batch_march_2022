cart=[("Bread",5),("Butter",7),("Jam",4)]
print("Cart:",cart)

# sorting_key=lambda  item:item[1];
#
# cart.sort(key=sorting_key)
cart.sort(key=lambda item:item[1])

print("Sorted Cart",cart)

# ----------------------------------

prices=[];

for name,price in cart:
    prices.append(price)

print("Prices:",prices)

x=list(map(lambda item:item[1],cart))

print("Prices x:",x)

#-----------------------------------------

print("-------------------------")

filtered_list=[]

for item in cart:
    name,price=item
    if price>=5:
        filtered_list.append(item)

print("Filtered:",filtered_list)

y=list(filter(lambda item:item[1]>=5,cart))
print("Filtered:",y)