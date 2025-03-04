import csv
class Item: 

    pay_rate_ = .8     
    all = [] # alist for all the attributes ... 
    
        
    def __init__(self, name: str, price: float, quantity=0):      
        # run validation to the recived arguments
        print(f"we are in the constructor of the Item class!!")
        
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
            # making the objects ... 
            Item(
                name = item.get('name') ,
                price = float(item.get('price')) , 
                quantity = int(item.get('quantity')) , 
            )
    
    
    @staticmethod 
    def is_integer(num):
        if(isinstance(num,float)):
            return num.is_integer() # if the number after floating point is zero
                                    # retrun True , otherwise it returns false
        elif isinstance(num , int):
            return True
        else:
            return False
                
    def apply_discount(self):
        self.price = self.price * self.pay_rate_
        
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})" # the best practice
