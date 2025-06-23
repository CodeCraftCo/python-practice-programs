import math

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

def calculate_rectangle_area(length, width):
    return length * width

def main():
    # Circle input
    circle_radius = float(input("Enter circle radius in cm: "))
    circle_area = calculate_circle_area(circle_radius)
    print(f"Area of circle: {circle_area:.2f} sq cm")

    # Rectangle input
    rectangle_length = float(input("Enter rectangle length in cm: "))
    rectangle_width = float(input("Enter rectangle width in cm: "))
    rectangle_area = calculate_rectangle_area(rectangle_length, rectangle_width)
    print(f"Area of rectangle: {rectangle_area:.2f} sq cm")

    # Compare areas
    if circle_area > rectangle_area:
        print("Circle area is greater")
    elif circle_area < rectangle_area:
        print("Rectangle area is greater")
    else:
        print("Both areas are equal")

if __name__ == "__main__":
    main()