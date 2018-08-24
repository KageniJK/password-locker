import unittest
from user import User


class TestLocker(unittest.TestCase):
    """
    TestLocker class to test the functionality of the app
    """

    def setUp(self):
        """
        setup of the class to test against
        :return:
        """

        self.new_user = User('Kageni')

    def test_init(self):
        """
        test case to see if the object initializes properly
        :return:
        """

        self.assertEqual(self.new_user.name, 'Kageni')

    def test_save(self):
        """
        test case for saving an object of type user
        :return:
        """

        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


if __name__ == '__main__':
    unittest.main()
