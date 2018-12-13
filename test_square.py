import unittest
import square

class testlist(unittest.TestCase):

    def test_generator(self):
        result=square.generator()
        self.assertEqual(result,[1, 4, 9, 16, 25])

if __name__=="__main__":
    unittest.main()