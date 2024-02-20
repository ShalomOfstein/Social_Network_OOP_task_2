import matplotlib.pyplot as plt
from Notifications import *

"""
this is the file that contains the classes for the posts and the factory class to create the posts
the Post class is the parent class for the TextPost, ImagePost, and SalePost classes
the PostFactory class is used to create the posts by the User class with only the type and the content
"""


# todo: show image in ImagePost

########################################################################################
# this is the parent class for the posts
# all the posts have an owner, likes, and comments
# the owner is the user that created the post
class Post:
    def __init__(self, owner, post_type):
        self._owner = owner
        self._type = post_type
        self._likes = []
        self._comments = []

    # this is the method to like the post
    # it adds the user to the likes list
    def like(self, user):
        if user == self._owner:
            return
        else:
            if user not in self._likes:
                self._likes.append(user)
                notification = LikeNotification(self._owner.get_username(), user)
                self._owner.notify(notification)
                print(f"notification to {self._owner.get_username()}: {user.get_username()} liked your post")

    # this is the method to add a comment to the post
    # it adds the user and the text to the comments list
    def comment(self, user, text):
        self._comments.append((user, text))
        notification = CommentNotification(self._owner.get_username(), user)
        self._owner.notify(notification)
        print(f"notification to {self._owner.get_username()}: {user.get_username()} commented on your post: {text}")


#######################################################################################
# this is the class for the text posts
class TextPost(Post):

    def __init__(self, owner, content):
        super().__init__(owner, "Text")
        self._content = content
        self.display()

    def __str__(self):
        return f"{self._owner.get_username()} published a post:\n\"{self._content}\"\n"

    def display(self):
        print(self._owner.get_username() + " published a post:\n\"" + self._content + "\"")
        print()


########################################################################################
# this is the class for the image posts
class ImagePost(Post):

    def __init__(self, owner, content):
        super().__init__(owner, "Image")
        self._content = content
        print(self)

    def __str__(self):
        return f"{self._owner.get_username()} posted a picture\n"

    def display(self):
        print("Shows picture")
        # plt.imshow(self._content)


########################################################################################
# this is the class for the sale posts
class SalePost(Post):

    def __init__(self, owner, title, price, location):
        super().__init__(owner, "Sale")
        self._title = title
        self._price = price
        self._location = location
        self._sold = False
        print(self)

    def __str__(self):
        string = self._owner.get_username() + " posted a product for sale:\n"
        if self._sold:
            return string + f"Sold! {self._title}, price: {str(self._price)}, pickup from: {self._location}\n"
        else:
            return string + ("For sale! " +
                             self._title + ", price: " + str(self._price) + ", pickup from: " + self._location)+"\n"

    def display(self):
        if not self._sold:
            print(self._owner.get_username() + " posted a product for sale:\nFor sale! " +
                  self._title + ", price: " + str(self._price) + ", pickup from: " + self._location)
        else:
            print(f"Sold! {self._title}, price: {str(self._price)}, pickup from: {self._location}")
        print()

    def sold(self, password):
        if not self._sold:
            if self._owner.get_password() == password:
                self._sold = True
                print(self._owner.get_username() + "'s product is sold")

    def discount(self, percent, password):
        if not self._sold:
            if self._owner.get_password() == password:
                self._price *= (1 - percent / 100)
                print("Discount on " + self._owner.get_username() + " product! the new price is: " + str(self._price))


########################################################################################################
# this is the factory class to create the posts
# it has a static method to create the posts by the type and the content
class PostFactory:
    @staticmethod
    def create_post(owner, type, *args):
        if type == "Text":
            return TextPost(owner, *args)
        elif type == "Image":
            return ImagePost(owner, *args)
        elif type == "Sale":
            return SalePost(owner, *args)
        else:
            raise Exception("Invalid post type")
