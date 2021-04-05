import unittest
import matlib

class LibTests(unittest.TestCase):

    def test_basic_add(self):
        self.assertEqual(matlib.add(1, 2), 3)
        self.assertEqual(matlib.add(4,-12),-8)
        self.assertEqual(matlib.add(4,-5),-1)
        self.assertEqual(matlib.add(-2,4), 2)
        self.assertEqual(matlib.add(0,0), 0)

    def test_basic_sub(self):
        self.assertEqual(matlib.sub(4,3), 1)
        self.assertEqual(matlib.sub(4,1), 3)
        self.assertEqual(matlib.sub(0,0),0)
        self.assertEqual(matlib.sub(1,-3), 4)
        self.assertEqual(matlib.sub(12,-50),62)

    def test_basic_mul(self):
        self.assertEqual(matlib.mul(2,20),40)
        self.assertEqual(matlib.mul(0,2), 0)
        self.assertEqual(matlib.mul(4, -2), -8)

    def test_basic_div(self):
        self.assertAlmostEqual(matlib.div(4,2), 2)
        with self.assertRaises(ValueError):
            val = matlib.div(4, 0)
        self.assertAlmostEqual(matlib.div(0,2),0)
        self.assertAlmostEqual(matlib.div(4,-2), -2)
        self.assertAlmostEqual(matlib.div(-2, -1), 2)

    def test_basic_factorial(self):
        self.assertAlmostEqual(matlib.factorial(3), 6)
        self.assertAlmostEqual(matlib.factorial(0), 1)
        with self.assertRaises(ValueError):
            val = matlib.factorial(-4)

    def test_basic_pow(self):
        self.assertEqual(matlib.pow(4,2), 16)
        self.assertEqual(matlib.pow(4,0),1)

    def test_basic_nroot(self):
        self.assertAlmostEqual(matlib.nroot(9), 3)
        with self.assertRaises(ValueError):
            val = matlib.nroot(matlib.nroot(-1))
        self.assertAlmostEqual(matlib.nroot(27,3), 3)

    def test_basic_log(self):
        self.assertAlmostEqual(matlib.log(100), 2)
        with self.assertRaises(ValueError):
            val = matlib.log(matlib.log(-1))
        self.assertAlmostEqual(matlib.log(27,3), 3)

    def test_basic_expression(self):
        self.assertEqual(matlib.parse_expression("(12+4)*8"), 128)
        self.assertAlmostEqual(matlib.parse_expression("(12-4)/2"), 4)
        self.assertAlmostEqual(matlib.parse_expression("4+2*3!-3"),13)
        self.assertAlmostEqual(matlib.parse_expression("24-log(10)"),23)
        self.assertAlmostEqual(matlib.parse_expression("-8+(-9*6^2/5.5)/5!*8-log(16)+6*√4"),6.33527395674)




if __name__ == '__main__':
    unittest.main()
