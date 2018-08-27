# Password Locker
Moringa school core week 3 Friday IP to create a password locker.

## By: James Kageni

#### Description
This project contains a password locker. You can create a user with a username that will store your passwords.
the user can then add, copy or delete contacts from their account.

#### Installation and usage instructions

1. clone the repository using the url provided
2. check into the folder created by the cloning procedure
3. run: python3.6
4. run: from user import User
5. run: from user import Credentials
6. to create a new user run: name = User("name") where name is the username you want
7. to create a new credential run: acc = Credentials("acc", "password") where acc is the site name and password is your password
8. to save password run: acc.save_password() where acc is the account you had saved under
9. to check for all the passwords saved run: print(nam.account)


#### Known bugs

1. does not create a new instance of password list to every user
2. deletes all data on exit of the python instance

these bugs will be worked on much sooner than you think...

##### Thank you for visiting




This project is under an MIT [license](LICENSE)