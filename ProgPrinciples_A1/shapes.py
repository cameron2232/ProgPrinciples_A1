import math

def circle(radius):
    if radius < 0: return None
    return math.pi * radius ** 2, 2 * math.pi * radius

def rectangle(width, height):
    if width < 0 or height < 0: return None
    return width * height, 2 * (width + height)

def shape_test():
    print(circle(3.33), circle(4.44), circle(-33.33))
    print(rectangle(3.3, 4.4), rectangle(1.2, 2.3), rectangle(-33.22, -22.11))

if __name__ == '__main__': # will be executed only when standalone   
    shape_test()