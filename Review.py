import csv

class Review:
    def __init__(self, reviewer, rideid, rating, comment):
        self.reviewer = reviewer
        self.rideid = rideid
        self.rating = rating
        self.comment = comment

    def __str__(self):
        return f"{self.reviewer} ({self.rating}): {self.comment}"

class ReviewDB:
    def __init__(self, filename='reviewsdb.csv'):
        self.reviews = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                reviewer, reviewee, rating, comment = row
                self.reviews.append(Review(reviewer, reviewee, rating, comment))

    def add_review(self, review):
        self.reviews.append(review)
        with open('reviewsdb.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([review.reviewer, review.reviewee, review.rating, review.comment])
        print(f"Review added: {review}")

    def get_reviews(self):
        return self.reviews

    def get_reviews_by_reviewee(self, reviewee):
        reviews = []
        for review in self.reviews:
            if review.reviewee == reviewee:
                reviews.append(review)
        return reviews

    def get_reviews_by_reviewer(self, reviewer):
        reviews = []
        for review in self.reviews:
            if review.reviewer == reviewer:
                reviews.append(review)
        return reviews

    def get_review_by_reviewer_and_reviewee(self, reviewer, reviewee):
        for review in self.reviews:
            if review.reviewer == reviewer and review.reviewee == reviewee:
                return review
        return None

    def get_average_rating(self, reviewee):
        total = 0
        count = 0
        for review in self.reviews:
            if review.reviewee == reviewee:
                total += int(review.rating)
                count += 1
        if count == 0:
            return 0
        return total / count