class car :
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price 
car1 = car ("BMW",550000)    
print("car1.brand")
print("car1.price")    

class Bank:
    def __init__ (self,balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

b = Bank(5000)
print(b.get_balance())    
