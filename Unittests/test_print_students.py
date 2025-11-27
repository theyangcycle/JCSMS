import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from Main.main import Student,print_students

class TestPrint(unittest.TestCase):
    def test_print(self):
        students = []
        students.append(Student('Jonah',1))
        students.append(Student('Joel',2))
        students.append(Student('Jeremiah',3))
        x = print_students(students)
        self.assertIn('Jonah Joel Jeremiah',x)
        self.assertIn('1 2 3',x)

if __name__ == '__main__':
    unittest.main()