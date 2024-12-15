# Airline On-Time Performance Analysis Project

## Directory Structure
# - data/
#   - airline_performance.csv (Placeholder for raw data file)
# - src/
#   - main.py (Main project file for analysis and visualization)
# - visuals/
#   - (Generated plots will be saved here)
# - README.md

# Required Libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#file Paths
DATA_FILE = "C:\\Users\\LENOVO\\Desktop\\Aksh Python\\airline_performance.csv"
VISUALS_PATH = "visuals/"

#ensure the visuals directory exists
os.makedirs(VISUALS_PATH, exist_ok=True)

#1. Load Data
def load_data(filepath):
    """Load airline on-time performance data from a CSV file."""
    try:
        data = pd.read_csv(filepath)
        print("Data loaded successfully.")
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None

#2. Preprocess Data
def preprocess_data(data):
    """Clean and preprocess the data."""
    # Drop rows with missing values
    data = data.dropna()

    # Ensure data types are correct
    data['Month'] = data['Month'].astype(int)
    data['Day'] = data['Day'].astype(int)
    data['DepartureDelay'] = data['DepartureDelay'].astype(float)
    data['ArrivalDelay'] = data['ArrivalDelay'].astype(float)

    print("Data preprocessing complete.")
    return data

#3. Analysis
def analyze_data(data):
    """Perform basic analysis on the data."""
    avg_departure_delay = np.mean(data['DepartureDelay'])
    avg_arrival_delay = np.mean(data['ArrivalDelay'])

    most_delayed_airline = data.groupby('Airline')['DepartureDelay'].mean().idxmax()
    print(f"Average Departure Delay: {avg_departure_delay:.2f} minutes")
    print(f"Average Arrival Delay: {avg_arrival_delay:.2f} minutes")
    print(f"Airline with the most delays: {most_delayed_airline}")

    return avg_departure_delay, avg_arrival_delay, most_delayed_airline

# 4. Visualization
def visualize_performance(data):
    """Generate visualizations for airline performance."""
    # Bar plot for average delays by airline
    avg_delays = data.groupby('Airline')[['DepartureDelay', 'ArrivalDelay']].mean()
    avg_delays.plot(kind='bar', figsize=(10, 6))
    plt.title('Average Delays by Airline')
    plt.xlabel('Airline')
    plt.ylabel('Delay (minutes)')
    plt.grid(axis='y')
    plt.savefig(os.path.join(VISUALS_PATH, 'average_delays_by_airline.png'))
    plt.show()

    # Scatter plot: Departure delay vs Arrival delay
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='DepartureDelay', y='ArrivalDelay', hue='Airline', data=data)
    plt.title('Departure Delay vs Arrival Delay')
    plt.xlabel('Departure Delay (minutes)')
    plt.ylabel('Arrival Delay (minutes)')
    plt.grid()
    plt.savefig(os.path.join(VISUALS_PATH, 'departure_vs_arrival_delay.png'))
    plt.show()

# Main Execution
def main():
    # Load the data
    data = load_data(DATA_FILE)
    if data is None:
        return

    # Preprocess the data
    data = preprocess_data(data)

    # Analyze the data
    analyze_data(data)

    # Visualize performance
    visualize_performance(data)

if __name__ == "__main__":
    main()