class Item:
    
    pay_rate_ = .8     
    all = [] # alist for all the attributes ... 
    
    def __init__(self, name: str, price: float, quantity=0):      
        # run validation to the recived arguments
        assert price >= 0 , f"price [{price}] is not greater than zero!" # the second one is ; f"" is 
        assert quantity >= 0 , f"quantiy [{quantity}] is not greater than zero!"
        
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # actions to excute ... 
        Item.all.append(self)
            
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate_

    def __repr__(self):
        return f"[{self.name},{self.price},{self.quantity}]"
    
    



item1 = Item("Phone" , 100 ,1)
item2 = Item("Laptop", 1000 ,3)
item3 = Item("Cable" , 10 , 5)
item4 = Item("Mouse",  50 , 5)
item5 = Item("Keyboard" , 75 , 5)



print(f"all the ites are : {Item.all}")
print(f"for item1 is : {repr(item1)}")

# for i in range(len(Item.all)):
#     print(f"{i +1} : name is : {Item.all[i].name}")


