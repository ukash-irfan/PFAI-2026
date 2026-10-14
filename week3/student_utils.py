def calculate_grade(marks):
    if marks >= 85:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def calculte_average(*marks):
    return sum(marks) / len(marks)


def format_student(**details):
    return f"{details['name']} studies {details['program']}"


def main():

    print("Grade for 84:", calculate_grade(84))
    print("Grade for 85:", calculate_grade(85))
    print("Grade for 49:", calculate_grade(49))
    print("Grade for 50:", calculate_grade(50))

    print("Average:", calculte_average(70, 80, 90))

    print(
        "Student:",
        format_student(name="Ali", program="AI"),
    )
