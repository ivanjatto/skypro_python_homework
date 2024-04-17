import math 
def square(side):
    
    if isinstance(side, int):
        
        return side ** 2
    else:
        
        return math.ceil(side ** 2)


side_length = 3.5
area = square(side_length)
print(f"Площадь квадрата со стороной {side_length} равна {area}")