import sys
import os
import matplotlib.pyplot as plt
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from F_P1_Algorithm_1 import P1_Algorithm_1
from F_P1_Instance import P1_Instance
from F_P1_Objetive_Function import P1_Objetive_Function

INSTACE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + "\\Instances\\instancia_10_n150_m15.txt"

class P1_Stadistics:
	def __init__(self):
		self.instance = P1_Instance(INSTACE_PATH)
		self.of = P1_Objetive_Function()
		self.x = np.arange(0, 1.1, 0.1)
		self.y = []
		self.run()

	def run(self, time = 1):
		algorithm = P1_Algorithm_1()
		self.y = []
		for alpha in self.x:
			self.y.append(algorithm.run(self.instance, self.of, time, float(alpha)).get_of_value())
		self.y = np.array(self.y)

	def show(self):
		_, ax = plt.subplots()

		max_value = np.max(self.y)

		bars = ax.bar(self.x, self.y, width=0.05, color=['red' if value == max_value else 'blue' for value in self.y])

		for bar in bars:
			yval = bar.get_height()
			ax.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2),
					ha='center', va='bottom', fontsize=10)

		ax.set_xticks(self.x)

		ax.set_title('Objective Function vs Alpha')
		ax.set_xlabel('Alpha')
		ax.set_ylabel('Objective Function Value')

		plt.show()
