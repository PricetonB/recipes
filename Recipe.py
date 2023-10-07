
from Review import Review


class Recipe:
    def __init__(self, title, cooking_time, difficulty):
        self.title = title
        self.cooking_time = cooking_time
        self.difficulty = difficulty
        self.reviews = []

    def add_review(self, user, rating, comment):
        review = Review(user, rating, comment)
        self.reviews.append(review)