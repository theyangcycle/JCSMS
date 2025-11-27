#Class student: each student is saved as an object, each student has a name and an id
class Student:
    def __init__(self,name,id):
        self.name = name
        self.id = id

#For lists of students(objects), prints the names of the students and then their ids on a separate line
def print_students(List):
    names = ' '.join(i.name for i in List)
    ids = ' '.join(str(i.id) for i in List)
    return f"{names}\n{ids}"

#Adds students to the main list
def add_student(student_name, students, student_id):
    student = Student(student_name,student_id)
    students.append(student)
    print('Student added successfully.')

#Removes a student from a list
def remove_student(student_info, students):
    boolean = False
    try:
        student_info = int(student_info)
        for i in students:
            if i.id == student_info:
                students.remove(i)
                boolean = True
        if boolean:
            print('Student removed successfully.')
        else:
            print('Student not found.')
    except ValueError:
        for i in students:
            if i.name == student_info:
                students.remove(i)
                boolean = True
        if boolean:
            print('Student removed successfully.')
        else:
            print('Student not found.')

#Adds a student to a specific club
def add_student_to_club(Info, Club, students):
    boolean = False
    try:
        Info = int(Info)
        for i in students:
            if i.id == Info:
                boolean = True
                if i in Club:
                    print('Student is already in this club.')
                    break
                else:
                    Club.append(i)
                    print('Student added successfully.')
                    break
        if not boolean:
            print('Student not found.')
    except ValueError:
        for i in students:
            if i.name == Info:
                boolean = True
                if i in Club:
                    print('Student is already in this club.')
                    break
                else:
                    Club.append(i)
                    print('Student added successfully.')
                    break
        if not boolean:
            print('Student not found.')

#Main code
if __name__ == '__main__':
    #Initializes all clubs
    Science_Olympiad = []
    CS_Team = []
    Math_Team = []
    TSA = []
    Cyberpatriots = []

    #Initializes main student list
    students = []
    #Initializes the student id count, every time a student is added the count goes up by one
    student_id = 1

    while True:
        #Main menu
        print('\n---JCSMS Menu---')
        print('1. List students')
        print('2. Add student')
        print('3. Remove student')
        print('4. List clubs')
        print('5. List students in a club')
        print('6. Add student to a club')
        print('7. Quit')
        
        #User choice
        choice = input('Choose an option: ')
        
        if choice == '1':
            #Calls the print students function on the main student list
            print(print_students(students))
        elif choice == '2':
            #Takes a student name calls the add student function on the student name and the current id
            student_name = input('Enter student name: ')
            add_student(student_name,students,student_id)
            #Increases id by 1
            student_id += 1
        elif choice == '3':
            #Takes the student name or id and calls the remove student function on the main student list
            student_info = input('Enter the student name or the student ID: ')
            remove_student(student_info,students)
        elif choice == '4':
            #Prints all the clubs
            print('Science Olympiad, CS Team, Math Team, TSA, Cyberpatriots')
        elif choice == '5':
            #Takes a club name and calls the print students function on that club
            club = input('Choose a club (Science Olympiad, CS Team, Math Team, TSA, Cyberpatriots): ')
            if club == 'Science Olympiad':
                print(print_students(Science_Olympiad))
            elif club == 'CS Team':
                print(print_students(CS_Team))
            elif club == 'Math Team':
                print(print_students(Math_Team))
            elif club == 'TSA':
                print(print_students(TSA))
            elif club == 'Cyberpatriots':
                print(print_students(Cyberpatriots))
            else:
                print('Club not found.')
        elif choice == '6':
            #Takes the name or id of a student and a club and calls the add student to club function on the info and club
            while True:
                student_club = input('Enter student name or ID: ')
                club = input('Choose a club (Science Olympiad, CS Team, Math Team, TSA, Cyberpatriots): ')
                if club == 'Science Olympiad':
                    add_student_to_club(student_club, Science_Olympiad, students)
                    break
                elif club == 'CS Team':
                    add_student_to_club(student_club, CS_Team, students)
                    break
                elif club == 'Math Team':
                    add_student_to_club(student_club, Math_Team, students)
                    break
                elif club == 'TSA':
                    add_student_to_club(student_club, TSA, students)
                    break
                elif club == 'Cyberpatriots':
                    add_student_to_club(student_club, Cyberpatriots, students)
                    break
                else:
                    print('Club not found.')
        elif choice == '7':
            #Breaks out of the main loop and ends the code
            break
        else:
            #Makes the user choose a valid choice if they do not
            print('Choose a valid choice.')