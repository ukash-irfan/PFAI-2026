import csv
from pathlib import Path
from student import Student


def load_students(file_path):
    """Load students from a CSV file and return a list of Student objects."""
    students = []
    with Path(file_path).open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            marks = [
                float(row["mark1"]),
                float(row["mark2"]),
                float(row["mark3"]),
            ]
            students.append(Student(row["sap_id"], row["name"], marks))
    return students


def save_student_report(student, file_path):
    """Write an individual student report to a text file."""
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    report_text = (
        f"SAP ID: {student.sap_id}\n"
        f"Name: {student.name}\n"
        f"Average: {student.calculate_average():.2f}\n"
        f"Grade: {student.calculate_grade()}\n"
    )

    with path.open("w", encoding="utf-8") as file:
        file.write(report_text)


def main():
    """Load students, print profiles, save reports, and calculate class average."""
    base_folder = Path(__file__).resolve().parent
    csv_path = base_folder / "data" / "students.csv"

    students = load_students(csv_path)

    total_marks = 0.0

    print("Student Profiles:\n")
    for student in students:
        # Profile display karna
        print(student.format_profile())
        print("-" * 25)

        total_marks += student.calculate_average()

        report_path = base_folder / "reports" / f"{student.sap_id}.txt"
        save_student_report(student, report_path)

    class_average = total_marks / len(students)
    print(f"\nClass Average: {class_average:.2f}")

    sample_report = base_folder / "reports" / f"{students[0].sap_id}.txt"
    print("\nReading generated report for verification:")
    print(sample_report.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
