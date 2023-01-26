#!/usr/bin/python3
"""
User class
"""


class User():
    """ Documentation """

    def __init__(self):
        """ Documentation """
        self._email = None

    @property
    def email(self):
        """ Documentation """
        return self._email

    @email.setter
    def email(self, value):
        """ Documentation """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self._email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
