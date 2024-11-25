from abc import ABC, abstractmethod
from Interfaces.F_Solution_Binary import Solution_Binary
from Interfaces.F_Objetive_Function import Objetive_Function

class Improvement(ABC):

	@abstractmethod
	def improve(self, solution: Solution_Binary, objetive_function: Objetive_Function) -> Solution_Binary:
		pass
