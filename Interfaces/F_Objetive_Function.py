from abc import ABC, abstractmethod
from Interfaces.F_Solution_Binary import Solution_Binary
from Interfaces.F_Instance import Instance

class Objetive_Function(ABC):

	@abstractmethod
	def evaluate(self, solution: Solution_Binary, instance: Instance) -> float:
		pass

