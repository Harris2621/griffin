import pandas as pd

# Load the dataset into a pandas dataframe
df = pd.read_csv('dark_patterns.csv')

# Get the unique pattern categories
unique_categories = pd.unique(df['Pattern Category'])

# Print the unique pattern categories
print(f'The unique pattern categories are: {unique_categories}')
