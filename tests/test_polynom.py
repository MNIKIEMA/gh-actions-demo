from src.polynom import Polynomial
import unittest


class TestPolynomial(unittest.TestCase):

    def setUp(self):
        # Create some polynomial instances for testing
        self.poly1 = Polynomial(1, -4, 3)  # Represents 1X^2 - 4X + 3
        self.poly2 = Polynomial(5, 0, -2, 3)  # Represents 5X^3 - 2X + 3
        self.poly3 = Polynomial(1, -4, 3)  # Same as poly1

    def test_repr(self):
        # Test string representation
        self.assertEqual(str(self.poly1), "X^2 -4X +3")
        self.assertEqual(str(self.poly2), "5X^3 -2X +3")

    def test_call(self):
        # Test polynomial evaluation
        self.assertEqual(self.poly1(0), 3)  # P(0)
        self.assertEqual(self.poly1(1), 0)  # P(1)
        self.assertEqual(self.poly2(1), 6)  # P(1)

    def test_eq(self):
        # Test equality comparison
        self.assertEqual(self.poly1, self.poly3)
        self.assertNotEqual(self.poly1, self.poly2)

    def test_initialization(self):
        # Test initialization
        self.assertEqual(self.poly1.coefs, [1, -4, 3])
        self.assertEqual(self.poly2.coefs, [5, 0, -2, 3])
        self.assertEqual(self.poly1.degre, 2)
        self.assertEqual(self.poly2.degre, 3)


if __name__ == '__main__':
    unittest.main()
