from sqlalchemy import (
    create_engine, Column, Integer, String, Float, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


# Create the engine and echo SQL statements for debugging
engine = create_engine('sqlite:///ecommerce.db', echo=True)
# Base class for declarative models
Base = declarative_base()


# Tables
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    # One-to-many relationship: a user can have many orders
    orders = relationship('Order', back_populates='user')


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    # Relationship for back-reference if needed (not strictly necessary here)
    order_items = relationship('OrderItem', back_populates='product')


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    # Many-to-one relationship: each order belongs to one user
    user = relationship('User', back_populates='orders')
    # One-to-many relationship: an order can have many order items
    items = relationship('OrderItem', back_populates='order')

    
class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    # Many-to-one relationships
    order = relationship('Order', back_populates='items')
    product = relationship('Product', back_populates='order_items')


# Create all tables
Base.metadata.create_all(engine)
