import math


def get_func(ls):
    result = []

    def circle_area(radius):
        return radius * radius * math.pi

    def square_area(edge):
        return edge * edge

    def rectangle_area(width, height):
        return width * height

    def triangle_area(height, qaede):
        return height * qaede * 0.5

    for i in ls:
        if i == 'circle':
            result.append(circle_area)
        elif i == 'square':
            result.append(square_area)
        elif i == 'rectangle':
            result.append(rectangle_area)
        elif i == 'triangle':
            result.append(triangle_area)

    return result
