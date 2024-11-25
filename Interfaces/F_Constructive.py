from abc import ABC, abstractmethod
from Interfaces.F_Instance import Instance
from Interfaces.F_Solution_Binary import Solution_Binary

class Constructive(ABC):

	@abstractmethod
	def execute(self, instance: Instance) -> Solution_Binary:
		pass
