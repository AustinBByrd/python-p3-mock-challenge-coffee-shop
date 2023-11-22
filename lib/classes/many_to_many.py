from statistics import mean

class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name_str):
        if isinstance(name_str, str) and len(name_str) >= 3 and not hasattr(self, 'name'):
            self._name = name_str

    def orders(self):
        return [order for order in Order.all if order.coffee is self]
    
    def customers(self):
        return list({ order.customer for order in Order.all if order.coffee is self })
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        # num_orders = self.num_orders()
        # total = 0
        # for order in self.orders():
        #     total += order.price

        # if total > 0:
        #     return total / num_orders
        
        # return 0
         if len(self.orders()) > 0:
            return mean([order.price for order in self.orders()])
         
         return 0

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name_str):
        if isinstance(name_str, str) and len(name_str) > 1 and len(name_str) < 16:
            self._name = name_str
        
    def orders(self):
        return [order for order in Order.all if order.customer is self]
    
    def coffees(self):
        return list({ order.coffee for order in Order.all if order.customer is self })
    
    
    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        return order
    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price_int):
        if isinstance(price_int, float) and price_int > 1 and price_int < 11 and not hasattr(self, 'price'):
            self._price = price_int  



# coffee = Coffee("Mocha")
# print(coffee.name == "Mocha")

coffee = Coffee("Mocha")
coffee2 = Coffee("Black")
coffee3 = Coffee('Chai Tea')
customer = Customer('Dj')
order = Order(customer, coffee, 9.99)
order = Order(customer, coffee, 5.99)
order = Order(customer, coffee, 14.99)

# print(coffee.orders()) - done
# print(coffee.customers()) - done
# print(customer.coffees()) - done\

customer.create_order(coffee2, 4)
# print(coffee2.num_orders())
print(coffee3.average_price())



