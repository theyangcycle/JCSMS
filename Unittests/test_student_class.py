import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from Main.main import Student

class TestStudent(unittest.TestCase):
    def test_student_creation(self):
        student = Student("Jonah", 1)
        self.assertEqual(student.name, "Jonah")
        self.assertEqual(student.id, 1)

    def test_student_attributes(self):
        student = Student("Joel", 2)
        self.assertTrue(hasattr(student, 'name'))
        self.assertTrue(hasattr(student, 'id'))

if __name__ == '__main__':
    unittest.main()