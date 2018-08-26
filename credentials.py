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

    def save_password(self):
        """
        saving the passwords
        :return:
        """

        # Credentials.password_list.add(self)
        print("enter the account")
        account = input()

        print("enter the password")
        password = input()

        Credentials.password_list[account] = password
        print(self.password_list)

        # print(password_list)



