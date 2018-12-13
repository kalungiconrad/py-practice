import unittest
import net_amount

class netamount(unittest.TestCase):

    def test_calc(self):
        result = net_amount.calc()
        #in the prompt enter d100,w100,d50,d100,w50
        self.assertEqual(result,100)


if __name__=="__main__":
    unittest.main()