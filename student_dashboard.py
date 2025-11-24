# Import required modules
import matplotlib.pyplot as plt
from datetime import datetime
import os
import random

# Global variables to store data
student_name = ""
subjects = {}
sessions = []

def set_name():
    global student_name
    name = input("\n👤 Enter your name: ")
    student_name = name
    print("\n Welcome, " + name + "!")

def add_subject():
    subject = input("\n📚 Enter subject name: ")
    if subject not in subjects:
        subjects[subject] = {"grades": [], "hours": 0}
        print("\n Added: " + subject)
    else:
        print("\n  Subject already exists!")

def add_grade():
    subject = input("\n📚 Enter subject name: ")
    if subject in subjects:
        grade = float(input("📝 Enter grade (0-100): "))
        subjects[subject]["grades"].append(grade)
        print("\n Grade " + str(grade) + " added to " + subject)
    else:
        print("\n Subject not found!")

def add_session():
    subject = input("\n📚 Enter subject name: ")
    if subject in subjects:
        hours = float(input("⏰ Enter study hours: "))
        subjects[subject]["hours"] += hours
        today = datetime.now().strftime("%Y-%m-%d")
        session_data = {"subject": subject, "hours": hours, "date": today}
        sessions.append(session_data)
        print("\n Added " + str(hours) + " hours to " + subject)
    else:
        print("\n Subject not found!")

def delete_session():
    if len(sessions) == 0:
        print("\n No sessions found!")
        return
    
    print("\n📋 Study Sessions:")
    for i in range(len(sessions)):
        s = sessions[i]
        print("  " + str(i+1) + ". " + s['subject'] + " - " + str(s['hours']) + " hours (" + s['date'] + ")")
    
    try:
        choice = int(input("\n🗑️  Enter session number: ")) - 1
        if choice >= 0 and choice < len(sessions):
            s = sessions[choice]
            subjects[s["subject"]]["hours"] -= s["hours"]
            sessions.pop(choice)
            print("\n Deleted: " + s['subject'] + " - " + str(s['hours']) + " hours")
        else:
            print("\n Invalid number!")
    except:
        print("\n Invalid input!")

def show_report():
    print("\n" + "="*50)
    print("📊 PROGRESS REPORT FOR " + student_name.upper())
    print("="*50)
    
    if len(subjects) == 0:
        print("\n No subjects added yet!")
        return
        
    for subject in subjects:
        info = subjects[subject]
        # Calculate average grade
        if len(info["grades"]) > 0:
            total = 0
            for grade in info["grades"]:
                total += grade
            avg = total / len(info["grades"])
        else:
            avg = 0
        
        print("\n📚 " + subject + ":")
        print("   📈 Average Grade: " + str(round(avg, 1)) + "%")
        print("   ⏰ Study Hours: " + str(info['hours']))
        print("   📝 Total Grades: " + str(len(info['grades'])))
    print("\n" + "-"*50)

def show_grade_chart():
    subject_names = []
    averages = []
    
    for subject in subjects:
        subject_names.append(subject)
        grades = subjects[subject]["grades"]
        if len(grades) > 0:
            total = 0
            for grade in grades:
                total += grade
            avg = total / len(grades)
        else:
            avg = 0
        averages.append(avg)
    
    # Create bar chart
    plt.figure(figsize=(10, 6))
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
    random.shuffle(colors)
    plt.bar(subject_names, averages, color=colors[:len(subject_names)], alpha=0.8)
    plt.title("Grade Averages - " + student_name, fontsize=14, fontweight='bold')
    plt.ylabel("Average Grade (%)", fontsize=12)
    plt.xlabel("Subjects", fontsize=12)
    plt.ylim(0, 100)
    plt.grid(axis='y', alpha=0.3)
    
    # Add percentage labels on bars
    for i in range(len(averages)):
        v = averages[i]
        plt.text(i, v + 1, str(round(v, 1)) + '%', ha='center', fontweight='bold')
    
    plt.tight_layout()
    plt.show()

