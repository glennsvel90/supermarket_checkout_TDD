import unittest
from Checkout import Checkout


class CheckoutTests(unittest.TestCase):
    def test_CanInstantiateCheckout(self):
        co = Checkout()

    def test_CanAddItemPrice(self):
        co = Checkout()
        co.addItemPrice("a",1)
