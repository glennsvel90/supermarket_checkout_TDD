import pytest
from Checkout import Checkout

@pytest.fixture()
def checkout():
    checkout = Checkout()
    return checkout


def test_CanFindTheCurrentTotal(checkout):
    checkout.addItemPrice("a", 1)
    checkout.addItem("a")
    assert checkout.CalculateTotal() == 1

def test_GetCorrectTotalWithMultipleItems(checkout):
    checkout.addItemPrice("a", 1)
    checkout.addItemPrice("b", 2)
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.CalculateTotal() == 3
