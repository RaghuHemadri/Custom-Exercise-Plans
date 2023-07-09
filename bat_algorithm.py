import numpy as np

class BatAlgorithm:
    def __init__(self, objective_function, dimension, lower_bound, upper_bound, population_size=10, max_generations=100, A=1, r=0.5, Qmin=0, Qmax=2):
        self.objective_function = objective_function
        self.dimension = dimension
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.population_size = population_size
        self.max_generations = max_generations
        self.A = A
        self.r = r
        self.Qmin = Qmin
        self.Qmax = Qmax
        
        # Initialize population
        self.population = np.random.uniform(low=self.lower_bound, high=self.upper_bound, size=(self.population_size, self.dimension))
        self.velocity = np.zeros((self.population_size, self.dimension))
        self.frequency = np.zeros(self.population_size)
        self.pulse_rate = np.zeros(self.population_size)
        self.loudness = np.ones(self.population_size)
        self.best_solution = np.zeros(self.dimension)
        self.best_fitness = float('inf')
    
    def optimize(self):
        for i in range(self.max_generations):
            # Update frequency and pulse rate for each bat
            self.frequency = np.array([self.A*np.exp(-self.r*np.linalg.norm(self.population[j]-self.best_solution)) for j in range(self.population_size)])
            self.pulse_rate = np.array([np.exp(-self.r*np.linalg.norm(self.population[j]-self.best_solution)) for j in range(self.population_size)])
            
            # Update velocity and position for each bat
            self.velocity = self.velocity + (self.population - self.best_solution)*self.frequency[:, np.newaxis]
            self.population = self.population + self.velocity
            
            # Apply bounds to population
            self.population = np.clip(self.population, self.lower_bound, self.upper_bound)
            
            # Generate new solutions using local search
            for j in range(self.population_size):
                if np.random.random() > self.pulse_rate[j]:
                    new_solution = self.population[j] + np.random.normal(0, self.loudness[j], size=self.dimension)
                    new_solution = np.clip(new_solution, self.lower_bound, self.upper_bound)
                    new_fitness = self.objective_function(new_solution)
                    
                    # Update solution if better than current
                    if new_fitness < self.best_fitness:
                        self.best_solution = new_solution
                        self.best_fitness = new_fitness
                        
                        # Update loudness and rate
                        self.loudness[j] *= self.Qmax*(1-np.exp(-0.1*i))
                        self.pulse_rate[j] = self.Qmin + (self.Qmax-self.Qmin)*np.random.random()
            
            # print(f'Generation {i+1}: Best Fitness = {self.best_fitness}')
            length=100
            percent = int(i/self.max_generations * 100)
            bar_length = int(length * i/self.max_generations)
            bar = "#" * bar_length + "-" * (length - bar_length)
            print(f"[{bar}] {percent}% ({i}/{self.max_generations})", end="\r")
        
        return self.best_solution, self.best_fitness
