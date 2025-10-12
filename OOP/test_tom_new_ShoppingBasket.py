import pytest
import tom_new_ShoppingBasket
import tom_Item

tomatoSoup = tom_Item.Item("Tomato Soup", "200mL can", 0.70, 10)
spaghetti = tom_Item.Item("Spaghetti", "500g pack", 1.10, 20)
blackOlives = tom_Item.Item("Black Olives Jar", "200g Jar", 2.10, 8)
mozarella = tom_Item.Item("Mozarella", "100g", 1.50, 20)
gratedCheese = tom_Item.Item("Grated Cheese", "100g", 2.20, 40)

testshoppingbasket = tom_new_ShoppingBasket.ShoppingBasket()





def test_add_item():
    with pytest.raises(ValueError):
        testshoppingbasket.addItem(tomatoSoup,100)
    with pytest.raises(ValueError):
        testshoppingbasket.addItem(tomatoSoup,-10)
    testshoppingbasket.addItem(tomatoSoup,2)
    assert testshoppingbasket.items[tomatoSoup] == 2
    testshoppingbasket.addItem(spaghetti,20)
    assert testshoppingbasket.items[spaghetti] == 20

#testshoppingbasket = tom_new_ShoppingBasket.ShoppingBasket()
print(testshoppingbasket.items)

def test_remove_item():
    with pytest.raises(ValueError):
        testshoppingbasket.removeItem(spaghetti,-10)
    with pytest.raises(ValueError):
        testshoppingbasket.removeItem(blackOlives,10)
    testshoppingbasket.removeItem(tomatoSoup,1)
    assert testshoppingbasket.items[tomatoSoup] == 1
    testshoppingbasket.removeItem(spaghetti, 20)
    assert spaghetti not in testshoppingbasket.items




def test_update_item():
    with pytest.raises(ValueError):
        testshoppingbasket.updateItem(tomatoSoup,-10)
    testshoppingbasket.updateItem(tomatoSoup,2)
    assert testshoppingbasket.items[tomatoSoup] == 2
    testshoppingbasket.updateItem(tomatoSoup,0)
    assert tomatoSoup not in testshoppingbasket.items


