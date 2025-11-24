import matplotlib.pyplot as plt
import os
import datetime
import random

# Simple variables
name = ""
subjects = []
grades = []
hours = []

def set_student_name():
    global name
    name = input("Enter your name: ")
    print("Hello " + name)

def add_new_subject():
    subject = input("Enter subject name: ")
    subjects.append(subject)
    grades.append([])
    hours.append(0)
    print("Added " + subject)

def add_grade():
    subject = input("Enter subject name: ")
    if subject in subjects:
        grade = int(input("Enter grade: "))
        i = subjects.index(subject)
        grades[i].append(grade)
        print("Grade added")
    else:
        print("Subject not found")

def add_study_hours():
    subject = input("Enter subject name: ")
    hour = float(input("Enter hours: "))
    
    if subject == subjects[0]:
        hours[0] = hours[0] + hour
        print("Added hours")
    elif len(subjects) > 1 and subject == subjects[1]:
        hours[1] = hours[1] + hour
        print("Added hours")
    elif len(subjects) > 2 and subject == subjects[2]:
        hours[2] = hours[2] + hour
        print("Added hours")
    elif len(subjects) > 3 and subject == subjects[3]:
        hours[3] = hours[3] + hour
        print("Added hours")
    else:
        print("Subject not found")

def show_grade_chart():
    subject = input("Enter subject name: ")
    
    my_grades = []
    
    if len(subjects) > 0:
        if subject == subjects[0]:
            my_grades = grades[0]
    
    if len(subjects) > 1:
        if subject == subjects[1]:
            my_grades = grades[1]
    
    if len(subjects) > 2:
        if subject == subjects[2]:
            my_grades = grades[2]
    
    if len(my_grades) == 0:
        print("Subject not found")
    elif len(my_grades) == 1:
        print("Need more grades")
    else:
        plt.plot(my_grades)
        plt.show()

def show_hours_chart():
    if len(subjects) == 0:
        print("No subjects added")
    else:
        color = random.choice(["red", "blue", "green"])
        plt.bar(subjects, hours, color=color)
        plt.show()



print("Grade Tracker")
print("Adil Sukumar")

stop = False
while stop != True:
    print("\nMenu")
    print("1 - Set Name")
    print("2 - Enter Subject")
    print("3 - Grade")
    print("4 - Hours")
    print("5 - Grade Chart")
    print("6 - Hours Chart")
    print("7 - Exit")
    
    option = input("Please choose a number: ")
    
    if option == "1":
        set_student_name()
    elif option == "2":
        add_new_subject()
    elif option == "3":
        add_grade()
    elif option == "4":
        add_study_hours()
    elif option == "5":
        show_grade_chart()
    elif option == "6":
        show_hours_chart()
    elif option == "7":
        print("Thank you for using the grade tracker")
        stop = True
    else:
        print("Wrong input, please enter again!")