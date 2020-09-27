from abc import ABC, abstractmethod

class Computer(ABC):
          
          
          def process(self):
                    return "Running"

          @abstractmethod
          def onlydeclare(self):
                    pass

class Laptop(Computer):
          
          def onlydeclare(self):
                    return "Done"


#obj=Computer()
#Abstract methods are like fill in the blanks as Child class inherits Parent abstract class the abstract methods are needed to be defined.

obj1=Laptop()
print(obj1.onlydeclare())
print(obj1.process())


'''
Method which is decorated with @abstractmethod and does not have any definition.
Python Don't support Abstract class, So we have ABC(abstract Base Classes) Module, so we can use here to achieve abstract classes and will see what is abstract class and why we need it.
An abstract class can be considered as a pattern for other classes. A class which contains one or more abstract methods is called an abstract class. An abstract method is a method that has a declaration but does not have an implementation.
'''
