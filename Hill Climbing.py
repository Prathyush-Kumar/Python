import random

def objective_function(x):
    return -(x - 3) ** 2 + 9  # Example function with max at x=3

def hill_climb(start, step_size, max_iterations):
    current = start
    current_value = objective_function(current)
    
    for _ in range(max_iterations):
        neighbor = current + random.choice([-step_size, step_size])
        neighbor_value = objective_function(neighbor)
        
        if neighbor_value > current_value: 
            current, current_value = neighbor, neighbor_value
        else:
            break  # Stop if no improvement
    
    return current, current_value

best_x, best_value = hill_climb(start=0, step_size=0.1, max_iterations=1000)
print(f"Best solution found: {best_x}")
print(f"Objective value at best solution: {best_value}")
