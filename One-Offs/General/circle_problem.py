"""
prompt:
    Given a point and a radius which designate a circle, return a random point
    within that circle.

"""

#Fun math
#The solution is a fun formula. I am hesitant to delve further into this since
#I would never be required to derive the Pythagoreas formula and customize it
#to a circle. I mean, it's logical IF AND ONLY IF you have been practicing math

#The magic formula is basically create a right angle triangle and one of the
#three points == our "rando" point. So we simply say:
#(x - x_center)^2 + (y - y_center) < radius^2
#see: https://www.veritasprep.com/blog/2016/10/how-to-use-the-pythagorean-theorem-with-a-circle/

#Low key though? I kind of miss math. It was beautiful and logical ONCE you got
#it. Until that point it is a tough nut to crack. But filled with Eureka
#moments and figuring out how to normalize variables for stuff

#So. Area of a circle == pi * r^2
#circumference == 2*r*pi

import math

def get_area(radius):
    return math.pi*(radius ** 2)

def get_circumference(radius):
    return math.pi*2*radius

def is_point_in_circle(point, center, radius):
    #Again, fun math stuff
    x, y = point
    x_center, y_center = center

    return ((x - x_center)**2 + (y - y_center)**2 < radius ** 2)

center = (1, 1)
point = (0, 0)
radius = 5

print(is_point_in_circle(point, center, radius))


