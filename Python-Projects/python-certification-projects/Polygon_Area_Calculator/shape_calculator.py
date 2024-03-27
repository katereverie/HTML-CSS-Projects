class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height 
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    def get_picture(self):
        if self.width > 50 or self.height > 50:
           return "Too big for picture."
        return ("*" * self.width + "\n") * self.height
    def get_amount_inside(self, shape):
        return int(self.width / shape.width) * int(self.height / shape.height)
    # if an instance of Rectangle is represented as a string, it should look like: Rectangle(width=5, height=10)
    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    
class Square(Rectangle):
  # side - 边长
    def __init__(self, side):
        super().__init__(side, side)
    def set_width(self, side):
        self.width = side
        self.height = side
    def set_height(self, side):
        self.width = side
        self.height = side
    def set_side(self, side):
        self.width = side
        self.height = side
    def __str__(self):
        return "Square(side=" + str(self.width) + ")"
