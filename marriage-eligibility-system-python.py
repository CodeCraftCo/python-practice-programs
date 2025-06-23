class Person:
    def __init__(self, name, gender, age, marital_status="unmarried"):
        self.name = name
        self.gender = gender
        self.age = age
        self.marital_status = marital_status

    def is_eligible_for_marriage(self):
        if self.gender == "male" and self.age < 21:
            return False
        elif self.gender == "female" and self.age < 18:
            return False
        elif self.marital_status == "married":
            return False
        else:
            return True

    def get_married(self, spouse):
        if self.is_eligible_for_marriage() and spouse.is_eligible_for_marriage():
            self.marital_status = "married"
            spouse.marital_status = "married"
            print(f"{self.name} and {spouse.name} got married!")
        else:
            print("One or both partners are not eligible for marriage.")

    def remarry(self, spouse):
        if self.gender == "female" and self.marital_status == "widow":
            self.get_married(spouse)
        elif self.marital_status == "unmarried":
            self.get_married(spouse)
        else:
            print("Remarriage is not allowed.")

# Test the code
person1 = Person("John", "male", 25)
person2 = Person("Jane", "female", 20)
person3 = Person("Bob", "male", 20)
person4 = Person("Alice", "female", 16)

person1.get_married(person2)  # John and Jane got married!
person3.get_married(person4)  # One or both partners are not eligible for marriage.
person2.remarry(person3)  # Remarriage is not allowed.
person2.marital_status = "widow"
person2.remarry(person3)  # Jane and Bob got married!
