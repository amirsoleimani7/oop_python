import csv 


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



    @classmethod #this is called a decorator ...
    def instantaite_from_csv(cls): 
        with open("items.csv" , "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
            
        for item in items:
            print(item)            
            
            Item(
                name = item.get('name') ,
                price = float(item.get('price')) , 
                quantity = int(item.get('quantity')) , 
            )
                
    def apply_discount(self):
        self.price = self.price * self.pay_rate_
        
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})" # the best practice



Item.instantaite_from_csv()
print(f"all the ites are : {Item.all}")

