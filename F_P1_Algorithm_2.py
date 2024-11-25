from time import time

from Interfaces.F_Experiment import Experiment
from Interfaces.F_Instance import Instance
from Interfaces.F_Objetive_Function import Objetive_Function
from Interfaces.F_Solution_Binary import Solution_Binary
from Algorithms.F_P1_GRASP_Constructive import P1_GRASP_Constructive
from Algorithms.F_P1_Simulated_Annealing import P1_Simulated_Annealing

T0 = 10
TEMPERATURE_FUNCTION = lambda x: x * 0.9
N_REP = 10
C = lambda x: x < 1

class P1_Algorithm_2(Experiment):
	def run(self, instance: Instance, objetive_function: Objetive_Function, max_time: float, alpha: float) -> Solution_Binary:
		time0 = time()
		time1 = time0
		best_sol = None
		grasp = P1_GRASP_Constructive()
		improvement = P1_Simulated_Annealing()
		while time1 - time0 < max_time or best_sol is None:
			current_sol = grasp.execute(instance, objetive_function, alpha)
			last_value = current_sol.get_of_value()
			current_sol = improvement.improve(current_sol, T0, TEMPERATURE_FUNCTION, N_REP, C)
			current_sol.set_percentage_improved(last_value)
			if current_sol > best_sol:
				best_sol = current_sol
			time1 = time()
		return best_sol
