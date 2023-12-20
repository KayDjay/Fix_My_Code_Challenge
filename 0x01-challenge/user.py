#!/usr/bin/python3
""" 
This is a user module
"""

class User():
    """ User class """

    def __init__(self):
        """ This is init function """
        self.__email = None

    @email.setter
    def email(self, value):
        """ To set email value """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value

    @property
    def email(self):
        """ Email Function"""
        return self.__email
   
    
if __name__ == "__main__":

    u = User()
    u.email = "shametlab@gmail.com"
    print(u.email)
