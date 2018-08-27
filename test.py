import unittest
from user import User
from credentials import Credentials

class testPasswords(unittest.TestCase):
    """
    Test class to test the functionality of the Passwords class
    """

    def setUp(self):
        """
        test case for testing whether the passwords initialize properly
        :return:
        """

        self.new_password = Credentials("instagram", "Password")

    def test_init(self):
        """
        test to see whether the password initializes properly
        """

        self.assertEqual(self.new_password.account, "instagram")
        self.assertEqual(self.new_password.password, "Password")

    def test_save(self):
        """
        test to check whether the password saves
        :return:
        """

        self.new_password.save_password()
        self.assertEqual(len(Credentials.password_list), 1)


class TestUser(unittest.TestCase):
    """
    TestLocker class to test the functionality of the user class
    """

    def setUp(self):
        """
        setup of the class to test against
        :return:
        """

        self.new_user = User('Kageni')
        self.new_user1 = User('James')

    def test_init(self):
        """
        test case to see if the object initializes properly
        :return:
        """

        self.assertEqual(self.new_user.name, 'Kageni', {})
        self.assertEqual(self.new_user1.name, 'James')

    def test_save(self):
        """
        test case for saving an object of type user
        :return:
        """

        self.new_user.save_user()
        self.new_user1.save_user()
        self.assertEqual(len(User.user_list), 2)
        print(User.user_list)


if __name__ == '__main__':
    unittest.main()
