import random
import time
import matplotlib.pyplot as plt
# Quicksort Algorithm
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
# Function to generate random elements
def generate_random_elements(n, max_value=10000):
    return [random.randint(1, max_value) for _ in range(n)]
# Function to measure time taken by quicksort
def measure_sorting_time(n):
    arr = generate_random_elements(n)  # Generate random elements
    start_time = time.time()  # Start timing
    quicksort(arr)            # Sort the elements
    end_time = time.time()    # End timing
    return end_time - start_time  # Return time taken
# Main function to run the experiment
def run_experiment(n_values):
    times = []    
    for n in n_values:
        time_taken = measure_sorting_time(n)
        times.append(time_taken)
        print(f"n={n}, time taken={time_taken:.6f} seconds")
    return times
# Plotting the results
def plot_results(n_values, times):
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, times, marker='o', color='b')
    plt.title('Quicksort Performance (Time vs Number of Elements)')
    plt.xlabel('Number of Elements (n)')
    plt.ylabel('Time Taken (seconds)')
    plt.grid(True)
    plt.show()
# Driver code to execute the experiment
if __name__ == "__main__":
    # Define the values of n (array sizes) to test
    n_values = [1000,2000,3000,4000, 5000,6000, 7000,8000,9000,10000]    
    # Run the experiment
    times = run_experiment(n_values)
    # Plot the results
    plot_results(n_values, times)
