# s=input()
# words=s.split()
# words.reverse()
# new_words=[]
# for word in words:
#     new_words.append(word.swapcase())
# result="".join(new_words)
# print(result)

class car:
    def __init__(self,max_speed,max_units):
        self.max_speed=max_speed
        self.max_units=max_units
    def __str__(self):
        return f"Car with maximum speed of {self.max_speed} abd the unit is {self.max_units}"