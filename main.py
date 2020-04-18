import matplotlib.pyplot as plt

import modules.problem as problem
from modules.genetics import operators
from modules.genetics import utils
from modules.genetics.chromossome import Chromossome

if __name__ == "__main__":
    population = []
    population.append(Chromossome(4, 3))
    population.append(Chromossome(2, 9))
    population.append(Chromossome(9, 11))
    population.append(Chromossome(0, 15))
    population.append(Chromossome(5, 5))
    population.append(Chromossome(14, 3))

    generation = 0
    population_score = problem.g_average(population)
    print(f"Generation # {generation} -> Average population score = {population_score:.3f}\n")

    generation_plot = []
    generation_plot.append(generation)

    population_score_plot = []
    population_score_plot.append(population_score)

    while generation < 50:
        parent1, parent2 = operators.selection(population)

        operators.crossover(population, parent1, parent2)
        operators.mutation(population)
        operators.elitism(population)

        generation += 1
        population_score = problem.g_average(population)

        generation_plot.append(generation)
        population_score_plot.append(population_score)

        print(f"Generation # {generation} -> Average population score = {population_score:.3f}\n")

    best_chromossome = utils.find_best_chromossome(population)
    print(f"Best individual: {utils.format_chromossome(best_chromossome)}")

    plt.plot(generation_plot, population_score_plot)
    plt.show()