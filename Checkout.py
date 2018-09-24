import math


class Checkout:
    """ Class to represent an checkout object system
    
    Attributes:
        
    

    class Discount:
        """Class to represent the discount for an item"""
        def __init__(self, numberofItems, price):
            self.numberofItems = numberofItems
            self.price = price
    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def addDiscount(self, item, numberofItems, price):
        discount = self.Discount(numberofItems,price)
        self.discounts[item] = discount

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def CalculateTotal(self):
        total = 0
        for item, cnt in self.items.items():
            total += self.calculateItemTotal(item, cnt)

        return total

    def calculateItemTotal(self, item, cnt):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if cnt >= discount.numberofItems:
                total += self.calculateItemDiscountedTotal(item, cnt, discount)
            else:
                total += cnt * self.prices[item]
        else:
            total += cnt * self.prices[item]
        return total

    def calculateItemDiscountedTotal(self, item, cnt, discount):
        total = 0
        numofDiscounts = math.trunc(cnt/discount.numberofItems)
        total += numofDiscounts * discount.price
        remaining = cnt % discount.numberofItems
        total += remaining * self.prices[item]
        return total



print("""
Explore the docstring for the Checkout class to understand its features.
To do so type: help(Checkout)
You may create an instance of a  checkout system and then add items. 
To create an instance of a checkout system, type into the terminal while in python interactive mode: system = Checkout()
Then add items to the checkout system by typing: system.addItem()

""")
