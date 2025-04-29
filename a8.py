from neural import *
import pandas as pd
print("<<<<<<<<<<<<<< XOR >>>>>>>>>>>>>>\n")

def normalize(data: List[Tuple[List[float], List[float]]]):
    """Makes the data range for each input feature from 0 to 1

    Args:
        data - list of (input, output) tuples

    Returns:
        normalized data where input features are mapped to 0-1 range (output already
        mapped in parse_line)
    """
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

# print("\n\nTraining h\n\n")
# h_data = [
#     ([1, 0, 1, 0, 0, 0], [1]),
#     ([1, 0, 1, 1, 0, 0], [1]),
#     ([1, 0, 1, 0, 1, 0], [1]),
#     ([1, 1, 0, 0, 1, 1], [1]),
#     ([1, 1, 1, 1, 0, 0], [1]),
#     ([1, 0, 0, 0, 1, 1], [1]),
#     ([1, 0, 0, 0, 1, 0], [0]),
#     ([0, 1, 1, 1, 0, 1], [1]),
#     ([0, 1, 1, 0, 1, 1], [0]),
#     ([0, 0, 0, 1, 1, 0], [0]),
#     ([0, 1, 0, 1, 0, 1], [0]),
#     ([0, 0, 0, 1, 0, 1], [0]),
#     ([0, 1, 1, 0, 1, 1], [0]),
#     ([0, 1, 1, 1, 0, 0], [0]),
# ]

# h = NeuralNet(6, 5, 1)
# h.train(h_data)

# print(h.get_ih_weights())
# print()
# print(h.get_ho_weights())

# print(h.evaluate([1, 1, 1, 1, 1, 1]))
# print(h.evaluate([0, 0, 0, 0, 0, 0]))
# print()
# print(h.evaluate([1, 0, 0, 0, 0, 0]))  
# print(h.evaluate([0, 1, 0, 0, 0, 0]))  
# print(h.evaluate([0, 0, 1, 0, 0, 0]))  
# print(h.evaluate([0, 0, 0, 1, 0, 0]))  
# print(h.evaluate([0, 0, 0, 0, 1, 0]))  
# print(h.evaluate([0, 0, 0, 0, 0, 1]))  

# h_data = [
#     ([0, 0], [0]),
#     ([0, 1], [1]),
#     ([1, 0], [1]),
#     ([1, 1], [0]),
    
# ]

# h = NeuralNet(2, 1, 1)
# h.train(h_data)

# print(h.get_ih_weights())
# print()
# print(h.get_ho_weights())
# print(h.evaluate([0, 0]))  
# print(h.evaluate([0, 1]))  
# print(h.evaluate([1, 0]))  
# print(h.evaluate([1, 1]))
# h_data = [
#     ([0.9, 0.6,0.8,0.3,0.1], [1.0]),
#     ([0.8, 0.8,0.4,0.6,0.4], [1.0]),
#     ([0.7, 0.2,0.4,0.6,0.3], [1.0]),
#     ([0.5, 0.5,0.8,0.4,0.8], [0.0]),
#     ([0.3, 0.1,0.6,0.8,0.8], [0.0]),
#     ([0.6, 0.3,0.4,0.3,0.6], [0.0]),
    
# ]

# h = NeuralNet(5, 9, 1)
# h.train(h_data)

# print(h.get_ih_weights())
# print()
# print(h.get_ho_weights())
# print(h.evaluate([1.0,1.0,1.0,0.1,0.1]))  
# print(h.evaluate([0.5,0.2,0.1,0.7,0.7]))  
# print(h.evaluate([0.8,0.3,0.3,0.3,0.8]))  
# print(h.evaluate([0.9,0.8,0.8,0.3,0.6]))


#ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity,Potability


df = pd.read_csv("waterQ.csv")

# Extract specific columns
columnsToextract = [
    "ph", "Hardness", "Solids", "Chloramines",
    "Sulfate", "Conductivity", "Organic_carbon",
    "Trihalomethanes", "Turbidity", "Potability"
]

waterData = df[columnsToextract]
waterData=normalize(waterData)
nwaterData=[
    (row[:-1].tolist(), [row[-1]]) for row in waterData.values
]