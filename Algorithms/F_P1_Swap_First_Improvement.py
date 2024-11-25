import random as rn

from Interfaces.F_Improvement import Improvement
from Interfaces.F_Instance import Instance
from Interfaces.F_Objetive_Function import Objetive_Function
from F_P1_Solution import P1_Solution

class P1_Swap_First_Improvement(Improvement):
	def improve(self, solution: P1_Solution) -> P1_Solution:
		new_list = solution.get_list().copy()
		new_sol = P1_Solution(solution.instance, solution.objetive_function)
		improved = True
		while improved:
			item_to_swap = rn.choice(new_list)
			possible_changes = list(set(range(solution.get_number_of_items())) - set(solution.get_list()))
			new_list.remove(item_to_swap)
			i = 0
			improved = False
			while not improved and i < len(possible_changes):
				index = possible_changes[i]
				new_list.append(index)
				new_sol.set_new_list(new_list)
				if new_sol > solution:
					solution.set_new_list(new_list.copy())
				new_list.remove(index)
				i += 1
		return solution
