# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides, determine if the triangle is
# equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).

Len_Side1 = float(input("Enter the length of 1st side: "))
Len_Side2 = float(input("Enter the length of 2nd side: "))
Len_Side3 = float(input("Enter the length of 3rd side: "))

if Len_Side1 == Len_Side2 == Len_Side3:
    print("Triangle is equilateral triangle ")
elif Len_Side1 == Len_Side2 or Len_Side2 == Len_Side3 or Len_Side1 == Len_Side3:
    print("Triangle is isosceles triangle")
else:
    print("Triangle is scalene triangle")
