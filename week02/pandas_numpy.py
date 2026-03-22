import pandas as pd

file_url = 'https://media.githubusercontent.com/media/mustha'
sample = pd.read_csv(file_url)

print(sample.head())
print(sample.ttail())