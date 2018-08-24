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


if __name__ == '__main__':
    unittest.main()
