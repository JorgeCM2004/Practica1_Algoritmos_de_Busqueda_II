import sys
import os
from time import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from F_P1_Tests import P1_Tests

def test_algorithm1():
	tester = P1_Tests()
	init_time = time()
	tester.run_test("Algorithm_1")
	final_time = time()
	assert final_time - init_time <= 60 * max(tester.get_number_of_tests(), tester.get_number_of_instances())

def test_algorithm2():
	tester = P1_Tests()
	init_time = time()
	tester.run_test("Algorithm_2")
	final_time = time()
	assert final_time - init_time <= 60 * max(tester.get_number_of_tests(), tester.get_number_of_instances())
