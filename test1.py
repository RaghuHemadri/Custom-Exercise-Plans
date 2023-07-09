import tensorflow as tf
import numpy as np
import pandas as pd
from bat_algorithm import BatAlgorithm

# Load the data
data = pd.read_csv('exercise_data.csv')

# Define the fitness function
def fitness_function(solution):
    # Convert solution to integer array
    solution = np.array(solution).astype(int)
    
    # Get the exercises corresponding to the solution
    exercises = data.iloc[solution]['Exercise'].values
    
    # Initialize variables
    repeats_over_25 = 0
    high_intensity_count = 0
    last_muscle_groups = []
    last_intensity = None
    score = 0
    
    # Loop over exercises
    for i in range(len(exercises)):
        exercise = exercises[i]
        muscle_group = data.iloc[solution[i]]['Muscle Group']
        intensity = data.iloc[solution[i]]['Intensity']
        repeats = data.iloc[solution[i]]['Repeats']
        
        # Constraint 1: At least four exercises must have the number of repeats over 25 times
        if repeats > 25:
            repeats_over_25 += 1
        if repeats_over_25 < 4:
            score -= 1
        
        # Constraint 2: Each training plan should have at least two exercises of high intensity
        if intensity == 'high':
            high_intensity_count += 1
        if high_intensity_count < 2:
            score -= 1
        
        # Constraint 3: Each muscle group repeating in dataframe more than once does not have the same exercise
        if muscle_group in last_muscle_groups:
            if exercise == last_exercise:
                score -= 1
        last_muscle_groups.append(muscle_group)
        
        # Constraint 4: If the last exercise in the fitness training plan was of higher intensity, 
        # the next exercise should be of medium or high intensity
        if last_intensity is not None:
            if last_intensity == 'high' and intensity == 'low':
                score -= 1
        last_intensity = intensity
        
        # Constraint 5: Number of repeats are less than 40 and greater than 1
        if repeats <= 1 or repeats >= 40:
            score -= 1
    
    return score

# Define the search space
search_space = []
for i in range(len(data)):
    search_space.append([i, i])

# Define the BatAlgorithm object
ba = BatAlgorithm(fitness_function, search_space, num_bats=10, num_iterations=100)

# Set up TensorFlow to use the GPU
physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

# Run the optimization
best_solution, best_fitness = ba.run()

# Print the best solution and fitness
print("Best solution:", best_solution)
print("Best fitness:", best_fitness)
