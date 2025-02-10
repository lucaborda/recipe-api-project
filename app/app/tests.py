"""
Sample test
"""

from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):
    """Test the calc module."""

    def test_add_number(self):
        """Test adding number together."""
        res = calc.add(5, 6)

        self.assertEquals(res, 11)

    def test_subtract_number(self):
        """Test subtract number."""
        res = calc.subtract(10, 15)

        self.assertEquals(res, 5)