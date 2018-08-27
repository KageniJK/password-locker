from typing import Dict, Any


class Credentials:
    """
    Class that generates new instances of passwords
    """

    password_list: Dict[Any, Any] = {}

    def __init__(self, account, password):
        """
        defining the properties of the class Credentials
        """

        self.account = account
        self.password = password

    # def enter_password(self):
    #     """
    #     entering the account and password
    #     :return:
    #     """
    #
    #     print("enter the account")
    #     self.account = input()
    #
    #     print("enter the password")
    #     self.password = input()

    def save_password(self, account, password):
        """
        saving the passwords
        :return:
        """
        self.account = account
        self.password = password

        Credentials.password_list[account] = password
