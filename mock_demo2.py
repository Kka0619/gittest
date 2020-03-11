


from unittest.mock import patch
from function import add_and_mult
import unittest

class Mocktest2(unittest.TestCase):

    @patch('function.mult')
    def testMock2(self,mock_mult):
        a=3
        b=5
        mock_mult.return_value = 15
        x,y = add_and_mult(a,b)
        self.assertEqual(8,x)
        self.assertEqual(15,y)
        print((x,y))
        print(mock_mult.assert_called_once_with(3, 5))
if __name__ == '__main__':
    unittest.main()