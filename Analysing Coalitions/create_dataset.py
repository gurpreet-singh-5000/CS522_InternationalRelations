import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
import itertools
import pandas as pd

#Creating the graph and adding nodes.

G = nx.Graph()
G.add_nodes_from(range(1, 31))

countries_dict = {"Ukraine": 1, 
                  "United-States": 2,
                  "Philippines": 3,
                  "Chile": 4,
                  "Canada": 5,
                  "United-Kingdom": 6,
                  "France": 7,
                  "Germany": 8,
                  "Spain": 9,
                  "Italy": 10,
                  "Japan": 11,
                  "South-Korea": 12,
                  "Australia": 13,
                  "Jamaica": 14,
                  "Libya": 15,
                  "Russia": 16,
                  "China": 17,
                  "Vietnam": 18,
                  "Iran": 19,
                  "North-Korea": 20,
                  "India": 21,
                  "Brazil": 22,
                  "Mexico": 23,
                  "Pakistan": 24,
                  "Singapore": 25,
                  "South-Africa": 26,
                  "Egypt": 27,
                  "Malaysia": 28,
                  "Saudi-Arabia": 29,
                  "United-Arab-Emirates": 30}

#Adding '+' sign for good relations (if Vote = For) between Ukraine and country 'i'
for i in range(2,16):
    G.add_edge(1,i, sign='+', weight = 10)
    
#Adding '-' sign for good relations (if Vote = Against | Abstained) between Ukraine and country 'i'
for i in range(16,31):
    G.add_edge(1, i, sign='-', weight = 10)

#Adding edges between different countries based on their general relationship with the other country
df = pd.read_csv('small-data-weighted.csv')
from_node = np.array(df['source'])
to_node = np.array(df['target'])
signs = np.array(df['sign'])
weights = np.array(df['weight'])

for i in range(len(from_node)):
    key = from_node[i]
    node1 = int(countries_dict[key])
    key = to_node[i]
    node2 = int(countries_dict[key])
    sign = signs[i]
    wt = weights[i]
    G.add_edge(node1, node2, sign = sign, weight = wt)

nx.draw(G)
plt.show()










