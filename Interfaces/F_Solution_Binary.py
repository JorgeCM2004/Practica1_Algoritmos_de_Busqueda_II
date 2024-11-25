from abc import ABC, abstractmethod
from Interfaces.F_Instance import Instance

class Solution_Binary(ABC):

	@abstractmethod
	def get_number_of_items(self) -> int:
		pass

	@abstractmethod
	def get_number_of_picks(self) -> int:
		pass

	@abstractmethod
	def get_list(self) -> list[int]:
		pass

	@abstractmethod
	def set_new_list(self, new_list: list):
		pass

	def get_instance(self) -> Instance:
		pass

	def get_of_value(self) -> int:
		pass

	def get_transformed_sol(self) -> list[bool]:
		pass

	def get_CPU_time(self) -> float:
		pass

	def get_percentage_improved(self) -> str:
		pass

	def set_CPU_time(self, time):
		pass

	def set_percentage_improved(self, last_value):
		pass
