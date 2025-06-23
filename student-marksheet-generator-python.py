def calculate_percentage(marks):
    total_marks = sum(marks)
    percentage = (total_marks / 500) * 100
    return percentage

def display_marksheet(name, marks, percentage):
    print("\n------------------------ Marksheet ------------------------")
    print(f"Student Name: {name}")
    print("---------------------------------------------------------")
    print("Subject\t\tMarks")
    print("---------------------------------------------------------")
    print(f"English/t\t\t{marks[0]}")
    print(f"Maths/t\t\t{marks[1]}")
    print(f"Science/t\t\t{marks[2]}")
    print(f"Social Science/t\t{marks[3]}")
    print(f"Computer Science\t{marks[4]}")
    print("---------------------------------------------------------")
    print(f"Total Marks: {sum(marks)}/500")
    print(f"Percentage: {percentage}%")
    print("---------------------------------------------------------")

def main():
    name = input("Enter student name: ")
    marks = []
    for i in range(5):
        mark = int(input(f"Enter mark for subject {i+1}: "))
        marks.append(mark)
    percentage = calculate_percentage(marks)
    display_marksheet(name, marks, percentage)

if __name__ == "__main__":
    main()
