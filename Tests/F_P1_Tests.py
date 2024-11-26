from typing import Literal
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from F_P1_Runner import P1_Runner

TIME = 60

class P1_Tests:
	def __init__(self) -> None:
		self.expected_quality = []
		self._fill_quality()

	def get_number_of_tests(self):
		return len(self.expected_quality)

	def get_number_of_instances(self):
		return self.num_instances

	def run_test(self, algorithm: Literal["Algorithm_1", "Algorithm_2"]):
		runner = P1_Runner()
		runner.run(algorithm, TIME, save=True)
		solution_list: list = runner.solutions
		self.num_instances = len(solution_list)
		for instance_name_test, minimum_quality in self.expected_quality:
			i = 0
			instance_name_sol = solution_list[i].get_instance().name
			value = solution_list[i].get_of_value()
			while i < len(solution_list) and instance_name_sol != instance_name_test:
				i += 1
				instance_name_sol = solution_list[i].get_instance().name
				value = solution_list[i].get_of_value()
			if instance_name_sol == instance_name_test:
				assert minimum_quality <= value
			else:
				print("La instancia deseada no se encuentra en la carpeta de instancias.")
				assert instance_name_sol == instance_name_test


	def _fill_quality(self):
		self.expected_quality.append(("instancia_01_n10_m6.txt", 2106.73))
		self.expected_quality.append(("instancia_02_n10_m8.txt", 2720.61))
		self.expected_quality.append(("instancia_03_n15_m3.txt", 670.80))
		self.expected_quality.append(("instancia_04_n15_m9.txt", 5574.20))
		self.expected_quality.append(("instancia_05_n30_m6.txt", 1912.59))
		self.expected_quality.append(("instancia_06_n30_m24.txt", 34073.31))
		self.expected_quality.append(("instancia_07_n50_m15.txt", 10567.54))
		self.expected_quality.append(("instancia_08_n100_m10.txt", 5169.02))
		self.expected_quality.append(("instancia_09_n125_m37.txt", 106708.50))
		self.expected_quality.append(("instancia_10_n150_m15.txt", 21346.37))
