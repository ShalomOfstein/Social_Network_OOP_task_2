import matplotlib.pyplot as plt
from Notifications import *

"""
this is the file that contains the classes for the posts and the factory class to create the posts
the Post class is the parent class for the TextPost, ImagePost, and SalePost classes
the PostFactory class is used to create the posts by the User class with only the type and the content
"""

########################################################################################
'''
this is the parent class for the posts
all the posts have an owner, likes, and comments
the owner is the user that created the post
'''


class Post:
    def __init__(self, owner, post_type):
        self._owner = owner
        self._type = post_type
        self._likes = []
        self._comments = []

    '''
    this is the method to like the post
    it adds the user to the likes list
    '''

    def like(self, user):
        if user.get_is_online():
            # if the user is the owner of the post, it does nothing
            if user == self._owner:
                return
            else:
                # if the user is not in the likes list, it adds it and sends a notification to the owner
                if user not in self._likes:
                    self._likes.append(user)
                    notification = LikeNotification(self._owner.get_username(), user)
                    self._owner.notify(notification)
                    # logs the action of the notification being sent
                    print(f"notification to {self._owner.get_username()}: {user.get_username()} liked your post")

    '''
    this is the method to add a comment to the post
    it adds the user and the text to the comments list
    '''

    def comment(self, user, text):
        if user.get_is_online():
            self._comments.append((user, text))
            notification = CommentNotification(self._owner.get_username(), user)
            self._owner.notify(notification)
            # logs the action of the notification being sent
            print(f"notification to {self._owner.get_username()}: {user.get_username()} commented on your post: {text}")


#######################################################################################
# this is the class for the text posts
class TextPost(Post):

    def __init__(self, owner, content):
        super().__init__(owner, "Text")
        self._content = content
        print(self)

    def __str__(self):
        return f"{self._owner.get_username()} published a post:\n\"{self._content}\"\n"


########################################################################################
# this is the class for the image posts
class ImagePost(Post):

    def __init__(self, owner, content):
        super().__init__(owner, "Image")
        self._content = content
        print(self)

    def __str__(self):
        return f"{self._owner.get_username()} posted a picture\n"

    '''
    this is the method to display the image of the post
    we use the matplotlib library to show the image
    '''

    def display(self):
        print("Shows picture")
        try:
            img = plt.imread(self._content)
            plt.imshow(img)
            plt.axis('off')
            plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
            plt.show()
        except Exception as e:
            print(f"Error displaying the image: {e}")


########################################################################################
'''
this is the class for the sale posts
the sale post is a bit more complex in that it has more attributes and methods
it has a title, price, location, and a boolean to indicate if it is sold
we can also discount the price of the product and mark it as sold
'''


class SalePost(Post):

    def __init__(self, owner, title, price, location):
        super().__init__(owner, "Sale")
        self._title = title
        self._price = price
        self._location = location
        self._sold = False
        print(self)

    '''
    in the __str__ method, we return a string with the information of the post
    note that the information is different if the product is sold or not
    '''

    def __str__(self):
        string = self._owner.get_username() + " posted a product for sale:\n"
        if self._sold:
            return string + f"Sold! {self._title}, price: {str(self._price)}, pickup from: {self._location}\n"
        else:
            return string + ("For sale! " +
                             self._title + ", price: " + str(self._price) + ", pickup from: " + self._location) + "\n"

    '''
    this is the method to mark the product as sold
    it takes a password to verify that the user is the owner of the product
    '''

    def sold(self, password):
        if not self._sold:
            if self._owner.check_password(password):
                self._sold = True
                print(self._owner.get_username() + "'s product is sold")

    '''
    this is the method to discount the price of the product
    it takes a percent and a password to verify that the user is the owner of the product
    '''

    def discount(self, percent, password):
        if not self._sold:
            if self._owner.check_password(password):
                self._price *= (1 - percent / 100)
                print("Discount on " + self._owner.get_username() + " product! the new price is: " + str(self._price))


########################################################################################################
'''
this is the factory class to create the posts
it implements the Factory design pattern
it has a static method to create the posts by the type and the content
the static method returns the post created or raises an exception if the type is invalid
'''


class PostFactory:
    @staticmethod
    def create_post(owner, post_type, *args):
        if post_type == "Text":
            return TextPost(owner, *args)
        elif post_type == "Image":
            return ImagePost(owner, *args)
        elif post_type == "Sale":
            return SalePost(owner, *args)
        else:
            raise Exception("Invalid post type\n")
