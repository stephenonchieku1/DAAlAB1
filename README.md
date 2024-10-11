

# Quicksort Performance Experiment

## Overview
This Python program demonstrates the performance of the **quicksort** algorithm by sorting random sets of numbers and measuring the time taken for the sorting process. It plots a graph of time taken versus the number of elements sorted to visualize the efficiency of the algorithm.

## Features
- **Quicksort Algorithm**: A fast and efficient sorting algorithm that works on the divide-and-conquer principle.
- **Random Number Generation**: Random integers are generated for each experiment instead of reading from a file.
- **Performance Measurement**: Measures and displays the time taken to sort arrays of different sizes.
- **Graph Plotting**: Plots a graph of the time taken against the number of elements to demonstrate how quicksort's performance scales.

## Requirements
- **Python 3.x**
- **matplotlib** for plotting the graph. Install it using:
  ```bash
  pip install matplotlib
  ```

## How to Run
1. Clone the repository or download the Python script.
2. Ensure Python is installed on your machine. You can check by running:
   ```bash
   python --version
   ```
3. Run the script:
   ```bash
   python quicksort_performance.py
   ```
4. The script will:
   - Generate random arrays of different sizes.
   - Sort the arrays using quicksort.
   - Measure the time taken for each sorting.
   - Plot the results in a graph.
   
## Code Explanation
The program contains the following key components:

1. **`quicksort(arr)`**: 
   - Implements the quicksort algorithm.
   
2. **`generate_random_elements(n)`**:
   - Generates a list of `n` random integers between `1` and `10000`.

3. **`measure_sorting_time(n)`**: 
   - Generates an array of size `n`, runs the quicksort function, and measures the time taken for sorting.

4. **`run_experiment(n_values)`**:
   - Runs the experiment for different values of `n` and collects the sorting times.
   
5. **`plot_results(n_values, times)`**:
   - Plots the graph of the time taken versus the number of elements sorted using `matplotlib`.

## Expected Output
The program will output the time taken for each array size and plot a graph like the following:

```
n=100, time taken=0.000123 seconds
n=500, time taken=0.000423 seconds
n=1000, time taken=0.001032 seconds
...
```

The graph will show the performance of the quicksort algorithm scaling with the number of elements, providing a visual representation of its time complexity.

## Example Graph
The graph plots the number of elements (`n`) on the x-axis and the time taken (in seconds) on the y-axis.

---

### License
This project is open-source. Feel free to use, modify, and distribute as needed.
