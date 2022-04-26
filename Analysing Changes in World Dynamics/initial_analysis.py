# Reading the Original Graph, and Performing the Initial Stabilization
import networkx as nx
import numpy as np
import random
import itertools
import matplotlib.pyplot as plt

# Importing all the Required Functions from different_relation_predictions.py
from different_relation_predictions import *

# Creating the Graph from the dataset and visualising it
G = create_graph_from_edges("signed-unsigned-data.csv")
nx.write_gml(G,"original_graph.gml")
edge_labels = nx.get_edge_attributes(G,'sign')
pos = nx.circular_layout(G)
nx.draw(G)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,font_size=10)
plt.show()


# Stabilizing the Graph and Visualizing it
stabilize_graph(G)
nx.write_gml(G,"stabilized_original_graph.gml")
edge_labels = nx.get_edge_attributes(G,'sign')
pos = nx.circular_layout(G)
nx.draw(G)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,font_size=10)
plt.show()