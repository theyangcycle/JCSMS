import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from Main.main import Student,remove_student

class TestRemove(unittest.TestCase):
    def setUp(self):
        self.students = [Student('Jonah',1),Student('Joel',2),Student('Jeremiah',3)]
    
    def test_remove_by_id(self):
        remove_student(3,self.students)
        self.assertNotIn(Student('Jeremiah',3),self.students)
    
    def test_remove_by_name(self):
        remove_student('Jeremiah',self.students)
        self.assertNotIn(Student('Jeremiah',3),self.students)
    
    def test_student_id_not_found(self):
        students = self.students
        remove_student(4,self.students)
        self.assertEqual(self.students,students)
    
    def test_student_name_not_found(self):
        students = self.students
        remove_student('Jason',self.students)
        self.assertEqual(self.students,students)

if __name__ == '__main__':
    unittest.main()