# PROJECT STATEMENT

## Student Grade Tracker System

---

### STUDENT INFORMATION

**Name**: Adil Sukumar  
**Registration Number**: 25MIB10056
**Institution**: VIT Bhopal University  
**Course Name**: Introduction to Programming & Problem Solving  
**Academic Year**: 2025-2026
**Semester**: 1

---

## 1. PROBLEM STATEMENT

### 1.1 Background

Students often struggle to keep track of their academic performance across multiple subjects throughout the semester. Traditional methods like notebooks or spreadsheets can be cumbersome and don't provide quick visual insights into progress. There is a need for a simple, interactive tool that allows students to record grades, monitor study hours, and visualize their academic performance in real-time.

### 1.2 Problem Definition

Develop a console-based Student Grade Tracker application using Python that enables students to:
- Manage multiple subjects
- Record and track grades for each subject
- Log study hours per subject
- Visualize grade trends and study time distribution
- Access all features through an intuitive menu-driven interface

---

## 2. OBJECTIVES

The primary objectives of this project are:

1. **Grade Management**: Create a system to record and store multiple grades for each subject
2. **Study Time Tracking**: Enable logging of study hours to correlate effort with performance
3. **Data Visualization**: Implement graphical representations of grades and study hours
4. **User-Friendly Interface**: Design an intuitive menu-driven console interface
5. **Demonstrate Python Fundamentals**: Apply core programming concepts learned in the course

---

## 3. SCOPE

### 3.1 In Scope

- Student name registration
- Dynamic subject addition
- Grade entry and storage for multiple subjects
- Study hours logging per subject
- Line chart visualization for grade progression
- Bar chart visualization for study hours comparison
- Menu-driven console interface
- Basic error handling for invalid inputs

### 3.2 Out of Scope

- Data persistence (database or file storage)
- Multi-user support
- Grade statistics and GPA calculation
- Assignment/exam categorization
- GUI interface
- Network/cloud features
- Authentication system

---

## 4. FUNCTIONAL REQUIREMENTS

### FR1: Student Profile Management
The system shall allow users to set and display their name.

### FR2: Subject Management
The system shall enable users to add new subjects dynamically during runtime.

### FR3: Grade Entry
The system shall allow users to enter multiple grades for each subject.

### FR4: Study Hours Logging
The system shall enable users to log study hours for each subject with cumulative tracking.

### FR5: Grade Visualization
The system shall display a line chart showing grade progression for a selected subject.

### FR6: Study Hours Visualization
The system shall display a bar chart comparing study hours across all subjects.

### FR7: Menu Navigation
The system shall provide a numbered menu with 7 options for easy navigation.

### FR8: Input Validation
The system shall validate subject existence before adding grades or hours.

### FR9: Chart Requirements
The system shall require at least 2 grades before displaying a grade chart.

### FR10: Exit Functionality
The system shall allow users to exit gracefully with a confirmation message.

---

## 5. NON-FUNCTIONAL REQUIREMENTS

### NFR1: Usability
The interface shall be simple enough for first-year students to use without training.

### NFR2: Performance
The system shall respond to user inputs within 1 second.

### NFR3: Reliability
The system shall handle invalid inputs without crashing.

### NFR4: Maintainability
The code shall be modular with clear function definitions.

### NFR5: Portability
The system shall run on Windows, macOS, and Linux with Python 3.x installed.

### NFR6: Visualization Quality
Charts shall be clear and readable with appropriate labels.

---

## 6. SYSTEM ARCHITECTURE

### 6.1 Architecture Overview

```
┌─────────────────────────────────────┐
│      User Interface Layer           │
│   (Console Menu & Input/Output)     │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│     Application Logic Layer         │
│  (Functions & Control Flow)         │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│       Data Storage Layer            │
│  (Lists & Global Variables)         │
└─────────────────────────────────────┘
               │
┌──────────────▼──────────────────────┐
│    Visualization Layer              │
│      (Matplotlib Charts)            │
└─────────────────────────────────────┘
```

### 6.2 Data Structure

- **name** (string): Stores student name
- **subjects** (list): Stores subject names
- **grades** (nested list): Stores grades for each subject
- **hours** (list): Stores cumulative study hours per subject

---

## 7. PROCESS FLOW

### 7.1 Main System Flow

```
START
  ↓
Display Welcome Message
  ↓
Enter Main Loop
  ↓
Display Menu (7 options)
  ↓
Get User Choice
  ↓
Execute Selected Function
  ↓
Return to Menu (unless Exit)
  ↓
END (when option 7 selected)
```

### 7.2 Add Grade Flow

```
User selects "Grade" option
  ↓
Input subject name
  ↓
Check if subject exists
  ↓
YES → Input grade value
  ↓
Find subject index
  ↓
Append grade to grades[index]
  ↓
Display confirmation
  ↓
Return to menu

NO → Display "Subject not found"
  ↓
Return to menu
```

---

## 8. IMPLEMENTATION DETAILS

### 8.1 Development Environment

- **Language**: Python 3.x
- **IDE**: Visual Studio Code
- **Libraries**: matplotlib, os, datetime, random
- **Platform**: Windows/macOS/Linux

### 8.2 Key Functions

1. **set_student_name()**: Captures and stores student name
2. **add_new_subject()**: Adds new subject to tracking system
3. **add_grade()**: Records grade for specified subject
4. **add_study_hours()**: Logs study hours for subject
5. **show_grade_chart()**: Displays line graph of grade progression
6. **show_hours_chart()**: Displays bar chart of study hours

### 8.3 Core Programming Concepts Used

- Variables (global and local)
- Data types (string, int, float, list)
- Lists and nested lists
- Functions and parameters
- Conditional statements (if-elif-else)
- Loops (while loop)
- User input/output operations
- External library integration
- List operations (append, index)

---

## 9. TESTING APPROACH

### 9.1 Test Cases

| Test ID | Test Case | Expected Result |
|---------|-----------|-----------------|
| TC01 | Set student name | Name stored and displayed |
| TC02 | Add new subject | Subject added to list |
| TC03 | Add grade to existing subject | Grade recorded successfully |
| TC04 | Add grade to non-existent subject | Error message displayed |
| TC05 | Add study hours | Hours added cumulatively |
| TC06 | View grade chart with <2 grades | Error message displayed |
| TC07 | View grade chart with ≥2 grades | Line chart displayed |
| TC08 | View hours chart with subjects | Bar chart displayed |
| TC09 | Invalid menu option | Error message, re-prompt |
| TC10 | Exit application | Graceful exit with message |

---

## 10. EXPECTED OUTCOMES

Upon successful completion, the project will:

1. Demonstrate proficiency in Python fundamentals
2. Provide a functional grade tracking tool for students
3. Showcase data visualization capabilities
4. Exhibit problem-solving and logical thinking skills
5. Serve as a foundation for future enhancements

---

## 11. TIMELINE

| Phase | Duration | Activities |
|-------|----------|------------|
| Planning | Week 1 | Requirement analysis, design |
| Development | Week 2-3 | Code implementation, testing |
| Documentation | Week 4 | README, report creation |
| Submission | Week 4 | Final review and submission |

---

## 12. CONCLUSION

The Student Grade Tracker project addresses a real-world need for academic performance monitoring while demonstrating fundamental programming concepts. The system provides practical utility through its visualization features and serves as an excellent learning exercise for understanding Python programming, data structures, and user interface design.

---

