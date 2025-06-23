#A Python program that calculates sine and cosine for a given angle and verifies the trigonometric identity sin²(x) + cos²(x) = 1.

import math

def prove_trigonometric_identity(angle_in_degrees):
    angle_in_radians = math.radians(angle_in_degrees)
    sin_value = math.sin(angle_in_radians)
    cos_value = math.cos(angle_in_radians)
    sin_squared = sin_value ** 2
    cos_squared = cos_value ** 2
    sum_of_squares = sin_squared + cos_squared

    print(f"sin({angle_in_degrees}) = {sin_value:.2f}")
    print(f"cos({angle_in_degrees}) = {cos_value:.2f}")
    print(f"sin^2({angle_in_degrees}) + cos^2({angle_in_degrees}) = {sum_of_squares:.2f}")

    if math.isclose(sum_of_squares, 1):
        print("Proved: sin^2(x) + cos^2(x) = 1")
    else:
        print("Failed to prove: sin^2(x) + cos^2(x) = 1")

def main():
    angle_in_degrees = float(input("Enter an angle in degrees: "))
    prove_trigonometric_identity(angle_in_degrees)

if __name__ == "__main__":
    main()