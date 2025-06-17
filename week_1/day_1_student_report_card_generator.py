def write_to_file(
    name: str, age: int, subjects: dict[str, int], grade: str, average: float
):
    with open("report.txt", "w") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
        for subject_name, subject_marks in subjects.items():
            file.write(f"{subject_name}: {subject_marks}\n")
        file.write(f"Average: {average:.2f}\n")
        file.write(f"Grade: {grade}\n")


def assign_grade(average: float) -> str:
    if average >= 80:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "F"


def add_bonus(subjects: dict[str, int]) -> dict[str, int]:
    response: str = (
        input("\nWould you like to add +5 bonus marks to all subjects?\nResponse: ")
        .strip()
        .lower()
    )
    if response in ["yes", "y", "true", "1"]:
        return {
            k: (100 if v + 5 > 100 else v + 5)  # cap at 100
            for k, v in subjects.items()
        }

    return subjects


def calculate_average(subjects: dict[str, int]) -> float:
    total: int = sum(subjects.values())
    return total / len(subjects)


def get_valid_age() -> int:
    while True:
        try:
            age = int(input("Please enter your age: "))
            if 3 <= age <= 120:
                return age
            print("Age must be between 4 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_valid_mark(subject: str) -> int:
    while True:
        try:
            mark = int(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Mark must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    name: str = input("Please enter your name: ").strip()
    while not name:
        name = input("Name cannot be empty. Please enter your name: ").strip()

    age: int = get_valid_age()

    subjects: dict[str, int] = {}

    for i in range(3):
        subject_name: str = input(f"\nEnter subject {i + 1} name: ").strip().title()
        while not subject_name:
            subject_name = (
                input("Subject name cannot be empty. Try again: ").strip().title()
            )
        subject_mark: int = get_valid_mark(subject_name)

        subjects[subject_name] = subject_mark

    subjects = add_bonus(subjects)
    average: float = calculate_average(subjects)
    grade: str = assign_grade(average)

    write_to_file(name, age, subjects, grade, average)

    print("\nStudent Report Card has been generated as 'report.txt'.\n")


main()
