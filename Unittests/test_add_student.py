import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from Main.main import Student, add_student

class TestAdd(unittest.TestCase):
    def setUp(self):
        self.students = []
        add_student('Jonah', self.students, 1)
        add_student('Joel', self.students, 2)
        add_student('Jeremiah', self.students, 3)
    
    def test_name(self):
        self.assertEqual(self.students[0].name, 'Jonah')
        self.assertEqual(self.students[1].name, 'Joel')
        self.assertEqual(self.students[2].name, 'Jeremiah')
    
    def test_id(self):
        self.assertEqual(self.students[0].id, 1)
        self.assertEqual(self.students[1].id, 2)
        self.assertEqual(self.students[2].id, 3)

if __name__ == '__main__':
    unittest.main()