from neural import *
import pandas as pd
from typing import Tuple, List
import csv

print("<<<<<<<<<<<<<< XOR >>>>>>>>>>>>>>\n")

def reverseparse_line(line: str) -> Tuple[List[float], List[float]]:
    tokens = line.split(",")
    if len(tokens) < 2:
        raise ValueError(f"Invalid line format: {line}")
    inputs = [float(token) for token in tokens[:-1]]
    output = [float(tokens[-1])]  
    return inputs, output
    
def normalize(data: List[Tuple[List[float], List[float]]]):
    """Makes the data range for each input feature from 0 to 1."""
    leasts = len(data[0][0]) * [100.0]
    mosts = len(data[0][0]) * [0.0]

    for i in range(len(data)):
        for j in range(len(data[i][0])):
            if data[i][0][j] < leasts[j]:
                leasts[j] = data[i][0][j]
            if data[i][0][j] > mosts[j]:
                mosts[j] = data[i][0][j]

    for i in range(len(data)):
        for j in range(len(data[i][0])):
            data[i][0][j] = (data[i][0][j] - leasts[j]) / (mosts[j] - leasts[j])
    return data

# Use pandas to handle missing values
df = pd.read_csv('waterQ.csv')

# Replace missing values with the median of each column
df.fillna(df.median(), inplace=True)

# Save the cleaned dataset back to a CSV file for further processing
df.to_csv('cleaned_waterQ.csv', index=False)

# Process the cleaned dataset
waterTData = []
with open('cleaned_waterQ.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        line = ",".join(row)
        try:
            inputs, output = reverseparse_line(line)
            waterTData.append((inputs, output))
        except ValueError as e:
            print(f"Skipping invalid line: {e}")

# Normalize the data and train the neural network

waterTData = normalize(waterTData)
wat = NeuralNet(9, 20, 1)  
wat.train(waterTData, learning_rate=0.01)
print(wat.get_ih_weights())
print(wat.get_ho_weights())


