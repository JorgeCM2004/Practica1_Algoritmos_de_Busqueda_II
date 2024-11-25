from Interfaces.F_Instance import Instance

class P1_Instance(Instance):
	def __init__(self, route: str):
		self.route = route
		self._read_instance()
		self._create_values()
		self._extract_name()

	def __call__(self, index0: int, index1: int) -> float:
		if type(index0) is not int:
			raise TypeError("El primer indice en la consulta debe ser entero.")
		if type(index1) is not int:
			raise TypeError("El segundo indice en la consulta debe ser entero.")
		if index0 >= self.n:
			raise ValueError("El primer indice es mayor al tamaño de la matriz.")
		if index1 >= self.n:
			raise ValueError("El segundo indice es mayor al tamaño de la matriz.")
		return self.cost_matrix[index0][index1]

	def get_values_list(self) -> list[float]:
		return self.values_list

	def get_number_of_items(self) -> int:
		return self.n

	def get_number_of_picks(self) -> int:
		return self.m

	def _read_instance(self):
		with open(self.route, "r") as file:
			self.n, self.m = map(int, file.readline().strip().split(" "))
			self.cost_matrix = [[0] * self.n for _ in range(self.n)]
			for line in file:
				index0, index1, cost = line.strip().split(' ')
				index0, index1 = (int(index0), int(index1))
				cost = float(cost)
				self.cost_matrix[index0][index1] = cost
				self.cost_matrix[index1][index0] = cost

	def _create_values(self):
		self.values_list: list[float] = []
		for index in range(self.n):
			self.values_list.append(sum(self.cost_matrix[index]))

	def _extract_name(self):
		index = self.route.rfind("/")
		if index == -1:
			index = self.route.rfind("\\")
		self.name = self.route[index + 1:]
