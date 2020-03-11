

from modular import Count
from unittest import mock
import unittest

class testCount(unittest.TestCase):

    def test_add(self):

        count = Count()
        count.add = mock.Mock(return_value=7,side_effect=count.add)
        result = count.add(2,6)
        print(result)
        self.assertEqual(7,result)
        print('pass')

if __name__ == '__main__':
    unittest.main()