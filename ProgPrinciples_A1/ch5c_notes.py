# Functions - 3/3

# Topic 1 - math module
# - contains some code for doing math
# - two constants: pi and e
# - trigonometry functions, sin, cos, asin, acos, tan
#       degrees (30, 45, 90, 180, 360)
#       radians (pi/6, pi/4, pi/2, pi, 2*pi)
# - exponents: (**) pow, exp, log, log10, sqrt
# - rounding: (round), ceil, floor


import math
import shapes

def math_tester():
    print(f'pi is {math.pi}, e is {math.e}')
    angle = 90
    print(f'sin of {angle} degrees is {math.sin(math.radians(angle))}')
    arc = math.pi / 6 
    print(f'sin of pi/6 is {math.sin(arc)}')
    
    a = math.e ** 5
    print(f'log of a is {math.log(a)}')
    b = 1000000
    print(f'log10 of b is {math.log10(b)}')
    
    print(f'{math.ceil(1.11)}, {math.ceil(2.99)}') # 2, 3
    print(f'{math.floor(1.11)}, {math.floor(2.99)}') # 1, 2
    print(f'{math.ceil(-1.11)}, {math.ceil(-2.99)}') # -1, -2
    print(f'{math.floor(-1.11)}, {math.floor(-2.99)}') # -2, -3
    
# Topic 2 - Modules
#   - A file named xxx.py containing code for reusing
#   - To use the code, import the module first
#   - When imported, code in module will be executed
#       - Module can be standalone or import
#       - Standalone: name '__main__'
#       - Import: name of the file

def my_app():
    radius = 234.234
    area, perimeter = shapes.circle(radius)
    print(f'Circle: {area}, {perimeter}')
    width, height = 234.234, 978.324
    area, perimeter = shapes.rectangle(width,height)
    print(f"Rectangle: {area}, {perimeter}")

def main():
    math_tester()
    my_app()
    pass

if __name__ == '__main__':
    main()


#=============================================================================================================


# Midterm review




# Quiz 2