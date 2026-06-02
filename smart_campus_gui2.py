import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# MODULE 1
# Student Registration & Grade Evaluation
# -------------------------------

def student_registration():

    print("\n--- Student Registration ---")

    name = input("Enter Student Name: ")
    score = float(input("Enter Marks: "))

    if score >= 90:
        grade = "A"
        remark = "Excellent"

    elif score >= 75:
        grade = "B"
        remark = "Very Good"

    elif score >= 60:
        grade = "C"
        remark = "Good"

    elif score >= 40:
        grade = "D"
        remark = "Average"

    else:
        grade = "F"
        remark = "Needs Improvement"

    print("\n----- Student Report -----")
    print("Name :", name)
    print("Marks :", score)
    print("Grade :", grade)
    print("Remark :", remark)


# -------------------------------
# MODULE 2
# Course Enrollment
# -------------------------------

def course_enrollment():

    print("\n--- Course Enrollment ---")

    courses = []
    max_courses = 5

    while True:

        if len(courses) >= max_courses:
            print("Maximum course limit reached!")
            break

        course = input("Enter Course Name (done to stop): ")

        if course.lower() == "done":
            break

        credits = input("Enter Credits: ")

        if not credits.isdigit():
            print("Invalid Credits!")
            continue

        credits = int(credits)

        if credits <= 0:
            print("Credits must be positive!")
            continue

        courses.append((course, credits))

    print("\nEnrolled Courses")

    for course, credit in courses:
        print(course, "-", credit, "Credits")


# -------------------------------
# MODULE 3
# Student Records
# -------------------------------

def student_records():

    print("\n--- Student Records ---")

    students = []

    students.append({
        "name": "Priya",
        "age": 20,
        "grades": [85, 90, 78]
    })

    students.append({
        "name": "Rahul",
        "age": 21,
        "grades": [72, 88, 91]
    })

    students.append({
        "name": "Anita",
        "age": 19,
        "grades": [95, 89, 92]
    })

    for student in students:

        print("\nName :", student["name"])
        print("Age :", student["age"])
        print("Grades :", student["grades"])

    event_A = {"Priya", "Rahul", "Anita", "Kiran"}
    event_B = {"Rahul", "Anita", "Sneha"}

    print("\nCommon Participants :", event_A & event_B)
    print("All Participants :", event_A | event_B)


# -------------------------------
# MODULE 4
# Search & Sort Student IDs
# -------------------------------

def search_sort():

    print("\n--- Search & Sort Student IDs ---")

    student_ids = [105, 102, 110, 108, 101, 115]

    print("Original IDs :", student_ids)

    student_ids.sort()

    print("Sorted IDs :", student_ids)

    target = int(input("Enter Student ID to Search : "))

    if target in student_ids:
        print("Student ID Found")
    else:
        print("Student ID Not Found")


# -------------------------------
# MODULE 5
# Fee Calculator
# -------------------------------

def calculate_fee():

    print("\n--- Fee Calculator ---")

    tuition = float(input("Enter Tuition Fee : "))
    hostel = float(input("Enter Hostel Fee : "))
    transport = float(input("Enter Transport Fee : "))

    total = tuition + hostel + transport

    print("Total Fee =", total)


# -------------------------------
# MODULE 6
# File Handling
# -------------------------------

def file_management():

    print("\n--- File Handling ---")

    with open("student_records.txt", "w") as file:

        file.write("ID,Name,Marks\n")
        file.write("101,Arjun,85\n")
        file.write("102,Meera,92\n")
        file.write("103,Ravi,76\n")

    print("File Created Successfully")

    print("\nStored Records:")

    with open("student_records.txt", "r") as file:

        for line in file:
            print(line.strip())


# -------------------------------
# MODULE 7
# Directory Scanner
# -------------------------------

def directory_scanner():

    print("\n--- Directory Scanner ---")

    path = input("Enter Folder Path: ")

    try:

        if not os.path.exists(path):
            raise FileNotFoundError

        for root, dirs, files in os.walk(path):

            print("\n", root)

            for file in files:
                print("   ", file)

    except FileNotFoundError:

        print("Invalid Folder Path")

    except Exception as e:

        print("Error:", e)


# -------------------------------
# MODULE 8
# Performance Analytics
# -------------------------------

def performance_analysis():

    print("\n--- Performance Analytics ---")

    try:

        df = pd.read_csv("student_performance.csv")

        print("\nStudent Data")
        print(df)

        print("\nStatistical Summary")
        print(df.describe())

        scores = df[["Math", "Science", "English"]].to_numpy()

        print("\nMean Scores")
        print(np.mean(scores, axis=0))

        print("\nMedian Scores")
        print(np.median(scores, axis=0))

        subjects = ["Math", "Science", "English"]

        averages = [
            df["Math"].mean(),
            df["Science"].mean(),
            df["English"].mean()
        ]

        plt.bar(subjects, averages)

        plt.title("Average Subject Scores")

        plt.xlabel("Subjects")

        plt.ylabel("Average Marks")

        plt.show()

    except FileNotFoundError:

        print("student_performance.csv not found")

    except Exception as e:

        print("Error:", e)


# -------------------------------
# MAIN DASHBOARD
# -------------------------------

while True:

    print("\n")
    print("=" * 50)
    print(" SMART CAMPUS INFORMATION SYSTEM ")
    print("=" * 50)

    print("1. Student Registration")
    print("2. Course Enrollment")
    print("3. Student Records")
    print("4. Search & Sort Student IDs")
    print("5. Fee Calculator")
    print("6. Academic Records File")
    print("7. Directory Scanner")
    print("8. Performance Analytics")
    print("9. Exit")

    choice = input("\nEnter Choice : ")

    if choice == "1":
        student_registration()

    elif choice == "2":
        course_enrollment()

    elif choice == "3":
        student_records()

    elif choice == "4":
        search_sort()

    elif choice == "5":
        calculate_fee()

    elif choice == "6":
        file_management()

    elif choice == "7":
        directory_scanner()

    elif choice == "8":
        performance_analysis()

    elif choice == "9":

        print("\nThank You")
        break

    else:

        print("Invalid Choice")