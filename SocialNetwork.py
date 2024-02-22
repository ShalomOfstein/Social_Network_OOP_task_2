from User import User

'''
this is the class for the social network
it is a singleton class so it can only be instantiated once
it has a name and a list of users
'''


class SocialNetwork:
    _instance = None
    _users = []  # a static list of users. since the social network is a singleton, the list is also static.

    '''
    this is my implementation of the singleton pattern
    I use the __new__ method to create the instance only once and then return the same instance every time
    the reason i use __new__ and not instance_of is that __new__ is called when the SocialNetwork() is called
    so if anyone doesn't use the instance_of, and uses the SocialNetwork() directly,
    the __new__ will be called and the instance will be returned.
    Side Note:
    the super() method calls to the parent class (in this case, the object class)
    it then creates a new generic object of this class (SocialNetwork) and returns it as this instance
    '''
    def __new__(cls, name):
        # if the instance is not created yet, create it
        if cls._instance is None:
            # call the super class to create the instance
            cls._instance = super().__new__(cls)
            # name the social network
            cls._instance._name = name
            print("The social network " + cls._instance._name + " was created!")
        return cls._instance

    def __str__(self):
        string = f"{self._instance._name} social network:\n"
        for user in self._users:
            string += (f"User name: {user.get_username()}, Number of posts: {user.get_number_of_posts()},"
                       f" Number of followers: {user.get_number_of_followers()}\n")
        return string

    '''
    this is the method to sign up a new user
    it takes a username and a password
    it checks that the username is not already taken
    it checks that the password is between 4 and 8 characters
    if everything is ok, it creates the user and adds it to the list
    '''

    def sign_up(self, username, password):
        try:
            # check if the username is already taken
            if any(user.get_username() == username for user in self._users):
                raise ValueError("Username already taken\n")
            # check that password is between 4 and 8 characters
            if len(password) < 4 or len(password) > 8:
                raise ValueError("Password must be between 4 and 8 characters\n")
            # create the user and add it to the list
            user = User(username, password)
            self._users.append(user)
            # set the user to online, although it is not necessary because the default is online
            user.set_is_online(True)
            return user
        # if there is an error, print it and return None to indicate that the user was not created
        except ValueError as e:
            print(f"Error: {e}")
            return None

    '''
    this is the method to log out a user
    it takes a username and sets the user to offline
    '''

    def log_out(self, username):
        # find the user by the username
        user = next((user for user in self._users if user.get_username() == username), None)
        # if the user exists, log it out
        if user:
            user._is_online = False
            print(f"{username} disconnected")
        else:
            print("User not found")

    '''
    this is the method to log in a user
    it takes a username and a password
    it finds the user by the username
    if the user exists and the password is correct, it sets the user to online
    '''

    def log_in(self, username, password):
        # find the user by the username
        user = next((user for user in self._users if user.get_username() == username), None)
        # if the user exists and the password is correct, log it in
        if user and user.check_password(password):
            user._is_online = True
            print(f"{username} connected")
        else:
            print("Invalid username or password")
