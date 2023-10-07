from Recipe import Recipe
from Review import Review
from User import User
from Data_Manager import Data_Manager
'''use hashmap with key username and value user object
to be able to match password to username

make user interface class that specifically handles 
input statements with number inputs

make place to store all recipes were they can be
searched add user variable to recipe class
'''

ActiveUser = None
activeStatus = False
data_manager = Data_Manager()

  
#User Screen Routines
def AddRecipe():
    global ActiveUser
    title = input("recipe name: ")
    cooktime = input("time to cook: ")
    difficulty = input("enter difficulty: ")
    createdRecipe = Recipe(title, cooktime, difficulty)
    ActiveUser.save_recipe(createdRecipe)
    data_manager.update_user(ActiveUser)
    print("recipe added")
    return

def viewRecipes():
    recipeCount = 1
    global ActiveUser
    recipes = ActiveUser.view_saved_recipes()
    for recipe in recipes:
        print(f"recipe #{recipeCount}: {recipe.title}")
        recipeCount += 1


  
#review screen routines
def getRecipe(recipeTitle):
    global ActiveUser
    recipes = ActiveUser.view_saved_recipes()
    for recipe in recipes:
        if recipe.title == recipeTitle:
            return recipe
    print("recipe not found")

def leaveReview(recipeObject = Recipe):
    rating = input("please leave a rating 1 through 5")
    comment = input("please add a comment about recipe")
    recipeObject.add_review(ActiveUser.user, rating, comment)



#login screen routines
def CreateUser():
    userName = input("username: ")
    email = input("email: ")
    passWord = input("password: ")
    newUser = User(userName, email, passWord)
    data_manager.Add_User(newUser)
    print("user created succsefully")
    return

def Login():
    global activeStatus
    global ActiveUser
    name = input("enter username: ")
    userObject = data_manager.get_User(name)
    if userObject:
        ActiveUser = userObject
        activeStatus = True
        print(f"logged in {ActiveUser.username} succesfully")
        return
    print("user not found")
    return



#User Interface routine
def runLoginScreen():
    running = True
    while running:
        userInput = input("1 to login, 2 to create account, 0 to close ")
        if userInput == "0":
            running = False
        if userInput == "1":
            Login()
            runUserScreen()

        if userInput == "2":
            CreateUser()

def runReviewScreen():
    reviewQuestion = ("would you like to leave a review. 1 for yes, 2 for no")
    if reviewQuestion == "1":
        recipeToReview = input("please enter the name of the recipe to review")
        recipeObject = getRecipe(recipeToReview)
        if recipeObject:
            leaveReview(recipeObject)

def runUserScreen():
    global activeStatus
    global ActiveUser
    while activeStatus:
        print(f"what would you like to do {ActiveUser.username}: ")
        loggedUserInput = input("1 to view recipes, 2 to add recipe, 0 to logout: ")
        if loggedUserInput == "0":
            activeStatus = False
            ActiveUser = None
        if loggedUserInput == "1":
            print("showing recipes")
            viewRecipes()
            runReviewScreen()
        if loggedUserInput == "2":
            AddRecipe()
            print("adding recipe")


# Main
def Main():
    runLoginScreen()



Main()