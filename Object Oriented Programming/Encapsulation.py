# Encapsulation in Python

'''

The object variable should not always be directly acessible.
To prevent accidently change an objects variable can sometimes only be changed with an objects methods.

Python does not have the private keyword, unlike other programming languages, but encapsulation can be done.
Instead, it relies on the convention: a class variable that should not directly be accessed should be prefixed with an underscore.

'''


class Robot:

    def __init__(self):
        print("In class Robot")
        self.robot = 123 
        self._robot1 = 124
        self.__robot2 = 125

    def get__robot(self):
        return self.__robot2

    def set__robot(self, number):
        self.__robot2 = number


obj = Robot()
print(obj.robot)
print(obj._robot1)
print(obj.get__robot())

obj.set__robot(130)
print(obj.get__robot())
# print(obj.__robot2) : This will result in an atribute error

'''
A single underscore: Private Variable, it should not be accessed directly. But nothing stops you from doing that (except convention)
A double underscore: Private variable, harder to access but still possible.
'''
