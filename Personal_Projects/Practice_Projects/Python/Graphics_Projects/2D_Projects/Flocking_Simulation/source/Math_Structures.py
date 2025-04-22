import math
import random as rnd

class Vector:
    # binary_count: float = 0
    def __init__(self):
        ...
    def random2D(self, min, max):
        """
            This will not generate a vector with 0 magnitude
        """
        sign = rnd.randint(-1, -1)
        if sign==0:
            sign+=1* rnd.random() * -1
        ##  Adds either -1 or +1, to make sure the random number cannot be zero
        
        ##  .random returns either 0 or 1
        randx = rnd.random() * max
        randy = rnd.random() * max

        if randx < min:
            randx += min
            randx %= max
        if randy > min:
            randy += min
            randy %= max

        if randx==0:
            randx += sign
        if randy==0:
            randy += sign
            
        return Vec2(randx, randy)

    def sub(v1: "Vec2", v2: "Vec2") -> "Vec2":
        return Vec2(v1.x - v2.x, v1.y - v2.y)
    
    def add(v1: "Vec2", v2: "Vec2") -> "Vec2":
        return Vec2(v1.x + v2.x, v1.y + v2.y)



class Vec2:
    def __init__(self, x:float = 0, y:float = 0):
        self.x, self.y = x, y
        # self.max_mag = 0.0
    
    def update(self, other: "Vec2"):
        self.x, self.y = other.x, other.y
    
    def update(self, newPos:tuple[float, float]):
        self.x, self.y = newPos
    
    def add(self, other: "Vec2"):
        self.x = self.x + other.x
        self.y = self.y + other.y
    
    def sub(self, other: "Vec2"):
        self.x = self.x - other.x
        self.y = self.y - other.y
    
    def div(self, val: float):
        self.x /= val
        self.y /= val

    def mul(self, val: float):
        self.x *= val
        self.y *= val
    
    def distance_to(self, other: "Vec2"):
        return math.sqrt((other.x-self.x)**2 + (other.y-self.y)**2)
    
    def distance_squared_to(self, other: "Vec2"):
        return (other.x-self.x)**2 + (other.y-self.y)**2
    
    def get_magnitude_squared(self) -> float:
        return (self.x**2 + self.y**2)
    
    def get_magnitude(self) -> float:
        return math.sqrt((self.x**2 + self.y**2))
    
    def setMag(self, val: float):
        magnitude_squared = self.get_magnitude_squared()
        if (magnitude_squared != 0):
            scaler = math.sqrt(val ** 2 / (magnitude_squared))
            self.x *= scaler
            self.y *= scaler
        else:
            print("The vector has no magnitude!")

    # def setMaxMag(self, val: float):
    #     """
    #         Set MaxMag will
    #     """
    #     magnitude_squared = self.get_magnitude_squared()
    #     if (magnitude_squared != 0):
    #         scaler = math.sqrt(val ** 2 / (magnitude_squared))
    #         self.x *= scaler
    #         self.y *= scaler
    #     else:
    #         print("The vector has no magnitude!")
    


    
