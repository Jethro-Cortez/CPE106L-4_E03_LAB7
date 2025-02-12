import pandas as pd
import matplotlib.pyplot as plt

# Load the data set
data = pd.read_csv('breadprice.csv')

# Print column names to verify
print("Column Names:", data.columns)

# Clean the data (you can add specific cleaning steps based on your data)
data.dropna(inplace=True)  # Drop rows with missing values

# Ensure the 'Year' column is of integer type and 'Value' column is of float type
data['Year'] = data['Year'].astype(int)
data['Value'] = data['Value'].astype(float)

# Group by 'Year' and calculate the average price for each year
average_price_per_year = data.groupby('Year')['Value'].mean()

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(average_price_per_year.index, average_price_per_year.values, marker='o')
plt.title('Average Price of Bread per Year')
plt.xlabel('Year')
plt.ylabel('Average Price (USD)')
plt.grid(True)
plt.show()
