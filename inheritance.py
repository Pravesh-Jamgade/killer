
class Robot:
    def __init__(self, name):
        self.name = name
    
    def say_hi(self):
        print("Hi, I am "+ self.name+" !")

class PhysicianRobot(Robot):
    def __init__(self):
        Robot.__init__(self, "Phy ROBO")


x = Robot("Marvin")
y = PhysicianRobot()

# print(x, type(x))
# print(y, type(y))
y.say_hi()