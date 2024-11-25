import random as rn

class P1_Queue():
	def __init__(self, max_size: int, l: list[float]) -> None:
		if max_size == 0:
			max_size = 1
		if max_size < 1:
			raise ValueError("El tamaño debe ser mayor a 0.")
		self.max_size = int(max_size)
		self.container = []
		self.l = l
		self.stop = False
		self._refill()

	def _refill(self):
		while len(self.container) < self.max_size and not self.stop:
			max_val = max(self.l)
			max_index = self.l.index(max_val)
			self.l[max_index] = 0
			if max_val != 0:
				self.container.append(max_index)
			else:
				self.stop = True

	def choice(self):
		self._refill()
		index = rn.randint(0, len(self.container) - 1)
		return self.container.pop(index)
