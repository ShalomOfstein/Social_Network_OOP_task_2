from Post import Post, PostFactory
from Notifications import *


class User:
    """
    this is the class for the users.
    the users have a username, a password, a list of followers, a list of following, a list of posts,
    a list of notifications, and a boolean to indicate if they are online
    """

    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._followers = []
        self._following = []
        self._posts = []
        self.notifications = []
        self._is_online = True

    def __str__(self):
        return (f"User name: {self.get_username()}, Number of posts: {self.get_number_of_posts()}"
                f", Number of followers: {self.get_number_of_followers()}")

    #########################################################################################
    # getters and setters

    def get_username(self):
        return self._username

    def get_followers(self):
        return self._followers

    def get_number_of_followers(self):
        return len(self._followers)

    def get_number_of_posts(self):
        return len(self._posts)

    ''' this is the method to check if the password given is the same as the user's password '''
    def check_password(self, password):
        return self._password == password

    def get_is_online(self):
        return self._is_online

    def set_is_online(self, is_online):
        self._is_online = is_online

    #########################################################################################
    # follow and unfollow methods

    '''
    this method is used to follow a different user
    if the user is already following the other user, it does nothing
    if the user is not following the other user, it adds the other user to the following list
    it does all of this only if the user is online
    '''
    def follow(self, user):
        if self._is_online:
            if user in self._following:
                return

            self._following.append(user)
            print(f"{self.get_username()} started following {user.get_username()}")
            user.get_followers().append(self)

    '''
    this method is used to unfollow a different user
    if the user is not following the other user, it does nothing
    if the user is following the other user, it removes the other user from the following list
    it does all of this only if the user is online
    '''
    def unfollow(self, user):
        if self._is_online:
            if user in self._following:
                self._following.remove(user)
                user.get_followers().remove(self)
                print(f"{self.get_username()} unfollowed {user.get_username()}")

    #########################################################################################
    # publish post method and notify followers

    '''
    this method is used to publish a new post
    it takes the type of the post and the content and creates the post using the PostFactory class
    it adds the post to the list of posts that each user has
    it then creates a post notification for each follower and sends it using the notify method
    all of this only if the user is online
    '''
    def publish_post(self, post_type, *args):
        try:
            if self._is_online:
                post = PostFactory.create_post(self, post_type, *args)
                self._posts.append(post)
                for follower in self._followers:
                    notification = NewPostNotification(self._username, follower)
                    follower.notify(notification)
                return post
        except Exception as e:
            print(f"Error: {e}")
            return None

    '''
    this is the method to notify the user
    it implements the Observer pattern
    it takes a notification and adds it to the list of notifications of the receiver
    '''
    def notify(self, notification):
        self.notifications.append(notification)

    '''
    this is the method to print all the notifications of the user
    '''
    def print_notifications(self):
        print(f"{self.get_username()}'s notifications:")
        for notification in self.notifications:
            print(notification)
