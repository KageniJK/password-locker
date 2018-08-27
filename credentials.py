from typing import Dict, Any
import random
import string
# from runner import Runner


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

        Credentials.password_list[Credentials.account] = Credentials.password


    def generate(size=6, chars=string.ascii_uppercase + string.digits):
        """
        generates new random password
        :return:
        """

        return ''.join(random.choice(chars) for _ in range(size))


