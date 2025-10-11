import pytest
from Class_excercises.OOP.Tom_new_ShoppingBasket import ShoppingBasket

tomatoSoup = Item("Tomato Soup","200mL can", 0.70,10)
spaghetti = Item("Spaghetti","500g pack", 1.10,20)
blackOlives = Item("Black Olives Jar","200g Jar", 2.10,8)
mozarella = Item("Mozarella","100g", 1.50,20)
gratedCheese = Item("Grated Cheese","100g",2.20,40)

testshoppingbasket = ShoppingBasket()



def test_add_item():
    with pytest.raises(ValueError):
        testshoppingbasket.add_item(tomatoSoup,100)
    with pytest.raises(ValueError):
        testshoppingbasket.add_item(tomatoSoup,-100)
    testshoppingbasket.add_item(tomatoSoup)
    assert testshoppingbasket.items[tomatoSoup] == 1
    testshoppingbasket.add_item(spaghetti,20)
    assert testshoppingbasket.items[spaghetti] == 20



def test_remove_item():
    assert False


def test_update_item():
    assert False


d