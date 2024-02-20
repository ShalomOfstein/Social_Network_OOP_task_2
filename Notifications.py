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
class NotificationFactory:
    @staticmethod
    def create_notification(notification_type, publisher, observer):
        if notification_type == "like":
            return LikeNotification(publisher, observer)
        elif notification_type == "comment":
            return CommentNotification(publisher, observer)
        elif notification_type == "new post":
            return NewPostNotification(publisher, observer)
        else:
            return None
