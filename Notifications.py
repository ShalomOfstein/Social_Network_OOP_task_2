'''
class Notification:
this class is the base class for all notifications
each notification has a type, a publisher, and an observer
the type is a string that can be "like", "comment", or "new post"
it implements the Observer pattern because each user has a notify method that
takes a notification and adds it to the list of notifications
this design also implements the scalability principle because it is easy to add new types of notifications
'''


class Notification:
    def __init__(self, notification_type, publisher, observer):
        self._notification_type = notification_type
        self._publisher = publisher
        self._observer = observer


################################################################################################
class LikeNotification(Notification):
    def __init__(self, publisher, observer):
        super().__init__("like", publisher, observer)

    def __str__(self):
        return f"{self._observer.get_username()} liked your post"


################################################################################################
class CommentNotification(Notification):
    def __init__(self, publisher, observer):
        super().__init__("comment", publisher, observer)

    def __str__(self):
        return f"{self._observer.get_username()} commented on your post"


################################################################################################
class NewPostNotification(Notification):
    def __init__(self, publisher, observer):
        super().__init__("new post", publisher, observer)

    def __str__(self):
        return f"{self._publisher} has a new post"


################################################################################################

'''
this is an unused class that i created to implement the factory pattern
the factory pattern is used to create objects without specifying the exact class of object that will be created
but because each notification is created in a different place in the code, and at after a different action,
there is no need for a factory pattern
but if we need for some reason to have a way to send a notification without knowing the exact type of the notification,
this could be a good way to do it
'''

# class NotificationFactory:
#     @staticmethod
#     def create_notification(notification_type, publisher, observer):
#         if notification_type == "like":
#             return LikeNotification(publisher, observer)
#         elif notification_type == "comment":
#             return CommentNotification(publisher, observer)
#         elif notification_type == "new post":
#             return NewPostNotification(publisher, observer)
#         else:
#             return None
