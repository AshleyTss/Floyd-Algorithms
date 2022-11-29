import unittest
from floyd_recursive import floyd
import test_case

class FloydOutputTest(unittest.TestCase):

	def testfloyd1(self):

	    self.assertEqual(floyd(test_case.input_tr1),test_case.output_tr1,"Incorrect")

	def testfloyd2(self):

	    self.assertEqual(floyd(test_case.input_tr2),test_case.output_tr2,"Incorrect")

	def testfloyd3(self):

	    self.assertEqual(floyd(test_case.input_tr3),test_case.output_tr3,"Incorrect")

	def testfloyd4(self):

	    self.assertEqual(floyd(test_case.input_tr4),test_case.output_tr4,"Incorrect")
