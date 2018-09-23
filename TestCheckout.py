import pytest
from Checkout import Checkout

@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice("a", 1)
    checkout.addItemPrice("b", 2)
    return checkout


def test_CanFindTheCurrentTotal(checkout):
    checkout.addItem("a")
    assert checkout.CalculateTotal() == 1

def test_GetCorrectTotalWithMultipleItems(checkout):
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.CalculateTotal() == 3

def test_AddDiscount(checkout):
    checkout.addDiscount("b", 3, 2)



def test_ApplyDiscount(checkout):
    checkout.addDiscount("b", 3, 2)
    checkout.addItem("b")
    checkout.addItem("b")
    checkout.addItem("b")
    assert checkout.CalculateTotal() == 2
