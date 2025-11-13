from arquivo import *
from models import Restaurant

def save_restaurants(doc):
    restaurants = []
    for item in doc:
        line = item.split(",")
        restaurant = Restaurant(line[2], line[3])
        restaurants.append(restaurant)
    return restaurants

