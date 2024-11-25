from abc import ABC, abstractmethod

class Instance(ABC):

	@abstractmethod
	def _read_instance(self) -> None:
		pass

	@abstractmethod
	def get_number_of_items(self) -> int:
		pass

	@abstractmethod
	def get_number_of_picks(self) -> int:
		pass

	def get_values_list(self) -> list[float]:
		pass
