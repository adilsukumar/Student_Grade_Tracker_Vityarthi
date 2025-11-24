# Student Grade Tracker

**Author**: Adil Sukumar  
**Institution**: VIT Bhopal University  
**Course**: Introduction to Programming & Problem Solving  
**Academic Year**: 2025-2026

## Overview

Student Grade Tracker is a Python-based console application that helps students track their academic performance across multiple subjects. The system allows students to record grades, monitor study hours, and visualize their progress through interactive charts.

## Features

1. **Student Profile Management**
   - Set and store student name

2. **Subject Management**
   - Add multiple subjects dynamically
   - Track unlimited subjects

3. **Grade Tracking**
   - Record multiple grades per subject
   - Maintain complete grade history

4. **Study Hours Logging**
   - Log study hours for each subject
   - Cumulative hour tracking

5. **Data Visualization**
   - Grade trend charts (line graphs)
   - Study hours comparison (bar charts)
   - Color-coded visualizations

## System Requirements

- Python 3.x
- matplotlib library

## Installation

1. Install Python from [python.org](https://www.python.org/downloads/)

2. Install required library:
```bash
pip install matplotlib
```

3. Run the program:
```bash
python student_grade_tracker.py
```

## Usage Guide

### Menu Options

**1. Set Name**
- Enter your name to personalize the tracker

**2. Enter Subject**
- Add a new subject to track

**3. Grade**
- Record a grade for a specific subject
- Enter subject name and grade value

**4. Hours**
- Log study hours for a subject
- Enter subject name and hours studied

**5. Grade Chart**
- View grade progression for a subject
- Displays line graph of all grades
- Requires at least 2 grades

**6. Hours Chart**
- View study hours across all subjects
- Displays bar chart comparison
- Random color scheme for visual appeal

**7. Exit**
- Close the application

## Example Workflow

```
1. Set Name → Enter "Adil Sukumar"
2. Enter Subject → Add "Mathematics"
3. Enter Subject → Add "Physics"
4. Grade → Mathematics: 85
5. Grade → Mathematics: 90
6. Hours → Mathematics: 3.5 hours
7. Hours → Physics: 2.0 hours
8. Grade Chart → View Mathematics progress
9. Hours Chart → Compare study time
```

## Technical Implementation

### Data Structures
- **Lists**: Store subjects, grades (nested), and hours
- **Global Variables**: Maintain state across functions

### Key Functions
- `set_student_name()`: Initialize student profile
- `add_new_subject()`: Create new subject entry
- `add_grade()`: Record grade for subject
- `add_study_hours()`: Log study time
- `show_grade_chart()`: Visualize grade trends
- `show_hours_chart()`: Compare study hours

### Libraries Used
- **matplotlib.pyplot**: Data visualization
- **os**: System operations
- **datetime**: Date/time handling
- **random**: Color randomization

## Learning Outcomes

This project demonstrates:
- Variables and data types
- Lists and list operations
- Functions and modular programming
- Conditional statements (if-elif-else)
- Loops (while loop)
- User input/output
- External library integration
- Data visualization basics

## Limitations

- Data is not persistent (lost on exit)
- No data validation for negative grades
- Limited to console interface
- Manual subject name entry (case-sensitive)

## Future Enhancements

- Add data persistence (file storage)
- Implement grade statistics (average, GPA)
- Add data validation
- Create GUI interface
- Export reports to PDF
- Add assignment/exam categorization
- Include grade predictions

## License

This project is created for educational purposes as part of the Introduction to Programming & Problem Solving course at VIT Bhopal University.

---

