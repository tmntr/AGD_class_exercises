#Shopping Basket Class - www.101computing.net/shopping-basket-class/
import tom_Item
import tom_new_ShoppingBasket


tomatoSoup = tom_Item.Item("Tomato Soup", "200mL can", 0.70, 10)
spaghetti = tom_Item.Item("Spaghetti", "500g pack", 1.10, 20)
blackOlives = tom_Item.Item("Black Olives Jar", "200g Jar", 2.10, 8)
mozarella = tom_Item.Item("Mozarella", "100g", 1.50, 20)
gratedCheese = tom_Item.Item("Grated Cheese", "100g", 2.20, 40)

myBasket = tom_new_ShoppingBasket.ShoppingBasket()

myBasket.addItem(tomatoSoup, 4)
myBasket.addItem(blackOlives, 1)
myBasket.addItem(mozarella, 2)
myBasket.addItem(tomatoSoup, 6)

myBasket.view()