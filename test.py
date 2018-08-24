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

        self.new_User = User('Kageni')

    def test_init(self):
        """
        test case to see if the object initializes properly
        :return:
        """

        self.assertEqual(self.name, 'Kageni')

if __name__ == '__main__':
    unittest.main()