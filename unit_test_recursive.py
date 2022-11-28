import unittest
import sys
import test_case
from floyd_recursive import floyd

NO_PATH=999

class testrecursive(unittest.TestCase):

	def test_floyd(self):
		NO_PATH=999
		MAX_LENGTH = len(graph[0])
		self.assertEqual(floyd(test_case.input_tr1),test_case.output_tr1,"Incorrect")