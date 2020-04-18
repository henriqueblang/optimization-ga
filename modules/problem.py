import math

from modules.genetics.chromossome import Chromossome

def f(x, y):
    return abs(x * y * math.sin(math.pi * y / 4.0))

def f_chromossome(chromossome):
    x, y = Chromossome.get_fenotype(chromossome.get_genes())

    return f(x, y)

def g(x, y):
    return f(x, y) + 1

def g_chromossome(chromossome):
    x, y = Chromossome.get_fenotype(chromossome.get_genes())

    return g(x, y)

def f_average(population):
    avg = 0

    for chromossome in population:
        avg += f_chromossome(chromossome)

    avg /= len(population)

    return avg

def g_average(population):
    avg = 0

    for chromossome in population:
        avg += g_chromossome(chromossome)

    avg /= len(population)

    return avg