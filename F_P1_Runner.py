from typing import Literal
from time import time

from Interfaces.F_Solution_Binary import Solution_Binary

from F_P1_Search_Instances import P1_Search_Instances
from F_P1_Algorithm_1 import P1_Algorithm_1
from F_P1_Algorithm_2 import P1_Algorithm_2
from Utilities.F_P1_Saver import P1_Saver
from F_P1_Objetive_Function import P1_Objetive_Function

ALPHA = 0.5

class P1_Runner:
	def run(self, algorithm_name: Literal["Algorithm_1", "Algorithm_2"] = "Algorithm_1", seconds_per_instance: int = 60, save: bool = False):
		searcher = P1_Search_Instances()
		objetive_function = P1_Objetive_Function()
		total_time = len(searcher.instances_list) * seconds_per_instance * 0.95
		if algorithm_name == "Algorithm_1":
			algorithm = P1_Algorithm_1()
		elif algorithm_name == "Algorithm_2":
			algorithm = P1_Algorithm_2()
		else:
			raise ValueError("Algorithm debe ser uno de los dos valores definidos.")
		solutions = []
		for instance in searcher:
			time_instance = instance.get_number_of_items() * instance.get_number_of_picks() / searcher.total_unit * total_time
			time0 = time()
			solution: Solution_Binary = algorithm.run(instance, objetive_function, time_instance, ALPHA)
			time1 = time()
			solution.set_CPU_time(time1 - time0)
			solutions.append(solution)
		if save:
			saver = P1_Saver()
			saver.save(solutions, "Jorge_Camacho_Mejias - " + algorithm_name)

