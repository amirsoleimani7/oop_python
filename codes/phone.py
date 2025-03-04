from item import Item

class Phone(Item): #inehrate form the Item class
    def __init__(self, name: str, price: float, quantity=0 , broken_phones=0):                  
            super().__init__(name , price , quantity)
            assert broken_phones >= 0 , f"quantiy [{broken_phones}] is not greater than zero!"   
                     
            self.broken_phones = broken_phones
            
