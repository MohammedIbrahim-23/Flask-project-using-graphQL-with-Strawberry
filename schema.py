import strawberry
from typing import List
from dao import ProductDAO, OrderDAO

@strawberry.type
class ProductType:
    id: int
    name: str
    price: int
    quantity: int

@strawberry.type
class OrderType:
    id: int
    product_id: int
    quantity: int
    order_date: str

@strawberry.type
class Query:
    @strawberry.field
    def get_products(self) -> List[ProductType]:
        return ProductDAO.get_all_products()

    @strawberry.field
    def get_orders(self) -> List[OrderType]:
        return OrderDAO.get_all_orders()

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_product(self, name: str, price: int, quantity: int) -> ProductType:
        return ProductDAO.create_product(name, price, quantity)

    @strawberry.mutation
    def update_product(self, id: int, name: str, price: int, quantity: int) -> ProductType:
        return ProductDAO.update_product(id, name, price, quantity)

    @strawberry.mutation
    def delete_product(self, id: int) -> bool:
        return ProductDAO.delete_product(id)

    @strawberry.mutation
    def create_order(self, product_id: int, quantity: int, order_date: str) -> OrderType:
        return OrderDAO.create_order(product_id, quantity, order_date)

    @strawberry.mutation
    def update_order(self, id: int, product_id: int, quantity: int, order_date: str) -> OrderType:
        return OrderDAO.update_order(id, product_id, quantity, order_date)

    @strawberry.mutation
    def delete_order(self, id: int) -> bool:
        return OrderDAO.delete_order(id)

# Create the GraphQL schema
schema = strawberry.Schema(query=Query, mutation=Mutation)