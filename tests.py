import unittest
import calculator

class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        print("SETUP CALLED...")
        self.a, self.b = (10, 99)

    def tearDown(self):
        print("TEAR DOWN CALLED...")
        a=b=0

    def test_addition(self):
        print("TEST ADDITION")
        self.assertEqual(calculator.addition(self.a, self.b), 109)

if __name__ == '__main__':
    unittest.main()
