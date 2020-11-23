class Dog :
    def Bark (self):
        print("woof")

class AngryDog (Dog):
    def Bark (self, num):
        for i in range (num):
            print("woof")


AngryDog().Bark(7)