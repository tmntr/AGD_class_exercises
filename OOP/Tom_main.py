#Shopping Basket Class - www.101computing.net/shopping-basket-class/
from OOP.Tom_Item import Item
from OOP.Tom_new_ShoppingBasket import ShoppingBasket


tomatoSoup = Item("Tomato Soup","200mL can", 0.70,10)
spaghetti = Item("Spaghetti","500g pack", 1.10,20)
blackOlives = Item("Black Olives Jar","200g Jar", 2.10,8)
mozarella = Item("Mozarella","100g", 1.50,20)
gratedCheese = Item("Grated Cheese","100g",2.20,40)

myBasket = ShoppingBasket()

myBasket.addItem(tomatoSoup, 4)
myBasket.addItem(blackOlives, 1)
myBasket.addItem(mozarella, 2)
myBasket.addItem(tomatoSoup, 6)

myBasket.view()