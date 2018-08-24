class Credentials:
    """
    Class that generates new instances of passwords
    """

    password_list = []

    def __init__(self, account, password):
        """
        defining the properties of the class Credentials
        """

        self.account = account
        self.password = password

    def save_password(self):
        """
        saving the passwords
        :return:
        """

        Credentials.password_list.append(self)