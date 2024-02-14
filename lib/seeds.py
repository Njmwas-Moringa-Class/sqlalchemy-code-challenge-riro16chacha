import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review, Base

# Connect to the database
engine = create_engine('sqlite:///db/restaurants.db')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add sample data
# Create restaurants
restaurant1 = Restaurant(name="Villa Rosa", price=125000)
restaurant2 = Restaurant(name="Faremont", price=40000)
session.add_all([restaurant1, restaurant2])
session.commit()

# Create customers
customer1 = Customer(first_name="Riro", last_name="Chacha")
customer2 = Customer(first_name="Jane", last_name="Gati")
session.add_all([customer1, customer2])
session.commit()

# Create reviews
review1 = Review(restaurant_id=restaurant1.id, customer_id=customer1.id, star_rating=5)
review2 = Review(restaurant_id=restaurant2.id, customer_id=customer2.id, star_rating=4)
review3 = Review(restaurant_id=restaurant1.id, customer_id=customer2.id, star_rating=3)
session.add_all([review1, review2, review3])
session.commit()


if __name__ == '__main__':
    engine = create_engine('sqlite:///db/restaurants.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add print statement to indicate start of seeding
    print("Seeding the database...")

    # Your seeding logic here

    # Add print statement to indicate end of seeding
    print("Seeding completed.")

