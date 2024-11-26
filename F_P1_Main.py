from time import time

from F_P1_Runner import P1_Runner

def main():
	runner = P1_Runner()
	runner.run(algorithm_name="Algorithm_2", seconds_per_instance=60, save=True)

if __name__ == "__main__":
	t1 = time()
	main()
	t2 = time()
	print(t2 - t1)
