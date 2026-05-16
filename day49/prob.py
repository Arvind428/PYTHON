#create a parent class animal havving sound as a method, child class dog having sound as a method
class Animal:
    def sound(self):
        print("Animal is shouting")
class dog(Animal):
    def sound(self):
        print("Dog is shouting")
d1=dog()
d1.sound()

#p-payment, ch-upi, ch-card---method=pay(self, amnt)
class payment:
    def pay(self,amnt):
        print("Select Payment method")
        print("amount",amnt)
class upi(payment):
    def pay(self,amnt):
        print("Selected upi:")
        print("amount paid",amnt)
class card(payment):
    def pay(self,amnt):
        print("Selected card:")
        print("amount paid",amnt)
u=upi()
c=card()
u.pay(100)
c.pay(560)

#p-employ, ch- developer, ch- manager classes---work method

class employ:
    def rule(self,id):
        print("have to wear id")
        print("your id is",id)
class developer(employ):
    def rule(self,id):
        print("have to wear the developer id")
        print("your id is",id)
        if id=="developer":
            print("you have the access for the code snippet")
        print("does not have access ofdeveloper perks")
class manager(employ):
    def rule(self,id):
        print("have to wear the manager id")
        print("your id is",id)
        if id=="manager":
            print("have the connection of all the employees")
        print("does not have the access of manager perks")
e=employ()
d=developer()
m=manager()
e.rule("employ")
d.rule("developer")
m.rule("manager")