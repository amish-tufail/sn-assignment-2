# Pseudo-code:
# 1. We need to read each CSV file from the "temperature_data" folder for each year.
#    - For each file, extract temperature data for each month (January to December).
#    - If a file is missing or cannot be read, handle the error and prompt to continue.
# 2. Calculate average temperatures for each season (Summer, Autumn, Winter, Spring):
#    - For each season, calculate the average temperature across all years.
# 3. Find the station with the largest temperature range:
#    - For each station, calculate the temperature range (difference between max and min temperature).
# 4. Find the warmest and coolest stations based on the highest and lowest temperatures.
# 5. Save the results in separate files:
#    - "average_temp.txt" for the average temperatures for each season.
#    - "largest_temp_range_station.txt" for the station with the largest temperature range.
#    - "warmest_and_coolest_station.txt" for the warmest and coolest stations.

# Function to handle input validation

import os
import csv

def get_valid_input(prompt, value_type, min_value=None, max_value=None):
    while True:
        try:
            user_input = value_type(input(prompt))
            if (min_value is not None and user_input < min_value) or (max_value is not None and user_input > max_value):
                print(f"Error: Please enter a value between {min_value} and {max_value}.")
                continue
            return user_input
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")
        
        retry = input("Would you like to try again? (y/n): ").lower()
        if retry == 'n':
            print("Exiting the program.")
            exit()

# Function to read and process temperature data from all CSV files
def read_temperature_data(folder_path):
    data = {}  # To store data by station name

    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            year = filename.split('_')[-1].split('.')[0]  # Extract year from the file name
            try:
                with open(os.path.join(folder_path, filename), newline='') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        station = row["STATION_NAME"]
                        if station not in data:
                            data[station] = {}
                        # Store the temperature data for each month
                        data[station][year] = {
                            "January": float(row["January"]),
                            "February": float(row["February"]),
                            "March": float(row["March"]),
                            "April": float(row["April"]),
                            "May": float(row["May"]),
                            "June": float(row["June"]),
                            "July": float(row["July"]),
                            "August": float(row["August"]),
                            "September": float(row["September"]),
                            "October": float(row["October"]),
                            "November": float(row["November"]),
                            "December": float(row["December"])
                        }
            except Exception as e:
                print(f"Error reading {filename}: {e}")
    return data

# Function to calculate average temperatures for each season
def calculate_average_temperatures(data):
    seasons = {
        "Summer": ["December", "January", "February"],
        "Autumn": ["March", "April", "May"],
        "Winter": ["June", "July", "August"],
        "Spring": ["September", "October", "November"]
    }

    season_averages = {season: [] for season in seasons}

    # Loop through each station
    for station, years_data in data.items():
        for year, monthly_data in years_data.items():
            for season, months in seasons.items():
                season_temp = sum(monthly_data[month] for month in months) / len(months)
                season_averages[season].append(season_temp)
    
    # Calculate the average temperature for each season across all years
    season_average_final = {season: sum(temps) / len(temps) for season, temps in season_averages.items()}
    return season_average_final

# Function to find the station with the largest temperature range
def find_largest_temp_range_station(data):
    station_ranges = {}

    for station, years_data in data.items():
        temp_ranges = []
        for year, monthly_data in years_data.items():
            max_temp = max(monthly_data.values())
            min_temp = min(monthly_data.values())
            temp_ranges.append(max_temp - min_temp)
        station_ranges[station] = max(temp_ranges)  # Store the largest range for the station

    # Find the station(s) with the largest temperature range
    max_range = max(station_ranges.values())
    largest_range_stations = [station for station, range_value in station_ranges.items() if range_value == max_range]

    return largest_range_stations, max_range

# Function to find the warmest and coolest stations
def find_warmest_and_coolest_station(data):
    station_temps = {}

    for station, years_data in data.items():
        max_temp = float('-inf')
        min_temp = float('inf')
        for year, monthly_data in years_data.items():
            max_temp = max(max_temp, max(monthly_data.values()))
            min_temp = min(min_temp, min(monthly_data.values()))
        station_temps[station] = {"warmest": max_temp, "coolest": min_temp}

    # Find the warmest and coolest station
    warmest_station = max(station_temps, key=lambda x: station_temps[x]["warmest"])
    coolest_station = min(station_temps, key=lambda x: station_temps[x]["coolest"])

    return warmest_station, station_temps[warmest_station]["warmest"], coolest_station, station_temps[coolest_station]["coolest"]

# Function to save results to files
def save_results_to_files(average_temp, largest_temp_range, warmest_and_coolest):
    # Save average temperatures to file
    with open("average_temp.txt", "w") as file:
        for season, avg_temp in average_temp.items():
            file.write(f"{season}: {avg_temp:.2f}°C\n")

    # Save the largest temperature range station to file
    with open("largest_temp_range_station.txt", "w") as file:
        file.write(f"Station(s) with largest temperature range: {', '.join(largest_temp_range[0])}\n")
        file.write(f"Largest temperature range: {largest_temp_range[1]:.2f}°C\n")

    # Save the warmest and coolest stations to file
    with open("warmest_and_coolest_station.txt", "w") as file:
        file.write(f"Warmest station: {warmest_and_coolest[0]} with {warmest_and_coolest[1]:.2f}°C\n")
        file.write(f"Coolest station: {warmest_and_coolest[2]} with {warmest_and_coolest[3]:.2f}°C\n")

def main():
    # Get the temperature data from the folder
    folder_path = '/Users/bisckoot/Desktop/Assingment 2/temperature_data'
    data = read_temperature_data(folder_path)

    # Calculate average temperatures for each season
    average_temp = calculate_average_temperatures(data)

    # Find the station with the largest temperature range
    largest_temp_range = find_largest_temp_range_station(data)

    # Find the warmest and coolest station(s)
    warmest_and_coolest = find_warmest_and_coolest_station(data)

    # Save the results to files
    save_results_to_files(average_temp, largest_temp_range, warmest_and_coolest)

    print("Results saved to files.")

if __name__ == "__main__":
    main()