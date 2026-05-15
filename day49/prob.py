#create a parent class animal havving sound as a method, child class dog having sound as a method
class Animal:
    def sound(self):
        print("Animal is shouting")
class dog(Animal):
    def sound(self):
        print("Dog is shouting")
d1=dog()
d1.sound()