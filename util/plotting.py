from typing import Dict

import matplotlib.pyplot as plt


def plot_fitness_function(max_fitness_value: int,
                          number_of_iterations: int,
                          curr_fitness_iteration_values: Dict[int, int]):
    x_data = list(curr_fitness_iteration_values.keys())
    y_data = list(curr_fitness_iteration_values.values())

    plt.ylim(0, max_fitness_value + 20)
    plt.axhline(y=max_fitness_value, linestyle='--', color='blue', label="max_fitness_value")
    plt.xlim(0, number_of_iterations + 20)

    plt.plot(x_data, y_data, 'ro')
    plt.plot(x_data, y_data, 'r-', label="curr_fitness_value")

    plt.xlabel('Number of generations')
    plt.ylabel('Fitness values')
    plt.legend(loc='lower right')
    plt.grid()
    plt.show()