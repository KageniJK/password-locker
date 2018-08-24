class User:
    """
    A class to create all instances of the users
    """

    user_list = []

    def __init__(self, name):
        """
        defining the properties of the user class
        """
        self.name = name

    def save_user(self):
        """
        saving the contacts created
        :return:
        """

        User.user_list.append(self)
