import pickle

class Data_Manager:
    def __init__(self):
        self.__UserList = []  # Private class attribute for storing user objects
        self.loadUserList()  # Initialize __UserList when an instance is created

    def saveUserList(self, listToSave):
        with open("userlist.txt", "wb") as file:
            pickle.dump(listToSave, file)

    def loadUserList(self):
        try:
            with open("userlist.txt", "rb") as file:
                loadedData = pickle.load(file)
                self.__UserList = loadedData  # Update the private attribute
        except (FileNotFoundError, EOFError):
            self.__UserList = []  # Initialize as an empty list if the file doesn't exist

    def Add_User(self, user_object):
        self.__UserList.append(user_object)
        self.saveUserList(self.__UserList)  # Pass the __UserList as an argument

    def get_User(self, user_name):
        for user in self.__UserList:
            if user.username == user_name:
                return user
        return None
    
    def update_user(self, user_object):
        for user in self.__UserList:
            if user.username == user_object.username:
                user = user_object
                return user
        return None



    print("data_manager_ran")
