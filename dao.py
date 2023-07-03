from database import db_session
from models import Product, Order

class ProductDAO:
    @staticmethod
    def get_all_products():
        return db_session.query(Product).all()

    @staticmethod
    def create_product(name, price, quantity):
        product = Product(name=name, price=price, quantity=quantity)
        db_session.add(product)
        db_session.commit()
        return product

    @staticmethod
    def update_product(id, name, price, quantity):
        product = db_session.query(Product).get(id)
        if product:
            product.name = name
            product.price = price
            product.quantity = quantity
            db_session.commit()
        return product

    @staticmethod
    def delete_product(id):
        product = db_session.query(Product).get(id)
        if product:
            db_session.delete(product)
            db_session.commit()
            return True
        return False


class OrderDAO:
    @staticmethod
    def get_all_orders():
        return db_session.query(Order).all()

    @staticmethod
    def create_order(product_id, quantity, order_date):
        order = Order(product_id=product_id, quantity=quantity, order_date=order_date)
        db_session.add(order)
        db_session.commit()
        return order

    @staticmethod
    def update_order(id, product_id, quantity, order_date):
        order = db_session.query(Order).get(id)
        if order:
            order.product_id = product_id
            order.quantity = quantity
            order.order_date = order_date
            db_session.commit()
        return order

    @staticmethod
    def delete_order(id):
        order = db_session.query(Order).get(id)
        if order:
            db_session.delete(order)
            db_session.commit()
            return True
        return False