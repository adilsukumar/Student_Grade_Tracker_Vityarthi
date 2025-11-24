# Personalized Learning Analytics Dashboard for Students

## Project Overview

This is a Python-based desktop application that helps students track their academic progress and study habits. I built this as my college project to solve the problem of managing grades and study time across multiple subjects. Instead of using boring spreadsheets, this dashboard provides an interactive menu system with colorful charts and visual feedback.

The application allows students to record grades, log study sessions, and view their academic performance through beautiful bar charts and pie charts. All data is automatically saved to text files, so you never lose your progress.

## Features

### Core Functionality
- **Student Profile Management** - Set and store your name
- **Subject Management** - Add multiple subjects you're studying
- **Grade Tracking** - Record grades for assignments, tests, and projects
- **Study Session Logging** - Track how many hours you study each subject
- **Session Management** - Delete study sessions if you make mistakes

### Analytics & Visualization
- **Progress Reports** - View detailed statistics for each subject
- **Grade Charts** - Interactive bar charts showing grade averages
- **Study Time Charts** - Pie charts displaying study hour distribution
- **Automatic Calculations** - Average grades computed automatically

### Data Management
- **Auto-Save** - Data automatically saves when you exit
- **Manual Save** - Save your progress anytime
- **Data Backup** - Automatic backup files created in project folder
- **Data Persistence** - All information stored in simple text files

## Technologies/Tools Used

### Programming Language
- **Python 3.x** - Main programming language

### Required Libraries (4 total)
- **matplotlib** - For creating interactive charts and graphs
- **datetime** - For tracking dates of study sessions
- **os** - For file operations and checking file existence
- **random** - For randomizing chart colors

### Development Approach
- **Functional Programming** - Uses functions and global variables
- **Text-based UI** - Simple menu-driven interface
- **File I/O** - Custom text file format (no JSON dependency)
- **Error Handling** - Basic try/except blocks for user input

## Steps to Install & Run the Project

### Prerequisites
- Python 3.7 or higher installed on your computer
- Command line/terminal access

### Installation Steps

1. **Download the Project**
   ```bash
   # Clone or download the Vityarthi_Project folder to your computer
   cd Vityarthi_Project
   ```

2. **Install Required Dependencies**
   ```bash
   # Install matplotlib (only external dependency)
   pip install matplotlib
   
   # OR use the requirements file
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   # Start the main program
   python student_dashboard.py
   ```

### Alternative: Run Sample Data Demo
```bash
# Generate sample data and see charts
python sample_data.py
```

## Instructions for Testing

### Basic Testing Workflow

1. **Start the Application**
   ```bash
   python student_dashboard.py
   ```

2. **Test Core Features**
   - Choose option 1: Set your name (e.g., "John Doe")
   - Choose option 2: Add a subject (e.g., "Mathematics")
   - Choose option 3: Add grades (e.g., 85, 92, 78)
   - Choose option 4: Add study sessions (e.g., 2.5 hours)

3. **Test Analytics Features**
   - Choose option 6: View progress report
   - Choose option 7: Generate grade chart
   - Choose option 8: Generate study hours chart

4. **Test Data Management**
   - Choose option 9: Save data manually
   - Exit and restart program to test data loading

### Sample Test Data
```
Student Name: Alex Johnson
Subjects: Python Programming, Mathematics, Data Structures
Grades: 
  - Python Programming: 85, 90, 88
  - Mathematics: 92, 87, 95
  - Data Structures: 78, 82, 85
Study Sessions:
  - Python Programming: 3.5 hours
  - Mathematics: 2.5 hours
  - Data Structures: 4.0 hours
```

### Expected Results
- Progress report shows calculated averages
- Bar chart displays grade comparisons
- Pie chart shows study time distribution
- Data persists between program runs

### Error Testing
- Try entering invalid grades (letters instead of numbers)
- Try adding duplicate subjects
- Try deleting sessions when none exist
- Test with empty data

## File Structure
```
Vityarthi_Project/
├── student_dashboard.py    # Main application file
├── sample_data.py         # Sample data generator
├── requirements.txt       # Python dependencies
├── README.md             # This documentation
├── data.txt              # Your saved data (auto-created)
└── Vityarthi_Project/    # Backup folder
    └── data_backup.txt   # Automatic backup file
```

## Screenshots

### Main Menu Interface
<img width="807" height="522" alt="image" src="https://github.com/user-attachments/assets/2cfaeae2-bc78-4449-9633-3f640122472e" />


### Sample Progress Report
<img width="872" height="556" alt="image" src="https://github.com/user-attachments/assets/a385c054-b33d-4f8e-9757-adb22ff12112" />


### Chart Features
- **Bar Charts**: Colorful grade averages with percentage labels
- **Pie Charts**: Study time distribution with percentages
- **Interactive**: Charts open in separate windows
- **Professional**: Clean styling with student name in titles

## Troubleshooting

### Common Issues
- **"matplotlib not found"**: Run `pip install matplotlib`
- **Charts not displaying**: Make sure you have a GUI environment
- **Data not saving**: Check file permissions in project folder
- **Invalid input errors**: Enter numbers only for grades and hours

### Data File Format
```
NAME:Alex Johnson
SUBJECT:Math|GRADES:85,90,78|HOURS:5.5
SESSION:Math|2.5|2024-01-15
```

---
**Built by a college student learning Python**

**Project completed for Vityarthi**
