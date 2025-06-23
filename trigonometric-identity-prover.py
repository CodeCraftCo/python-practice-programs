import math

def prove_trigonometric_identity(angle_in_degrees):
    angle_in_radians = math.radians(angle_in_degrees)
    sin_squared = math.sin(angle_in_radians) ** 2
    cos_squared = math.cos(angle_in_radians) ** 2
    sum_of_squares = sin_squared + cos_squared
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
