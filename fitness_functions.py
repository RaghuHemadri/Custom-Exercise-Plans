'''
The variable exercise is used in several methods of the ExercisePlan class to represent each exercise in the plan. It is a tuple that contains the following information:

*For weight loss, endurance, power, plyometric, and HIIT plans: (duration_in_minutes, intensity_level). Here, duration_in_minutes is the length of time the exercise is performed for, and intensity_level is a number between 0 and 1 that represents the level of intensity of the exercise.

*For muscle building plans: (weight_in_pounds, number_of_reps, number_of_sets). Here, weight_in_pounds is the weight of the resistance used for the exercise, number_of_reps is the number of repetitions performed in each set, and number_of_sets is the number of sets performed.

*For agility, flexibility, and balance plans: (duration_in_seconds, score). Here, duration_in_seconds is the length of time the exercise is performed for, and score is a number that represents the performance score of the exercise. The meaning of the score depends on the specific type of exercise - for example, for a balance exercise, the score might represent how long the person was able to balance for, while for a flexibility exercise, it might represent how far the person was able to stretch.

By using a tuple with these values, the ExercisePlan class can calculate the overall fitness score of the plan for a given goal, by combining the values of all the exercises in the plan according to the specific fitness function for that goal.

'''
class FitnessFunctions:
    
    def __init__(self, goal, plan):
        self.goal = goal
        self.plan = plan
    
    def fitness(self):
        if self.goal == 'weight_loss':
            return self.weight_loss_fitness()
        elif self.goal == 'endurance':
            return self.endurance_fitness()
        elif self.goal == 'muscle_building':
            return self.muscle_building_fitness()
        elif self.goal == 'agility':
            return self.agility_fitness()
        elif self.goal == 'flexibility':
            return self.flexibility_fitness()
        elif self.goal == 'balance':
            return self.balance_fitness()
        elif self.goal == 'power':
            return self.power_fitness()
        elif self.goal == 'plyometric':
            return self.plyometric_fitness()
        elif self.goal == 'hiit':
            return self.hiit_fitness()
        else:
            raise ValueError('Invalid goal.')
    
    def weight_loss_fitness(self):
        total_minutes = 0
        total_intensity = 0
        
        for exercise in self.plan:
            total_minutes += exercise[0]
            total_intensity += exercise[0] * exercise[1]
        
        avg_intensity = total_intensity / total_minutes
        
        return -total_minutes * avg_intensity
    
    def endurance_fitness(self):
        total_minutes = 0
        total_intensity = 0
        
        for exercise in self.plan:
            total_minutes += exercise[0]
            total_intensity += exercise[0] * exercise[1]
        
        avg_intensity = total_intensity / total_minutes
        
        return total_minutes * avg_intensity
    
    def muscle_building_fitness(self):
        total_weight = 0
        total_reps = 0
        
        for exercise in self.plan:
            total_weight += exercise[0] * exercise[1] * exercise[2]
            total_reps += exercise[1] * exercise[2]
        
        avg_weight = total_weight / total_reps
        
        return total_reps * avg_weight
    
    def agility_fitness(self):
        total_time = 0
        agility_score = 0
        
        for exercise in self.plan:
            total_time += exercise[0]
            agility_score += exercise[1] / exercise[0]
        
        avg_agility_score = agility_score / total_time
        
        return avg_agility_score
    
    def flexibility_fitness(self):
        total_time = 0
        flexibility_score = 0
        
        for exercise in self.plan:
            total_time += exercise[0]
            flexibility_score += exercise[1] / exercise[0]
        
        avg_flexibility_score = flexibility_score / total_time
        
        return avg_flexibility_score
    
    def balance_fitness(self):
        total_time = 0
        balance_score = 0
        
        for exercise in self.plan:
            total_time += exercise[0]
            balance_score += exercise[1] / exercise[0]
        
        avg_balance_score = balance_score / total_time
        
        return avg_balance_score
    
    def power_fitness(self):
        total_power = 0
        
        for exercise in self.plan:
            total_power += exercise[0] * exercise[1]
        
        return total_power
    
    def plyometric_fitness(self):
        total_power = 0
        
        for exercise in self.plan:
            total_power += exercise[0] * exercise[1]
        
        return total_power
    
    def hiit_fitness(self):
        total_time = 0
        total_intensity = 0

        for exercise in self.plan:
            total_time += exercise[0]
            total_intensity += exercise[1]

        avg_intensity = total_intensity / len(self.plan)

        return total_time * avg_intensity

class AdvancedFitnessFunctions(FitnessFunctions):
    '''
    During each iteration of the loop, the exercise variable represents a single exercise in the fitness plan, stored as a tuple with two values: the duration of the exercise (in minutes or kilometers, depending on the type of exercise), and the difficulty level of the exercise (on a scale of 1 to 10).
    '''
    def __init__(self, plan):
        super().__init__(plan)

    def yoga_fitness(self):
        total_time = 0
        total_difficulty = 0

        for exercise in self.plan:
            total_time += exercise[0]
            total_difficulty += exercise[1]

        avg_difficulty = total_difficulty / len(self.plan)

        return total_time * avg_difficulty

    def pilates_fitness(self):
        total_time = 0
        total_difficulty = 0

        for exercise in self.plan:
            total_time += exercise[0]
            total_difficulty += exercise[1]

        avg_difficulty = total_difficulty / len(self.plan)

        return (total_time ** 2) * avg_difficulty

    def cardiovascular_fitness(self):
        total_distance = 0
        total_time = 0

        for exercise in self.plan:
            total_distance += exercise[0]
            total_time += exercise[1]

        avg_speed = total_distance / total_time

        return avg_speed

    def cross_training_fitness(self):
        total_time = 0
        total_difficulty = 0

        for exercise in self.plan:
            total_time += exercise[0]
            total_difficulty += exercise[1]

        avg_difficulty = total_difficulty / len(self.plan)

        return total_time * (avg_difficulty ** 2)
