#!/usr/bin/env python3
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review, engine
import ipdb;


if __name__ == '__main__':
    
    
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Test relationships between models
        # Query a restaurant and print its name
        first_restaurant = session.query(Restaurant).first()
        print("Restaurant Name:", first_restaurant.name)

        # Print reviews for the first restaurant
        print("Reviews for Restaurant:")
        for review in first_restaurant.reviews:
            print(review)

        # Query a customer and print their full name
        first_customer = session.query(Customer).first()
        print("Customer Name:", first_customer.full_name())

        # Print reviews given by the first customer
        print("Reviews by Customer:")
        for review in first_customer.reviews:
            print(review)

        # Query a review and print its details along with related customer and restaurant
        first_review = session.query(Review).first()
        print("Review Star Rating:", first_review.star_rating)
        print("Customer for Review:", first_review.customer.full_name())
        print("Restaurant for Review:", first_review.restaurant.name)

    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Close the session
        session.close()

    ipdb.set_trace()
