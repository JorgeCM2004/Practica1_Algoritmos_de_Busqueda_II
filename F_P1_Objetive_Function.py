from Interfaces.F_Objetive_Function import Objetive_Function
from Interfaces.F_Instance import Instance

class P1_Objetive_Function(Objetive_Function):
	def evaluate(self, l_sol: list[int], instance: Instance) -> float:
		size = len(l_sol)
		index0 = 0
		value = 0
		while index0 < size:
			index1 = index0 + 1
			while index1 < size:
				value += instance(l_sol[index0], l_sol[index1])
				index1 += 1
			index0 += 1
		return value
