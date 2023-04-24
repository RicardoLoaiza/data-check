"""Dummy challenge for Kitt Demo"""



def circle_area(radius):
    """Returns the area of the circle of given radius"""
    #YOUR CODE HERE
    result = radius * radius * (3.1416)
    if radius < 0:
        return 0
    return result
