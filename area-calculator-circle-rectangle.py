import math

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

def calculate_rectangle_area(length, width):
    return length * width

def main():
    print("Enter shape details:")
    shape = input("Enter shape (circle/rectangle): ")
    
    if shape.lower() == "circle":
        radius = float(input("Enter radius in cm: "))
        area = calculate_circle_area(radius)
        print(f"Area of circle: {area:.2f} sq cm")
    elif shape.lower() == "rectangle":
        length = float(input("Enter length in cm: "))
        width = float(input("Enter width in cm: "))
        area = calculate_rectangle_area(length, width)
        print(f"Area of rectangle: {area:.2f} sq cm")
    else:
        print("Invalid shape")
        return
    
    # Compare areas
    circle_area = calculate_circle_area(5)
    rectangle_area = calculate_rectangle_area(5, 5)
    print(f"\nArea of circle with 5cm radius: {circle_area:.2f} sq cm")
    print(f"Area of rectangle with 5cm side: {rectangle_area:.2f} sq cm")
    
    if circle_area > rectangle_area:
        print("Circle area is greater")
    elif circle_area < rectangle_area:
        print("Rectangle area is greater")
    else:
        print("Both areas are equal")

if __name__ == "__main__":
    main()