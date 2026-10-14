from student_toolkit import generate_summary, parse_marks, save_report


def main():
    name = input("Enter student name: ")
    marks_text = input("Enter marks separated by commas (e.g. 78, 65, 92): ")

    try:
        marks = parse_marks(marks_text)
        report = generate_summary(name, marks)

        print("\n" + report)

        save_report("student_report.txt", report)
        print("\nReport saved successfully as student_report.txt")

    except ValueError as error:
        print("Invalid marks:", error)


if __name__ == "__main__":
    main()