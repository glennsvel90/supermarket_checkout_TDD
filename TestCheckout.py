import unittest
from Checkout import Checkout


class CheckoutTests(unittest.TestCase):
    def test_CanInstantiateCheckout(self):
        co = Checkout()
