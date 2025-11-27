import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from Main.main import Student,add_student_to_club

class TestAddClub(unittest.TestCase):
    def setUp(self):
        self.club = []
        self.students = [Student('Jonah',1),Student('Joel',2),Student('Jeremiah',3)]
    
    def test_add_by_id(self):
        add_student_to_club(1,self.club,self.students)
        self.assertEqual(self.club[0],self.students[0])
    
    def test_add_by_name(self):
        add_student_to_club('Jonah',self.club,self.students)
        self.assertEqual(self.club[0],self.students[0])
    
    def test_id_not_found(self):
        add_student_to_club(4,self.club,self.students)
        self.assertEqual(self.club,[])
    
    def test_name_not_found(self):
        add_student_to_club('Jason',self.club,self.students)
        self.assertEqual(self.club,[])


if __name__ == '__main__':
    unittest.main()