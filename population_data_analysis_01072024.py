import pandas as pd
import matplotlib.pyplot as plt

# Loading the data from the CSV file
df = pd.read_csv(r'C:\\Users\\Leander Chris\\OneDrive\\Desktop\\PRODIGY_DS_01\\API_SP.POP.TOTL_DS2_en_csv_v2_21117.csv')

# Print the entire DataFrame to check its content
print(df)

# Print the first 5 rows of the DataFrame
print(df.head())

# Print the last 5 rows of the DataFrame
print(df.tail())

# Print the shape of the DataFrame (number of rows and columns)
print(df.shape)

# Print the column names of the DataFrame
print(df.columns)

# Print the data types of each column
print(df.dtypes)

# Print a concise summary of the DataFrame
print(df.info())

# Print summary statistics of the DataFrame (for numerical columns)
print(df.describe())




