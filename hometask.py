# OOP
print('Task1')

class Fruit:
    def __init__(self, title, price, quantity):
        self.title=title
        self.price=price
        self.quantity=quantity

    def get(self):
        return{
            'title': self.title,
            'price':self.price,
            'quantity':self.quantity
        }
   
    def set_price(self, new_price):
        self.price=new_price
    

banana=Fruit('Banana', 21000, 1 )

print(banana.get())
banana.set_price(19000)
print(banana.get())

print('Task2')
class Kompany:
    def __init__(self, title, tarkibi, quantity, price):
        self.title = title
        self.tarkibi = tarkibi
        self.quantity = quantity
        self.price = price

    def get(self):
        return {
            'title': self.title,
            'tarkibi': self.tarkibi,
            'quantity': self.quantity,
            'price': self.price
        }


product = Kompany(
    title='Macbook',
    tarkibi=['Cpu', 'Cooling', 'sytem', 'Ram', 'Ssd'],
    quantity=1,
    price=14000
)


print(product.get())