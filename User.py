

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.saved_recipes = []

    def save_recipe(self, recipe):
        self.saved_recipes.append(recipe)

    def view_saved_recipes(self):
        return self.saved_recipes