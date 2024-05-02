from util.ga_methods import *
import time

if __name__ == '__main__':
    start_time: float = time.time()
    solution, num_evo = solve_melody()  # returns final solution and number of evolutions cycled to reach solution

    print(target_note, MAX_FITNESS_VALUE, "--> target")
    print(solution, solution.fitness(), "--> solution")
    print((time.time() - start_time) * 1000, "ms")  # time passed since the start of the program in milliseconds
    print(num_evo)
