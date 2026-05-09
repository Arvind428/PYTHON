class course:

    def __init__(self,name,rno):
        self.name = name
        self.rno = rno

car1 = course("shriya","123")#project assign
car2=course("arvind","24")
print(car1.name, car1.rno)#external
print(car2.name,car2.rno)

# class course:
#     pass

# car1 = course()
# car1.name = "shriya"
# car1.rno = "123"

# car2 = course()
# car2.name = "arvind"
# car2.rno = "24"

# print(car1.name, car1.rno)
# print(car2.name, car2.rno)