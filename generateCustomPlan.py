import numpy as np
import pandas as pd
from bat_algorithm import BatAlgorithm

# Read the CSV file into a DataFrame
df = pd.read_csv('sample_data.csv')

# Define the fitness function to be optimized
def fitness_function(solution):
    # Create a list of exercises
    exercises = []
    for i in range(len(solution)):
        exercises.append(df.iloc[i]['Exercise'])
    
    # Check constraints
    num_high_intensity = 0
    num_repeats_over_25 = 0
    muscle_groups = []
    last_intensity = None
    for i in range(len(exercises)):
        exercise = exercises[i]
        intensity = df.loc[df['Exercise'] == exercise, 'Intensity'].iloc[0]
        repeats = np.random.randint(2, 40)
        muscle_group = df.loc[df['Exercise'] == exercise, 'Muscle Group'].iloc[0]
        
        # Constraint 1: At least four exercises must have the number of repeats over 25 times
        if repeats > 25:
            num_repeats_over_25 += 1
        
        # Constraint 2: Each training plan should have at least two exercises of high intensity
        if intensity == 'High':
            num_high_intensity += 1
        
        # Constraint 3: Each muscle group repeating in dataframe more than once does not have the same exercise
        if muscle_group in muscle_groups:
            last_exercise = exercises[i-1]
            if df.loc[(df['Muscle Group'] == muscle_group) & (df['Exercise'] != last_exercise), 'Exercise'].iloc[0] == exercise:
                return 0.0
        else:
            muscle_groups.append(muscle_group)
        
        # Constraint 4: If the last exercise in the fitness training plan was of higher intensity, 
        # the next exercise should be of medium or high intensity
        if last_intensity is not None:
            if last_intensity == 'High' and intensity == 'Low':
                return 0.0
        
        # Constraint 5: Number of repeats are less than 40 and greater than 1
        if repeats <= 1 or repeats >= 40:
            return 0.0
        
        last_intensity = intensity
    
    # Calculate the fitness score
    fitness = 0.0
    if num_repeats_over_25 >= 4:
        fitness += 1.0
    if num_high_intensity >= 2:
        fitness += 1.0
    return fitness

# Set up Bat Algorithm
dimension = 8
lower_bound = -5.12
upper_bound = 5.12
population_size = 20
max_generations = 1000
ba = BatAlgorithm(fitness_function, dimension, lower_bound, upper_bound, population_size, max_generations)

# Run the optimization process
best_solution, best_fitness = ba.optimize()

# Print the results
print("Best solution:", best_solution)
print("Best fitness:", best_fitness)
