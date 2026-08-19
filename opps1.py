class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        return self.base + self.height + (self.base**2 + self.height**2)**0.5

class EquilateralTriangle(Triangle):
    

    def __init__(self, side):
        
        # super().__init__(side, (3**0.5 / 2) * side)
        self.side = side
        self.height = (3**0.5 / 2) * side
        self.base = side
    # def area(self):
    #         return 0.5 * self.side * (3**0.5 / 2) * self.side

    def perimeter(self):
        return 3 * self.side
    
    def __str__(self):
            return f"Equilateral Triangle with side {self.side}"
    
triangle_area = EquilateralTriangle(3)

print("Area of the equilateral triangle:", triangle_area.area())
print("Perimeter of the equilateral triangle:", triangle_area.perimeter())

#print("Height of the equilateral triangle:", triangle_area.height)

print(triangle_area)