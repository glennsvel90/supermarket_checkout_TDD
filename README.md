# supermarket_checkout_TTD
A project to explore TDD(Test-Driven Development) principles by testing the features of the checkout system.

A checkout cash register system can add items, set prices, give discounts(such as 3 for $2), and calculate the total cost of items.

### Prerequisites

 * Python 3
 * Import the pytest python package with by typing in the terminal:
 
```
pip install pytest
```
### Using the program
 
 In the terminal, change to the directory where the Checkout.py file is located in, then type:

```
python 
```
```
import Checkout
```
```
help(Checkout.Checkout)
```
### Testing the program

In the terminal, change to the directory where the TestCheckout.py file is located in, then type:

```
pytest -v TestCheckout.py
```
Test Cases to make unit tests for:
- [ ] creating an instance of the checkout class. 
- [ ] add an item price
- [ ] adding an individual item to the list of checkout items
- [ ] calculating the current total
- [ ] adding multiple items and getting the correct total
- [ ] the class needs the ability to add discount rules
- [ ] the class needs to be able to apply those discount rules when calculating the total
- [ ] the class needs to throw an exception when an item is added that doesn't have a defined price.
