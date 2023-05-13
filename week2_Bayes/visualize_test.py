import numpy as np # Library for linear algebra and math utils
import pandas as pd # Dataframe library
import matplotlib.pyplot as plt # Library for plots
from utils import confidence_ellipse # Function to add confidence ellipses to charts
import os

current_path = os.getcwd()
# print(current_path)
data = pd.read_csv('./week2_Bayes/data/bayes_features.csv'); # Load the data from the csv file

# print(data.head(5)) # Print the first 5 tweets features. Each row represents a tweet

# Plot the samples using columns 1 and 2 of the matrix
fig, ax = plt.subplots(figsize = (8, 8)) #Create a new figure with a custom size

colors = ['red', 'green'] # Define a color palete
sentiments = ['negative', 'positive'] 

index = data.index

# Color base on sentiment
for sentiment in data.sentiment.unique():
    ix = index[data.sentiment == sentiment]
    ax.scatter(data.iloc[ix].positive, data.iloc[ix].negative, c=colors[int(sentiment)], s=0.1, marker='*', label=sentiments[int(sentiment)])

ax.legend(loc='best')    
    
# Custom limits for this chart
# plt.xlim(-250,0)
# plt.ylim(-250,0)

# plt.xlabel("Positive") # x-axis label
# plt.ylabel("Negative") # y-axis label
# plt.show()