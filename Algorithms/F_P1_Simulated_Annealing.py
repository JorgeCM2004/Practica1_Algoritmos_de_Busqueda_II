import numpy as np

from Interfaces.F_Improvement import Improvement
from Interfaces.F_Solution_Binary import Solution_Binary
from F_P1_Solution import P1_Solution

class P1_Simulated_Annealing(Improvement):
	def improve(self, solution: Solution_Binary, t0, temperature_function, n_rep: int, C) -> Solution_Binary:
		best_sol = P1_Solution(solution.get_instance(), solution.objetive_function)
		best_sol.set_new_list(solution.get_list().copy())
		while not C(t0) and t0 > 0:
			for _ in range(n_rep):
				new_sol = self._get_random_neighbour(solution)
				delta = solution.get_of_value() - new_sol.get_of_value()
				if delta < 0:
					solution.set_new_list(new_sol.get_list().copy())
					best_sol.set_new_list(new_sol.get_list().copy())
				else:
					u = np.random.uniform(0, 1)
					if u < np.exp(-delta / t0):
						solution.set_new_list(new_sol.get_list().copy())
			t0 = temperature_function(t0)
		return best_sol


	def _get_random_neighbour(self, solution: Solution_Binary) -> Solution_Binary:
		new_list = solution.get_list().copy()
		item_to_swap = int(np.random.choice(new_list))
		possible_changes = list(set(range(solution.get_number_of_items())) - set(solution.get_list()))
		new_list.remove(item_to_swap)
		item_to_insert = int(np.random.choice(possible_changes))
		new_list.append(item_to_insert)
		new_sol = P1_Solution(solution.get_instance(), solution.objetive_function)
		new_sol.set_new_list(new_list)
		return new_sol
