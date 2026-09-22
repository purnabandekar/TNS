raw_delivery=[('Apple',0.75,50),('Banana',0.40,100),('Milk',2.50,15),('Bread',1.80,20),('Apple',0.75,30)]
shopping_cart=['Apple','dragonfruit','Apple','Bread','Milk']
def check_quantity(raw_delivery):
    final_list={}
    for name,price,qty in raw_delivery:
        if name in final_list:
            final_list[name]["Quantity"]+=qty

        else:
            final_list[name]={"Price":price,"Quantity":qty}
        
    return final_list

def checkout(inventory,shopping_cart):
    receipt=[]
    for items in shopping_cart:
        if items not in inventory:
            print(f"{items} is not there in store")
        elif inventory[items]["Quantity"]<=0:
            print(f"{items} is out of stock")
        else:
            inventory[items]["Quantity"]-=1
            receipt.append((items,inventory[items]["Price"]))
    return receipt
inventory=check_quantity(raw_delivery)
recep= checkout(inventory,shopping_cart)
print("----------Receipt-------")
total=0
for item,price in recep:
    print(f"{item}:","    ",f"{price}")
    total+=price

print("Total:","    ",f"{total}")




