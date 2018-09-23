import math


class Checkout:

    class Discount:
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
            if item in self.discounts:
                discount = self.discounts[item]
                if cnt >= discount.numberofItems:
                    numofDiscounts = math.trunc(cnt/discount.numberofItems)
                    total += numofDiscounts * discount.price
                    remaining = cnt % discount.numberofItems
                    total += remaining * self.prices[item]
                else:
                    total += cnt * self.prices[item]
            else:
                total += cnt * self.prices[item]
        return total
