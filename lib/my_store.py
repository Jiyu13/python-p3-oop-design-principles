class User:

    def sign_in(self, user):
        self.user = user


    def current_user(self):
        return self.user

    
    def sign_in(self):
        pass

    
    def sign_out(self):
        pass


class Item:
    def item(self, item):
        self.item = item


    def item_price(self, price):
        self.item_price = price


 class ShoppingCart:   

    # refactor by creating __init__() which initialises coupon attritube 
    def __init__(self, coupon=0)
        self.coupon = coupon

    def shopping_cart(self):
        self.shopping_cart = list()


    def add_item_to_cart(self, item):
        self.shopping_cart.append(item)


    # refactor to be able to access coupon attritube
    def checkout(self):
        total = sum([item.price for item in self.shopping_cart()])
        total -= total * self.coupon / 100

        return total
    

    # def checkout(self, discount=0):
    #     total = sum([item.price for item in self.shopping_cart()])
    
    #     #  if/else statement to determine what discount a user has
    #     #  but too much repetition
    #     if discount == 10:
    #         total -= total * 10 / 100.00
    #     elif discount == 20:
    #         total -= total * 20 / 100.00
    #     elif discount == 50:
    #         total -= total * 50 / 100.00
        
        return total
