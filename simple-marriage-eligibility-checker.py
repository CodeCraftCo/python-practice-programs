def main():
    print("Enter details for Male:")
    male_gender = "male"
    male_age = int(input("Enter age: "))
    male_marital_status = input("Enter marital status (married/unmarried/widow): ")

    print("\nEnter details for Female:")
    female_gender = "female"
    female_age = int(input("Enter age: "))
    female_marital_status = input("Enter marital status (married/unmarried/widow): ")

    if male_gender == "male":
        if male_age < 21 or (male_marital_status == "married" and male_marital_status != "widow"):
            print("\nMale: Not Eligible")
        else:
            print("\nMale: Eligible")
    elif male_gender == "female":
        print("Invalid gender for Male")

    if female_gender == "female":
        if female_age < 18 or (female_marital_status == "married" and female_marital_status != "widow"):
            print("\nFemale: Not Eligible")
        else:
            print("\nFemale: Eligible")
    elif female_gender == "male":
        print("Invalid gender for Female")

if __name__ == "__main__":
    main()

