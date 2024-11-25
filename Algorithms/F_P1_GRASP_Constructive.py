from Interfaces.F_Constructive import Constructive
from Interfaces.F_Instance import Instance
from Interfaces.F_Objetive_Function import Objetive_Function
from Interfaces.F_Solution_Binary import Solution_Binary
from Utilities.F_P1_Queue import P1_Queue

from F_P1_Solution import P1_Solution

class P1_GRASP_Constructive(Constructive):
	def execute(self, instance: Instance, objetive_function: Objetive_Function, alpha: int) -> Solution_Binary:
		if alpha < 0 or alpha > 1:
			raise ValueError("El porcentaje de ciudades dado no es válido.")
		solution: Solution_Binary = P1_Solution(instance, objetive_function)
		value_list = instance.get_values_list().copy()
		n_items = int(instance.get_number_of_items() * alpha)
		best_queue = P1_Queue(n_items, value_list)
		m = instance.get_number_of_picks()
		l = []
		while m > 0:
			l.append(best_queue.choice())
			m -= 1
		solution.set_new_list(l)
		return solution
