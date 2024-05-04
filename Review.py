import csv
from Ride import *

class Review:
    def __init__(self, user, rideid, rating, comment):
        self.user = user
        self.rideid = rideid
        self.rating = rating
        self.comment = comment

    def __str__(self):
        return f"Rating: {self.rating}, Comment: {self.comment}, Ride ID: {self.rideid}, user: {self.user}"

class ReviewDB:
    def __init__(self, filename='reviewsdb.csv'):
        self.reviews = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                user, rideid, rating, comment = row
                self.reviews.append(Review(user, rideid, rating, comment))

    def add_review(self, review):
        self.reviews.append(review)
        with open('reviewsdb.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([review.user, review.rideid, review.rating, review.comment])
        print(f"Review added: {review}")

    def get_reviews(self):
        return self.reviews

    def get_review_by_rideid(self, rideid):
        reviews = []
        for review in self.reviews:
            if review.rideid == rideid:
                reviews.append(review)
        return reviews

    def get_reviews_by_driver(self, driver):
        reviews = []
        for i in get_rides_by_driver(driver):
            for review in self.reviews:
                if review.rideid == i.ride_id:
                    reviews.append(review)
        return reviews

    def get_review_by_user(self, user):
        reviews = []
        for review in self.reviews:
            if review.user == user:
                reviews.append(review)
        return reviews