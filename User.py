from Post import Post, PostFactory
from Notifications import *


class User:

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

    def get_password(self):
        return self._password

    #########################################################################################
    # follow and unfollow methods
    def follow(self, user):
        if self._is_online:
            if user in self._following:
                return

            self._following.append(user)
            print(f"{self.get_username()} started following {user.get_username()}")
            user.get_followers().append(self)

    def unfollow(self, user):
        if self._is_online:
            if user in self._following:
                self._following.remove(user)
                user.get_followers().remove(self)
                print(f"{self.get_username()} unfollowed {user.get_username()}")

    #########################################################################################
    # publish post method and notify followers
    def publish_post(self, post_type, *args):
        post = PostFactory.create_post(self, post_type, *args)
        self._posts.append(post)
        for follower in self._followers:
            notification = NewPostNotification(self._username, follower)
            follower.notify(notification)
        return post

    def notify(self, notification):
        self.notifications.append(notification)

    def print_notifications(self):
        print(f"{self.get_username()}'s notifications:")
        for notification in self.notifications:
            print(notification)
