# Importing the required libraries
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate Random Data
# Generate an array of 1000 random numbers from a normal distribution
data = np.random.randn(1000)

# Step 2: Perform Statistical Analysis
mean = np.mean(data)  # Mean of the data
median = np.median(data)  # Median of the data
std_dev = np.std(data)  # Standard deviation of the data

# Step 3: Display the Results
print("Statistical Analysis Results:")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev}")

# Step 4: Visualization
# Histogram of the data
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram of Random Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Step 5: Save the Data to a CSV file
np.savetxt("random_data.csv", data, delimiter=",")
print("\nData saved to 'random_data.csv'.")
