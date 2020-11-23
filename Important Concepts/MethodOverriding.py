class Dog :
    def Bark (self):
        print("woof")

class AngryDog (Dog):
    def Bark (self):
        print("Angry Bark")

AngryDog().Bark()
