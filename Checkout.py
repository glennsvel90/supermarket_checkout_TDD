import math


class Checkout:
    """ Class to represent a checkout object system
    
    Attributes:
        prices(dict): A dictionary of items and their value prices
        discounts(dict): A dictionary of items and their value class instances of discounts
        items(dict): A dictionary of items and each of their quantities added
        
   Methods:
        addItem: Used to add an item.
        addItemPrice: Used to add an item's price
        addDiscount: Used to add a discount
        CalculateTotal: Used to calculate the total of all items combined
        CalculateItemTotal: Used to calculate the total cost of all items of one type
        CalculateItemDiscountedTotal: Used to calculate the total cost of discounted items of a type
    """
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
        """Used to add a discount"""
        discount = self.Discount(numberofItems,price)
        self.discounts[item] = discount

    def addItemPrice(self, item, price):
        """Used to add an item's price"""
        self.prices[item] = price

    def addItem(self, item):
        """Used to add an item."""
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def CalculateTotal(self):
        """Used to calculate the total of all items combined"""
        total = 0
        for item, cnt in self.items.items():
            total += self.calculateItemTotal(item, cnt)

        return total

    def calculateItemTotal(self, item, cnt):
        """Used to calculate the total cost of all items of one type"""
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
        """Used to calculate the total cost of discounted items of a type"""
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
