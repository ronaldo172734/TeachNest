# test_teachnest.py
"""
Tests for TeachNest module.
"""

import unittest
from teachnest import TeachNest

class TestTeachNest(unittest.TestCase):
    """Test cases for TeachNest class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TeachNest()
        self.assertIsInstance(instance, TeachNest)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TeachNest()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
