#!/usr/bin/python3
""" This is square Module """


class Square():
    """ This is a Square class """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """init function """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square function """
        return self.width * self.height

    def permiter_of_my_square(self):
        """permiter of my square function """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """str function """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
