from credentials import Credentials



class Runner:
    """
    Class to run all functions to merge the two other classes
    """

    def __init__(self):
        """
        init function
        """

        self.new_password = Credentials.save_password('fb', 'password')
        # self.new_password.Credentials.)
        print(Credentials.password_list)