def show_hours_chart():
    subject_names = []
    hours_list = []
    
    for subject in subjects:
        subject_names.append(subject)
        hours_list.append(subjects[subject]["hours"])
    
    # Create pie chart
    plt.figure(figsize=(8, 8))
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
    plt.pie(hours_list, labels=subject_names, autopct='%1.1f%%', startangle=90,
            colors=colors[:len(subject_names)], explode=[0.05]*len(subject_names))
    plt.title("Study Hours Distribution - " + student_name, 
             fontsize=14, fontweight='bold')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

def save_data():
    # Create backup if data file exists
    if os.path.exists("data.txt"):
        if os.path.exists("data_backup.txt"):
            os.remove("data_backup.txt")
        os.rename("data.txt", "data_backup.txt")
    
    file = open("data.txt", 'w')
    file.write("NAME:" + student_name + "\n")
    
    for subject in subjects:
        info = subjects[subject]
        # Convert grades list to string
        grade_string = ""
        for i in range(len(info["grades"])):
            if i > 0:
                grade_string += ","
            grade_string += str(info["grades"][i])
        
        file.write("SUBJECT:" + subject + "|GRADES:" + grade_string + "|HOURS:" + str(info['hours']) + "\n")
    
    for session in sessions:
        file.write("SESSION:" + session['subject'] + "|" + str(session['hours']) + "|" + session['date'] + "\n")
    
    file.close()
    print("\n💾 Data saved!")

def load_data():
    global student_name
    try:
        if not os.path.exists("data.txt"):
            print("\n🆕 No saved data found.")
            return
            
        file = open("data.txt", 'r')
        lines = file.readlines()
        file.close()
        
        for line in lines:
            line = line.strip()
            if line.startswith("NAME:"):
                student_name = line[5:]
            elif line.startswith("SUBJECT:"):
                parts = line[8:].split("|")
                subject = parts[0]
                
                grade_part = parts[1].replace("GRADES:", "")
                hours_part = parts[2].replace("HOURS:", "")
                hours = float(hours_part)
                
                grades = []
                if grade_part != "":
                    grade_strings = grade_part.split(',')
                    for g in grade_strings:
                        if g != "":
                            grades.append(float(g))
                
                subjects[subject] = {"grades": grades, "hours": hours}
            elif line.startswith("SESSION:"):
                parts = line[8:].split("|")
                session_data = {"subject": parts[0], "hours": float(parts[1]), "date": parts[2]}
                sessions.append(session_data)
                
        print("\n Data loaded!")
    except:
        print("\n Error loading data.")

def main():
    print("\n" + "="*70)
    print("🎓 PERSONALIZED LEARNING ANALYTICS DASHBOARD FOR STUDENTS 🎓")
    print("="*70)
    
    load_data()
    
    while True:
        print("\n" + "-"*40)
        print("📋 MAIN MENU")
        print("-"*40)
        print("1. 👤 Set Name")
        print("2. 📚 Add Subject")
        print("3. 📝 Add Grade")
        print("4. ⏰ Add Study Session")
        print("5. 🗑️  Delete Session")
        print("6. 📊 Show Report")
        print("7. 📈 Grade Chart")
        print("8. 🥧 Hours Chart")
        print("9. 💾 Save Data")
        print("10. 🚪 Exit")
        print("-"*40)
        
        choice = input("\n🔢 Enter choice (1-10): ")
        
        if choice == '1':
            set_name()
        elif choice == '2':
            add_subject()
        elif choice == '3':
            add_grade()
        elif choice == '4':
            add_session()
        elif choice == '5':
            delete_session()
        elif choice == '6':
            show_report()
        elif choice == '7':
            show_grade_chart()
        elif choice == '8':
            show_hours_chart()
        elif choice == '9':
            save_data()
        elif choice == '10':
            save_data()
            print("\n" + "="*40)
            print("🎓 Thank you for using Student Dashboard - made by Adil Sukumar 🎓")
            print("📚 Keep learning and growing! 📚")
            print("="*40)
            break
        else:                                   
            print("\n Invalid choice! Please enter 1-10.")

if __name__ == "__main__":
    main()
