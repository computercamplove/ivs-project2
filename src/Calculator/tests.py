##
# @mainpage IVS project documentation
# Doxygen documentation for IVS second project
#
# @file tests.py
# @brief File contains tests for matlib library

# Imports
import unittest
import matlib


##
# @defgroup tests Basic Tests
# @brief Tests for matlib library
# @{

class LibTests(unittest.TestCase):
    ##
    # @brief  Purpose of this test is to try various cases on add operation
    def test_basic_add(self):
        self.assertEqual(matlib.add(1, 2), 3)
        self.assertEqual(matlib.add(4, -12), -8)
        self.assertEqual(matlib.add(4, -5), -1)
        self.assertEqual(matlib.add(-2, 4), 2)
        self.assertEqual(matlib.add(0, 0), 0)

    ##
    # @brief Purpose of this test is to try various cases on sub operation
    def test_basic_sub(self):
        self.assertEqual(matlib.sub(4, 3), 1)
        self.assertEqual(matlib.sub(4, 1), 3)
        self.assertEqual(matlib.sub(0, 0), 0)
        self.assertEqual(matlib.sub(1, -3), 4)
        self.assertEqual(matlib.sub(12, -50), 62)

    ##
    # @brief Purpose of this test is to try various cases on mul operation
    def test_basic_mul(self):
        self.assertEqual(matlib.mul(2, 20), 40)
        self.assertEqual(matlib.mul(0, 2), 0)
        self.assertEqual(matlib.mul(4, -2), -8)

    ##
    # @brief Purpose of this test is to try various cases on div operation
    def test_basic_div(self):
        self.assertAlmostEqual(matlib.div(4, 2), 2)
        with self.assertRaises(ValueError):
            val = matlib.div(4, 0)
        self.assertAlmostEqual(matlib.div(0, 2), 0)
        self.assertAlmostEqual(matlib.div(4, -2), -2)
        self.assertAlmostEqual(matlib.div(-2, -1), 2)

    ##
    # @brief Purpose of this test is to try various cases on factorial operation
    def test_basic_factorial(self):
        self.assertAlmostEqual(matlib.factorial(3), 6)
        self.assertAlmostEqual(matlib.factorial(0), 1)
        with self.assertRaises(ValueError):
            val = matlib.factorial(-4)

    ##
    # @brief Purpose of this test is to try various cases on pow operation
    def test_basic_pow(self):
        self.assertEqual(matlib.pow(4, 2), 16)
        self.assertEqual(matlib.pow(4, 0), 1)

    ##
    # @brief Purpose of this test is to try various cases on n-root operation
    def test_basic_nroot(self):
        self.assertAlmostEqual(matlib.nroot(9), 3)
        with self.assertRaises(ValueError):
            val = matlib.nroot(matlib.nroot(-1))
        self.assertAlmostEqual(matlib.nroot(27, 3), 3)

    ##
    # @brief Purpose of this test is to try various cases on log operation
    def test_basic_log(self):
        self.assertAlmostEqual(matlib.log(100), 2)
        with self.assertRaises(ValueError):
            val = matlib.log(matlib.log(-1))
        self.assertAlmostEqual(matlib.log(27, 3), 3)


# @}

##
# @defgroup tests Advanced Tests
# @brief Advanced Tests for matlib library and for parsing functions
# @{
class AdvancedTests(unittest.TestCase):
    ##
    # @brief Purpose of this test is to test various functions which are used for parsing
    def test_support_functions_parsing(self):
        self.assertTrue(matlib.is_operator('+'))
        self.assertTrue(matlib.is_operator('-'))
        self.assertTrue(matlib.is_operator('/'))
        self.assertTrue(matlib.is_operator('*'))
        self.assertTrue(matlib.is_operator('^'))
        self.assertTrue(matlib.is_operator('!'))
        self.assertFalse(matlib.is_operator('e'))
        self.assertEqual(matlib.convert_str(15.323), "15.323")
        self.assertEqual(matlib.convert_str(0), "0")
        self.assertEqual(matlib.convert_str(0.000), "0")
        self.assertEqual(matlib.convert_str(757581.111114), "757581.111114")
        with self.assertRaises(TypeError):
            matlib.convert_str("12347")
        with self.assertRaises(TypeError):
            matlib.convert_str(None)
        with self.assertRaises(TypeError):
            list = []
            list.append(4)
            list.append(18.4242)
            matlib.convert_str(list)

    ##
    # @brief Purpose of this test is to try various cases on syntax checking
    def test_syntax(self):
        self.assertTrue(matlib.syntax("4+2"))
        self.assertTrue(matlib.syntax("((4+2)/12-3*(2^2-3.233454)*√2)-log(123.777)"))
        self.assertFalse(matlib.syntax("((4+2)/12-3*(2^2-3.233454)*√2"))
        self.assertFalse(matlib.syntax("((4+2)/12-3*(2)^2-3.233454)*√2)"))
        self.assertFalse(matlib.syntax("((4+2)/12-3*(2)^2-3.233454)*√2)"))
        self.assertFalse(matlib.syntax("log(2134.44"))
        self.assertFalse(matlib.syntax("4^^2"))
        self.assertFalse(matlib.syntax("4++2"))
        self.assertFalse(matlib.syntax("4//2"))

    ##
    # @brief Purpose of this test is to try various cases on unary conversion function
    def test_unary(self):
        self.assertEqual(''.join(matlib.convert_unary_func("(1^1/(5-1))-344.12+log(10)-4√74")),
                         "(1^1/(5-1))-344.12+l(10)-4r74")
        self.assertEqual(''.join(matlib.convert_unary_func("-74+122")), "0-74+122")
        self.assertEqual(''.join(matlib.convert_unary_func("-74-122")), "0-74-122")
        self.assertNotEqual(''.join(matlib.convert_unary_func("(1^1/(5-1))-344.12+log(10)-4√74")),
                            "(1^1/(5-1))-344.12+log(10)-4√74")

    ##
    # @brief Purpose of this test is to try various cases on postfix function
    def test_postfix(self):
        self.assertEqual(''.join(matlib.postfix("1^1/(5*1)+10")), "11^51*/10+")
        self.assertEqual(''.join(matlib.postfix("(1^1/(5-1))-344.12+log(10)-74")), "11^51-/344.12-10l+74-")
        self.assertEqual(''.join(matlib.postfix("( 1 ^ 1 / ( 5 - 1))-344.12+l(10)-74")), "11^51-/344.12-10l+74-")
        self.assertEqual(''.join(matlib.postfix("( 1 ^ 1 / ( 5 - 1))-344.12+l(10)-4r74")), "11^51-/344.12-10l+474r-")
        self.assertNotEqual(''.join(matlib.postfix("1^1/(5*1)+10")), "^1151*/+10")

    ##
    # @brief Purpose of this test is to try various cases on parsing and calculating expressions
    def test_basic_expression(self):
        self.assertEqual(matlib.parse_expression("(12+4)*8"), 128)
        self.assertAlmostEqual(matlib.parse_expression("(12-4)/2"), 4)
        self.assertAlmostEqual(matlib.parse_expression("4+2*3!-3"), 13)
        self.assertAlmostEqual(matlib.parse_expression("24-log(10)"), 23)
        self.assertAlmostEqual(matlib.parse_expression("-8+(-9*6^2/5.5)/5!*8-log(16)+6*√(4)"), -1.1313927099286)


if __name__ == '__main__':
    unittest.main()
