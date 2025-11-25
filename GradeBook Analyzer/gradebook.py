# ----------------------------------------------------------
# GradeBook Analyzer + CSV Creator Tool
# Name: Surya Rao
# Date: 25 Nov 2025
# ----------------------------------------------------------

import csv

# ==========================================================
# CSV CREATOR (EXTRA TOOL FOR USER)
# ==========================================================

def create_csv():
    file_name = input("Enter CSV file name to create (example: students.csv): ")
    n = int(input("Enter number of students: "))

    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        print("\nEnter student details:\n")

        for i in range(n):
            name = input(f"Enter name of student {i+1}: ")
            marks = input(f"Enter marks of {name}: ")
            writer.writerow([name, marks])

    print(f"\nCSV file '{file_name}' created successfully!\n")

# ==========================================================
# TASK 3: Statistical Functions
# ==========================================================

def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    scores = sorted(marks_dict.values())
    n = len(scores)
    mid = n // 2
    
    if n % 2 == 1:
        return scores[mid]
    else:
        return (scores[mid - 1] + scores[mid]) / 2

def find_max_score(marks_dict):
    return max(marks_dict.values())

def find_min_score(marks_dict):
    return min(marks_dict.values())

# ==========================================================
# TASK 4: Grade Assignment
# ==========================================================

def assign_grades(mmarks):
    grades = {}
    for name, score in mmarks.items():
        if score >= 90:
            grades[name] = "A"
        elif score >= 80:
            grades[name] = "B"
        elif score >= 70:
            grades[name] = "C"
        elif score >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"
    return grades

# ==========================================================
# TASK 2: Manual Input / CSV Input
# ==========================================================

def input_manual():
    marks = {}
    n = int(input("Enter number of students: "))
    
    for _ in range(n):
        name = input("Enter student name: ")
        score = int(input("Enter marks: "))
        marks[name] = score
    return marks

def load_csv():
    marks = {}
    file_name = input("Enter CSV file name (example: students.csv): ")
    
    try:
        with open(file_name, newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                name = row[0]
                score = int(row[1])
                marks[name] = score
        print("\nCSV loaded successfully!\n")
    except FileNotFoundError:
        print("File not found! Try again.")
        return load_csv()
    
    return marks

# ==========================================================
# TASK 6: Results Table
# ==========================================================

def print_table(marks, grades):
    print("\nName\t\tMarks\tGrade")
    print("-------------------------------------")
    for name in marks:
        print(f"{name}\t\t{marks[name]}\t{grades[name]}")
    print("-------------------------------------\n")

# ==========================================================
# MAIN PROGRAM LOOP
# ==========================================================

def main():
    print("===================================")
    print("       GradeBook Analyzer")
    print("===================================\n")

    while True:
        print("1. Manual Input of Marks")
        print("2. Load Marks from CSV File")
        print("3. Create a CSV File (Extra Tool)")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            marks = input_manual()
        elif choice == "2":
            marks = load_csv()
        elif choice == "3":
            create_csv()
            continue
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")
            continue

        # ---------------------------
        # TASK 3: Statistics
        # ---------------------------
        avg = calculate_average(marks)
        median = calculate_median(marks)
        max_score = find_max_score(marks)
        min_score = find_min_score(marks)

        print("\n----- Statistical Summary -----")
        print(f"Average Marks: {avg:.2f}")
        print(f"Median Marks: {median}")
        print(f"Highest Marks: {max_score}")
        print(f"Lowest Marks: {min_score}")

        # ---------------------------
        # TASK 4: Grade Assignment
        # ---------------------------
        grades = assign_grades(marks)

        grade_counts = {
            "A": list(grades.values()).count("A"),
            "B": list(grades.values()).count("B"),
            "C": list(grades.values()).count("C"),
            "D": list(grades.values()).count("D"),
            "F": list(grades.values()).count("F"),
        }

        print("\n----- Grade Distribution -----")
        for g, c in grade_counts.items():
            print(f"{g}: {c}")

        # ---------------------------
        # TASK 5: Pass / Fail
        # ---------------------------
        passed = [name for name, score in marks.items() if score >= 40]
        failed = [name for name, score in marks.items() if score < 40]

        print("\n----- Pass / Fail Summary -----")
        print("Passed Students:", passed)
        print("Failed Students:", failed)

        # ---------------------------
        # TASK 6: Display Table
        # ---------------------------
        print_table(marks, grades)

        repeat = input("Do you want to analyze again? (y/n): ")
        if repeat.lower() != "y":
            print("Thank you! Exiting...")
            break

# Run the program
main()
