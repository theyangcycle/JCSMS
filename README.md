# JCSMS - James Clemens Student Management System

An application for managing students and their clubs.

## Features

- Add and remove students
- List all students with their IDs
- Manage multiple clubs (Science Olympiad, CS Team, Math Team, TSA, Cyberpatriots)
- Add students to clubs by name or ID
- List students in a specific club
- Unit testing

## Project Structure

```
JCSMS/
├── Main/
│   └── __pycache__/
│   │   └── main.cpython-313.pyc
│   └── main.py
├── Unittests/
│   └── test_add_student_to_club.py
│   └── test_add_student.py
│   └── test_print_students.py
│   └── test_remove_student.py
│   └── test_student_class.py
└── README.md
```

## Requirements

- Python 3.6 or higher (only uses Python standard library)

## Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd JCSMS
   ```

## Usage

### Running the Application

From the JCSMS directory, run:

```bash
python Main/main.py
```

### Main Menu Options

When you run the application, you'll see this menu:

```
---JCSMS Menu---
1. List students
2. Add student
3. Remove student
4. List clubs
5. List students in a club
6. Add student to a club
7. Quit
```

### Example Usage

#### Adding Students
```
Choose an option: 2
Enter student name: Jonah
Student added successfully.
```

#### Listing Students
```
Choose an option: 1
Jonah Joel Jeremiah
1 2 3
```

#### Adding Student to Club
```
Choose an option: 6
Enter student name or ID: Jonah
Choose a club (Science Olympiad, CS Team, Math Team, TSA, Cyberpatriots): CS Team
Student added successfully.
```

#### Viewing Club Roster
```
Choose an option: 5
Choose a club (Science Olympiad, CS Team, Math Team, TSA, Cyberpatriots): CS Team
Jonah
1
```

#### Removing Students
```
Choose an option: 3
Enter the student name or the student ID: 1
Student removed successfully.
```

## Running Tests

The project includes unit tests to ensure all source code works correctly.

### Run Test
```bash
python -m unittest Unittests.test_student_class
```
To run a different test simply replace test_student_class with the name of the file the test is in.

### Import Errors
If you get `ModuleNotFoundError`:
```python
# Make sure you're running from the JCSMS directory
cd JCSMS
python Main/main.py
```

### Tests Not Running
If tests can't find the main module:
```bash
# Run from JCSMS directory with -m flag
python -m unittest Unittests.test_student_class
```

## License

This project is created for educational purposes.

## Author

Jonah Yang

**Version:** 1.0  
**Last Updated:** November 2024
