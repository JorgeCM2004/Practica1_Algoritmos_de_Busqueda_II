from abc import ABC, abstractmethod
from Interfaces.F_Instance import Instance
from Interfaces.F_Constructive import Constructive
from Interfaces.F_Objetive_Function import Objetive_Function
from Interfaces.F_Solution_Binary import Solution_Binary

class Experiment(ABC):

	@abstractmethod
	def run(self, instance: Instance, constructive: Constructive, objetive_function: Objetive_Function) -> Solution_Binary:
		pass
