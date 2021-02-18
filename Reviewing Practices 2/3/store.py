from models import Product, User, Comment
from datetime import datetime


class Store:

    products: [Product]
    users: [User]

    def __init__(self):
        self.products = dict()
        self.users = list()

    def add_product(self, product, amount=1):
        self.products[product] = self.products.get(product, 0) + amount

    def remove_product(self, product, amount=1):
        if product not in self.products:
            raise Exception('Not Enough Products')
        if self.products[product] - amount < 0:
            raise Exception('Not Enough Products')

        self.products[product] -= amount
        if self.products[product] == 0:
            del self.products[product]

    def add_user(self, username):
        new_user = User(username)
        if new_user in self.users:
            return None
        self.users.append(new_user)
        return username

    def get_total_asset(self):
        sumo = 0
        for p in self.products:
            sumo += self.products[p] * p.price
        return sumo

    def get_total_profit(self):
        sumo = 0
        for user in self.users:
            for product in user.bought_products:
                sumo += product.price
        return sumo

    def get_comments_by_user(self, user):
        result = []
        for product in self.products:
            for comment in product.comments:
                if comment.user == user:
                    result.append(comment.text)
        return result

    def get_inflation_affected_product_names(self):
        result = set()
        for p in self.products:
            for q in self.products:
                if p == q:
                    continue
                if p.name == q.name and p.price != q.price:
                    result.add(p.name)
        return list(result)

    def clean_old_comments(self, date):
        to_remove = []
        for product in self.products:
            for comment in product.comments:
                if comment.date_added < date:
                    to_remove.append((product, comment))

        for item in to_remove:
            item[0].comments.remove(item[1])

    def get_comments_by_bought_users(self, product):
        result = []
        for comment in product.comments:
            if product in comment.user.bought_products:
                result.append(comment.text)
        return result
