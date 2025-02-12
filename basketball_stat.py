import pandas as pd

def cleanStats(df):
    # Define the columns to be cleaned
    columns_to_clean = ['FG', '3PT', 'FT']
    
    for col in columns_to_clean:
        # Split the column into two new columns
        makes_attempts = df[col].str.split('-', expand=True)
        makes_col = col + 'M'
        attempts_col = col + 'A'
        
        # Add the new columns to the dataframe
        df[makes_col] = makes_attempts[0].astype(int)
        df[attempts_col] = makes_attempts[1].astype(int)
        
        # Drop the original column
        df.drop(columns=[col], inplace=True)
    
    return df

# Load the data frame from the CSV file
df = pd.read_csv('rawbrogdonstats.csv')

# Clean the data frame
cleaned_df = cleanStats(df)

# Display the cleaned data frame in a table-like format
print(cleaned_df.to_markdown(index=False))