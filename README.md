## Description
Converging to the predetermined set of notes using genetic algorithm methods.
- Gene is a string. Each gene takes one of the values from a predefined list containing different notes. Each note is unique and differs by name, high or low pitch and duration of the note. One example of a gene is "A4#-0.5", which contains the name of the note(A), octave(4), raiser(#), delimiter(-) and the duration of the note(0.5).<br /><br />
- Chromosome represents one solution containing N notes. Each solution in each generation is scored according to the fitness function criteria. For each solution, we show the numerical value obtained by using the fitness function. Also, we map the list of notes to a dictionary whose key is the name of the note, and the value is the number of occurrences of a particular note. The fitness function uses the dictionary as one of the scoring criteria.<br /><br />
- Population is a set of solutions of size M<br /><br />
- The fitness function calculates the value of each solution based on two criteria. The first criterion is satisfied if the current and target solutions have the same note at the same index in the list. The second criterion is satisfied if the current solution has the same number of repetitions of a particular note in the list as the target solution. Dictionaries are used to check the second criterion. Satisfaction of the first criterion is scored 10 points, while satisfaction of the second criterion is scored 5 points. The program stops executing when the current and target solutions match according to all requirements and different forms of notes. When the value of the fitness function of a specific solution in the Nth evolution is equal to the value of the fitness function of the target solution, then we have reached the desired solution. The formula calculates the maximum value of the fitness function:
<p align="center">max_fitness_value = number of notes * 10 + number of different notes * 5</p><br />

## Genetic algorithm methods
- K-tournament selection: two winning parents with the highest fitness value are selected
- Recombination: random one-point crossover
- Mutation: swapping two existing notes or replacing a random note with the new one

## Fitness function
<img alt="Visualization of fitness function" height=70% src="/plots_img/fitness_function_03.png" width=70%/>