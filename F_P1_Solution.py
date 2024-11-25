from Interfaces.F_Solution_Binary import Solution_Binary
from Interfaces.F_Instance import Instance
from Interfaces.F_Objetive_Function import Objetive_Function

class P1_Solution(Solution_Binary):
	def __init__(self, instance: Instance, objetive_function: Objetive_Function) -> None:
		self.instance = instance
		self.objetive_function = objetive_function
		self.value = None

	def __gt__(self, other: 'P1_Solution'):
		if self.value is None and other.value is None:
			raise ValueError("Ambas soluciones están vacias.")
		if self.value is None:
			return False
		if other is None or other.value is None:
			return True
		return self.value > other.value

	def get_number_of_items(self) -> int:
		return self.instance.get_number_of_items()

	def get_number_of_picks(self) -> int:
		return self.instance.get_number_of_picks()

	def get_instance(self) -> Instance:
		return self.instance

	def get_of_value(self) -> int:
		return self.value

	def get_list(self) -> list[int]:
		return self.list

	def get_transformed_sol(self) -> list[bool]:
		return self.transformed_solution

	def get_CPU_time(self) -> float:
		return self.CPU_time

	def get_percentage_improved(self) -> str:
		return self.percentage_improved

	def set_new_list(self, new_list: list[int]) -> None:
		self.list = new_list
		self.list.sort()
		self.value = self._calculate_value()
		self._transform_solution()

	def set_CPU_time(self, time):
		self.CPU_time = time

	def set_percentage_improved(self, last_value):
		val = (self.value * 100 / last_value) - 100
		self.percentage_improved = str(val) + '%'

	def _transform_solution(self):
		self.transformed_solution = [False for _ in range(self.get_number_of_items())]
		for index in self.list:
			self.transformed_solution[index] = True

	def _calculate_value(self) -> float:
		return self.objetive_function.evaluate(self.list, self.instance)
