import pandas as pd

# Load the CSV file into a pandas DataFrame
file_path = 'D:\\7\\66-psu\\year2\\semester2\\ba ai\\termpro-predictPM25\\clean_data\\pm-data.csv'
data = pd.read_csv(file_path)


# Drop columns with more than 50% NaN values
data.dropna(axis=1, thresh=1, inplace=True)

data['temperature'].fillna(data['temperature'].mean(), inplace=True)
data['pm_2_5'].fillna(data['pm_2_5'].mean(), inplace=True)

# Drop specific columns
columns_to_drop = ["timezone", "pm_10", "pm_2_5_sp"]
data.drop(columns=columns_to_drop, inplace=True, errors="ignore")

# Handle zeros separately
columns_to_handle_zeros = ['humidity', 'pm_2_5', 'temperature']


new_data = data.drop(index=range(2000, len(data)))
cleaned_file_path = 'D:\\7\\66-psu\\year2\\semester2\\ba ai\\termpro-predictPM25\\clean_data\\cleaned_data.csv'
new_data.to_csv(cleaned_file_path, index=False)