import random
import string
from typing import Dict, Any


class User:
    """
    A class to create all instances of the users
    """

    user_list = {}

    def __init__(self, name):
        """
        defining the properties of the user class
        """
        self.name = name
        self.accounts = Credentials.password_list


    def save_user(self):
        """
        saving the contacts created
        :return:
        """

        User.user_list[self.name] = self.accounts

        print(self.accounts)

    def add_password(self):
        """
        adding the passwords to the user
        :return:
        """

        User.accounts = Credentials.password_list

class Credentials:
    """
    Class that generates new instances of passwords
    """

    password_list: Dict = {}

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

        Credentials.password_list[self.account] = self.password
        User.add_password(self)


    def generate(size=6, chars=string.ascii_uppercase + string.digits):
        """
        generates new random password
        :return:
        """

        return ''.join(random.choice(chars) for _ in range(size))
