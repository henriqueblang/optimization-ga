import problem

def find_best_chromossome(population):
    best_chromossome = None

    for chromossome in population:
        score = problem.g_chromossome(chromossome)

        if best_chromossome is None or score > problem.g_chromossome(best_chromossome):
            best_chromossome = chromossome

    return best_chromossome

def find_worst_chromossome(population):
    worst_chromossome = None

    for chromossome in population:
        score = problem.g_chromossome(chromossome)

        if worst_chromossome is None or score < problem.g_chromossome(worst_chromossome):
            worst_chromossome = chromossome

    return worst_chromossome

def format_chromossome(chromossome):
    return f"{chromossome.to_string()}, Score = {problem.g_chromossome(chromossome):.3f}"