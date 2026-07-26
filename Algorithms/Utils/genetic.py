import random
import math

# INITIALIZATION
population_size = 10
gene_length = 10  # Assuming each individual has 10 genes
population = [[random.uniform(0, 1) for _ in range(gene_length)] for _ in range(population_size)]

# EVALUATION
def fitness_function(x):
    return x * math.sin(10 * math.pi * x) + 1

def evaluate_population(population):
    return [fitness_function(individual) for individual in population]

# SELECTION
def select_parents(population, scores):
    parents = []
    total_fitness = sum(scores)
    selection_probs = [score / total_fitness for score in scores]
    while len(parents) < 2:
        r = random.random()
        cumulative_prob = 0
        for i, prob in enumerate(selection_probs):
            cumulative_prob += prob
            if r <= cumulative_prob:
                parents.append(population[i][:])  # Append a copy of the individual's genes
                break
    return parents

# CROSSOVER
def crossover(parents):
    gene_length = len(parents[0])
    
    point = random.randint(1, gene_length - 1)
    # Perform crossover
    child1 = parents[0][:point] + parents[1][point:]
    child2 = parents[1][:point] + parents[0][point:]
    
    return [child1, child2]

# MUTATION
def mutate(child, mutation_rate):
    mutated_child = []
    for gene in child:
        if random.random() < mutation_rate:
            mutated_child.append(random.uniform(0, 1))
        else:
            mutated_child.append(gene)
    return mutated_child

# GENETIC ALGORITHM
def genetic_algorithm(population, num_generations, mutation_rate):
    for generation in range(num_generations):
        scores = evaluate_population(population)

        parents = [select_parents(population, scores) for _ in range(population_size // 2)]

        children = [crossover(p) for p in parents]
        children = [item for sublist in children for item in sublist]

        mutated_children = [mutate(c, mutation_rate) for c in children]

        population = mutated_children

    best_solution = max(population, key=lambda x: fitness_function(x))
    return best_solution

best_individual = genetic_algorithm(population, num_generations=100, mutation_rate=0.1)
print("Best individual:", best_individual)
print("Fitness:", fitness_function(best_individual))
