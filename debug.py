#!/usr/bin/env python3
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Review, Restaurant, Customer
import ipdb
from sqlalchemy.exc import OperationalError

if __name__ == '__main__':
    try:
        # Corrected database path
        engine = create_engine('sqlite:///db/restaurants.db')
        Session = sessionmaker(bind=engine)
        
        # Ensuring session is scoped within a context manager
        with Session() as session:
            # Test Review object relationship methods
            first_review = session.query(Review).first()
            print("Review customer:", first_review.customer)
            print("Review restaurant:", first_review.restaurant)

            # Test Restaurant object relationship methods
            first_restaurant = session.query(Restaurant).first()
            print("Restaurant reviews:")
            for review in first_restaurant.reviews:
                print(review)
            print("Restaurant customers:")
            for customer in first_restaurant.customers:
                print(customer)

            # Test Customer object relationship methods
            first_customer = session.query(Customer).first()
            print("Customer reviews:")
            for review in first_customer.reviews:
                print(review)
            print("Customer restaurants:")
            for restaurant in first_customer.restaurants:
                print(restaurant)  

            ipdb.set_trace()

    except OperationalError as e:
        print("An error occurred while connecting to the database:", e)

    except Exception as e:
        print("An unexpected error occurred:", e)
