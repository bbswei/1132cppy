### CPPY HW1

'''
# Calculate the perimeter (sum of the three sides) of the triangle.
# Calculate the area (using Heron's formula) of the triangle. 𝐴 = 𝑠(𝑠 − 𝑎)(𝑠 − 𝑏)(𝑠 − 𝑐) , where 𝑠 = 1/2(𝑎 + 𝑏 + 𝑐)
# Classify the triangle based on the properties of its sides into one of the following types.
'''

def perimeter_calculator(side1, side2, side3):
    perimeter = side1 + side2 + side3
    return perimeter

def area_calculator(side1, side2, side3):
    s = (1/2) * perimeter_calculator(side1, side2, side3)
    area = (s * (s-side1) * (s-side2) * (s-side3))**(1/2)
    return round(area, 1)

def type_classifier(side1, side2, side3):
    if side1 == side2 == side3:
        type = "Equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        type = "Isosceles"
    else:
        type = "Scalene"
    return type


side1 = float(input())
side2 = float(input())
side3 = float(input())

import time
start_time = time.time()

print(f"Perimeter: {round(perimeter_calculator(side1, side2, side3), 1)}")
print(f"Area: {area_calculator(side1, side2, side3)}")
print(f"Type: {type_classifier(side1, side2, side3)} Triangle")

end_time = time.time()
print(f"--{end_time - start_time} seconds--")




