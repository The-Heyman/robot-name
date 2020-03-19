import string
import random


class Robot:

    name = "NG453"
    
    def __init__(self):
        self.robot_name()
        
        
    def reset(self):
        del self.name
        return self.name
        
    
    def robot_name(self):
        #code below generates the robot name
        pool = set()
        alpha = string.ascii_uppercase
        num = string.digits
        self.name = "".join((random.sample(alpha,2)) + random.sample(num,3))
        if self.name not in pool:
            pool.add(self.name)
            return self.name


