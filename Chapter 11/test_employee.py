import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.e = Employee("Suresh", "Yhap", 60000)

    def test_give_default_raise(self):
        salary1 = self.e.salary
        self.e.give_raise()
        salary2 = self.e.salary
        self.assertEqual(salary2 - salary1, 5000)

    def test_give_custom_raise(self):
        salary1 = self.e.salary
        custom_raise = 10000
        self.e.give_raise(custom_raise)
        salary2 = self.e.salary
        self.assertEqual(salary2 - salary1, custom_raise)



unittest.main()
        
