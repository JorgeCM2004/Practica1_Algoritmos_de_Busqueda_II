import os

from Interfaces.F_Solution_Binary import Solution_Binary

ABS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

class P1_Saver():
	def save(self, solution_list: list[Solution_Binary], optional_header = None):
		csv_h = "Name;Value;Taken;Solution;%_Improved;CPU_Time\n"
		if optional_header is not None:
			HEADER = optional_header + "\n" + csv_h
		else:
			HEADER = csv_h
		lines = []
		best_lines = []
		for solution in solution_list:
			name = solution.get_instance().name
			value = str(solution.get_of_value())
			taken = str(solution.get_list())
			transformed_sol = str(solution.get_transformed_sol())
			percentage = solution.get_percentage_improved()
			CPU_time = str(solution.get_CPU_time()) + ' s'
			lines.append(";".join([name, value, taken, transformed_sol, percentage, CPU_time]))
		with open(ABS_PATH + "\\Saves\\Last_Save.csv", "w") as file:
			file.write(HEADER)
			for line in lines:
				file.write(line + '\n')
		try:
			with open(ABS_PATH + "\\Saves\\Best_Save.csv", "r") as best_file:
				best_file.readline()
				for best_line in best_file:
					best_lines.append(best_line)
			lines.sort()
			best_lines.sort()
			with open(ABS_PATH + "\\Saves\\Best_Save.csv", "w") as best_file:
				best_file.write(csv_h)
				i = 0
				while i < len(lines) and i < len(best_lines):
					container = lines[i].strip().split(';')
					best_container = best_lines[i].strip().split(';')
					if container[0] == best_container[0]:
						if float(container[1]) > float(best_container[1]):
							best_file.write(lines[i] + '\n')
						else:
							best_file.write(best_lines[i])
					else:
						if container[0] < best_container[0]:
							best_file.write(lines[i] + '\n')
							best_file.write(best_lines[i])
						else:
							best_file.write(best_lines[i])
							best_file.write(lines[i] + '\n')
					i += 1
				while i < len(lines):
					best_file.write(lines[i] + '\n')
					i += 1
				while i < len(best_lines):
					best_file.write(best_lines[i])
					i += 1
		except:
			with open(ABS_PATH + "\\Saves\\Best_Save.csv", "w") as best_file:
				best_file.write(csv_h)
				for line in lines:
					best_file.write(line + '\n')
