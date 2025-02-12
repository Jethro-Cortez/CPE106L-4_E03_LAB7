
import pandas as pd
import matplotlib.pyplot as plt
import os

# Check if breadprice.csv exists in the same directory
file_name = 'breadprice.csv'
if os.path.exists(file_name):
    # Load the data set
    data = pd.read_csv(file_name)

    # Clean the data
    # Convert 'Year' and 'Value' columns to numeric types
    data['Year'] = pd.to_numeric(data['Year'], errors='coerce')
    data['Value'] = pd.to_numeric(data['Value'], errors='coerce')

    # Group by 'Year' and calculate the average price for each year
    average_price_per_year = data.groupby('Year')['Value'].mean().reset_index()

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(average_price_per_year['Year'], average_price_per_year['Value'], marker='o')
    plt.title('Average Price of Bread per Year')
    plt.xlabel('Year')
    plt.ylabel('Average Price (USD)')
    plt.grid(True)
    plt.show()
else:
    print(f"{file_name} not found in the current directory.")
