def get_gender():
    while True:
        print("Enter your gender:")
        print("1. Male")
        print("2. Female")
        choice = input("Enter your choice (1/2): ")
        match choice:
            case "1":
                return "male"
            case "2":
                return "female"
            case _:
                print("Invalid choice. Please enter 1 for male or 2 for female.")

def get_age(gender):
    while True:
        try:
            age = int(input(f"Enter your age ({gender}): "))
            if gender == "male" and age < 21:
                print("Males below 21 are not eligible for marriage.")
            elif gender == "female" and age < 18:
                print("Females below 18 are not eligible for marriage.")
            else:
                return age
        except ValueError:
            print("Invalid age. Please enter a valid number.")

def get_marital_status():
    while True:
        print("Enter your marital status:")
        print("1. Married")
        print("2. Unmarried")
        print("3. Widow/Widower")
        choice = input("Enter your choice (1/2/3): ")
        match choice:
            case "1":
                return "married"
            case "2":
                return "unmarried"
            case "3":
                return "widow"
            case _:
                print("Invalid choice. Please enter 1 for married, 2 for unmarried, or 3 for widow/widower.")

def main():
    gender = get_gender()
    age = get_age(gender)
    marital_status = get_marital_status()

    print(f"Your gender is: {gender}")
    print(f"Your age is: {age}")
    print(f"Your marital status is: {marital_status}")

    if gender == "male" and marital_status == "married":
        print("Males who are already married cannot remarry.")
    elif gender == "female" and marital_status == "widow":
        print("Females who are widows can remarry.")
    else:
        print("You are eligible for marriage.")

if __name__ == "__main__":
    main()
