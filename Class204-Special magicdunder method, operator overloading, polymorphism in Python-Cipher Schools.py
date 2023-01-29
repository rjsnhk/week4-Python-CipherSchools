class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def phone_num(self):
        return f"{self.brand} {self.model}"

    def __str__(self):
        return f"{self.brand} {self.model}"

    def __repr__(self):
        return f"Phone({self.brand} {self.model} {self.price})"

    def __len__(self):
        return len(self.phone_num())

    def __add__(self,other):
        return self.price + other.price
class Smartphone(Phone):
    def __init__(self, brand, model, price,camera):
        super().__init__(brand, model, price)
        self.camera = camera
    
    def phone_num(self):
        return f"{self.brand} {self.model} and price is {self.price}"

my_phone = Phone('Nokia','1100',1000)
my_phone2 = Phone('Nokia','1600',1200)
my_smartphone = Smartphone('One Plus','9r',36000,'64mp')
print(my_smartphone.phone_num())
print(my_phone.phone_num())
print(my_phone + my_phone2)
print(my_phone)
print(my_phone.__repr__())
print(len(my_phone))
