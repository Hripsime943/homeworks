import math
def can_of_wall (height, weight, caverage=5):
    can = weight * height / caverage
    return math.ceil(can)

test_h = int(input("enter height: "))
test_w = int(input("enter weight: "))
cans_needed = can_of_wall(height=test_h, weight=test_w)
print (cans_needed)