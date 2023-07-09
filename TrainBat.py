'''
In this example, we define the objective function as the sphere function and initialize a BatAlgorithm object with a population size of 100 and a number of iterations of 1000. We then call the optimize method of the BatAlgorithm object to run the optimization and obtain the best solution and its fitness value. Finally, we print the best solution and its fitness value.
'''
import tensorflow as tf
import numpy as np
from bat_algorithm import BatAlgorithm

# Define the objective function
def sphere(x):
    return tf.reduce_sum(x**2, axis=-1)

# Initialize the BatAlgorithm object with the objective function
ba = BatAlgorithm(objective_function=sphere, pop_size=100, num_iterations=1000)

# Run the optimization
best_solution, best_fitness = ba.optimize()

# Print the best solution and its fitness value
print("Best solution:", best_solution.numpy())
print("Best fitness:", best_fitness.numpy())

