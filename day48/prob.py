#problem 2
class Animal:
    def wild(self):
        print("animal is shouting")
class pet(Animal):
    def dog(self):
        print("bow")
class sound(Animal):
    def cat(self):
        print("meow")    
d1=pet()   
d1.wild()    
d1.dog()       
d2=sound() 
d2.wild()  
d2.cat()