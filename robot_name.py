import string
import random
class Robot:
    def __init__(self, name=None, reset= None):
        self.name = name
        self.reset = reset
        
    
    def robot_name(self):
        #code below generates the robot name
        pool = set()
        alpha = string.ascii_uppercase
        num = string.digits
        self.name = "".join((random.sample(alpha,2)) + random.sample(num,3))
        if self.name not in pool:
            pool.add(self.name)
            
        return self.name
#bot_D = Robot()
#print(bot_D.robot_name())
