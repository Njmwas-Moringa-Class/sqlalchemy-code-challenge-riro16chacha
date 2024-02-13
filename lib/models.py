import os
import sys

sys.path.append(os.getcwd())

from sqlalchemy import (create_engine, Column, String, Integer, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine('sqlite:///db/restaurants.db', echo=True)
Session = sessionmaker(bind=engine)


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    star_rating = Column(Integer)

    restaurant = relationship("Restaurant", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")

    def customer(self):
        # Return the Customer instance for this review
        return self.customer

    def restaurant(self):
        # Return the Restaurant instance for this review
        return self.restaurant


    def __repr__(self):
        return f'Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars.'


class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    price = Column(Integer)

    reviews = relationship("Review", back_populates="restaurant")

    def reviews(self):
        # Return a collection of all the reviews for the Restaurant
        return self.reviews

    def customers(self):
        # Return a collection of all the customers who reviewed the Restaurant
        return [review.customer for review in self.reviews]


    def __repr__(self):
        return f'Restaurant: {self.name}'
    
    @classmethod
    def fanciest(cls):
        session = Session()
        return session.query(cls).order_by(cls.price.desc()).first()

    def all_reviews(self):
        return [review.full_review() for review in self.reviews]


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    reviews = relationship("Review", back_populates="customer")

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f'Customer: {self.first_name} {self.last_name}'
    
    def reviews(self):
        # Return a collection of all the reviews that the Customer has left
        return self.reviews

    def restaurants(self):
        # Return a collection of all the restaurants that the Customer has reviewed
        return [review.restaurant for review in self.reviews]

    
    def favorite_restaurant(self):
         # Return the favorite restaurant of the customer based on their reviews
        session = Session()
        favorite_review = session.query(Review).filter_by(customer_id=self.id).order_by(Review.star_rating.desc()).first()
        if favorite_review:
            return favorite_review.restaurant
        else:
            return None

    def add_review(self, restaurant, rating):
        # Add a new review for the customer
        new_review = Review(restaurant=restaurant, customer=self, star_rating=rating)
        session = Session()
        session.add(new_review)
        session.commit()

    def delete_reviews(self, restaurant):
        # Delete all reviews of the customer for a given restaurant
        session = Session()
        session.query(Review).filter_by(customer_id=self.id, restaurant_id=restaurant.id).delete()
        session.commit()
