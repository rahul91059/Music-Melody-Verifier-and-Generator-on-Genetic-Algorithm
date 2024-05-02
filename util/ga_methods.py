import musicalbeeps
from typing import List, Set, Tuple
import random as rd
from util.config import POPULATION_SIZE, NUMBER_OF_NOTES, MUTATION_RATE, REPRODUCTION_RATE, CROSSOVER_RATE, \
    MAX_NUMBER_OF_GENERATIONS, MAX_FITNESS_VALUE, target_note, target_dict, LIST_OF_POSSIBLE_NOTES

from entities.Individual import Individual
from util.plotting import plot_fitness_function


def generate_initial_population(count=POPULATION_SIZE) -> List[Individual]:
    population: Set[Individual] = set()

    # generate_initial_population
    while len(population) != count:
        notes: List[str] = [
            rd.choice(LIST_OF_POSSIBLE_NOTES)
            for _ in range(NUMBER_OF_NOTES)
        ]
        population.add(Individual(notes))

    return list(population)


# k-tournament selection
def selection(population: List[Individual]) -> List[Individual]:
    parents: List[Individual] = []

    rd.shuffle(population)

    # tournament selection between all individuals
    for i in range(len(population)):
        j = rd.randint(0, len(population) - 1)
        while i == j:
            j = rd.randint(0, len(population) - 1)
        if population[i].fitness() > population[j].fitness():
            parents.append(population[i])
        else:
            parents.append(population[j])

    # This returns a list of the two fittest individuals after performing tournament selection.
    return sorted(parents, key=lambda x: x.fitness(), reverse=True)[:2]


# random one-point crossover
def crossover(parents: List[Individual]) -> List[Individual]:
    crossover_point = rd.randint(1, NUMBER_OF_NOTES - 2)

    child1: List[str] = parents[0].notes[:crossover_point] + parents[1].notes[crossover_point:]
    child2: List[str] = parents[1].notes[:crossover_point:] + parents[0].notes[crossover_point:]

    return [Individual(child1), Individual(child2)]


# one-gene mutation
def mutate(individuals: List[Individual]) -> None:
    mutation_type = rd.choice(['swap', 'replace'])

    for individual in individuals:
        if mutation_type == 'swap':
            idx1, idx2 = rd.sample(range(len(individual.notes)), 2)
            individual.notes[idx1], individual.notes[idx2] = individual.notes[idx2], individual.notes[idx1]
        else:
            idx = rd.randint(0, len(individual.notes) - 1)
            individual.notes[idx] = rd.choice(LIST_OF_POSSIBLE_NOTES)


def next_generation(population: List[Individual]) -> List[Individual]:
    next_gen = []
    while len(next_gen) < len(population):
        children = []

        parents = selection(population)

        if rd.random() < REPRODUCTION_RATE:
            children = parents
        else:
            if rd.random() < CROSSOVER_RATE:
                children = crossover(parents)

            if rd.random() < MUTATION_RATE:
                mutate(children)

        next_gen.extend(children)

    return next_gen[:len(population)]


def print_generation(population: List[Individual]):
    for individual in population:
        print(individual.notes, individual.fitness(), individual.dict_notes, individual.number_of_shared_items())


def best_fitness(population: List[Individual]) -> Tuple[Individual, int]:
    max_idx, max_fitness = 0, 0
    for idx, i in enumerate(population):
        if i.fitness() > max_fitness:
            max_fitness = i.fitness()
            max_idx = idx

    return population[max_idx], max_fitness

def play_notes(notes: List[str]):
    player = musicalbeeps.Player(volume=0.15, mute_output=False)

    for note in notes:
        note_to_play = ''
        duration_note = ''
        flag = 0
        for c in note:
            if c != '-' and flag == 0:
                note_to_play += c
            elif c == '-':
                flag = 1
            else:
                duration_note += c

        player.play_note(note_to_play, float(duration_note))

def solve_melody() -> Tuple[Individual, int]:
    population: List[Individual] = generate_initial_population()
    curr_iteration_value = {}

    best_fitness_in_gen = 0
    best_individual_in_gen: Individual = population[0]
    number_of_evolutions = 0

    for _ in range(MAX_NUMBER_OF_GENERATIONS):
        best_individual_in_gen, best_fitness_in_gen = best_fitness(population)
        if number_of_evolutions % 200 == 0:
            curr_iteration_value[number_of_evolutions] = best_fitness_in_gen

            print(target_note, MAX_FITNESS_VALUE, target_dict, "----> target_note")
            print_generation(population)

            print("|\n|\n|>>>>\n")

            play_notes(best_individual_in_gen.notes)
            print("\n")

        if best_fitness_in_gen == MAX_FITNESS_VALUE:
            break
        else:
            population = next_generation(population)
            number_of_evolutions += 1

    print_generation(population)
    print("|\n|\n|>>>>\n")

    play_notes(best_individual_in_gen.notes)
    print("\n")

    curr_iteration_value[number_of_evolutions] = best_fitness_in_gen
    plot_fitness_function(MAX_FITNESS_VALUE, number_of_evolutions, curr_iteration_value)

    return best_individual_in_gen, number_of_evolutions

