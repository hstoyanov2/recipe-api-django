"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(5, 6)
        res2 = calc.add(1, 2)

        self.assertEqual(res, 11)
        self.assertEqual(res2, 3)

    def test_subtract_numbers(self):
        """Test subtracting numbers."""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)
    