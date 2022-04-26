# Reading the Original Graph, Making the First Set of Modifications, and Analysing the Resulting Balanced Graph
import networkx as nx
import numpy as np
import random
import itertools
import matplotlib.pyplot as plt

# Importing all the Required Functions from different_relation_predictions.py
from different_relation_predictions import *

# Loading the Original Network
G = nx.read_gml("original_graph.gml",None)

# Analysis 1 - Changing the USA-Russia edge to +4, USA-UK to -3, Ukraine-USA to -3, Ukraine-UK to -4
G1 = G.copy()
nx.set_edge_attributes(G1,{("United-States","Russia"):{'weight':"4.0",'sign':"+"}})
nx.set_edge_attributes(G1,{("United-States","United-Kingdom"):{'weight':"-3.0",'sign':"-"}})
nx.set_edge_attributes(G1,{("Ukraine","United-Kingdom"):{'weight':"-3.0",'sign':"-"}})
nx.set_edge_attributes(G1,{("United-States","Russia"):{'weight':"-4.0",'sign':"-"}})

# Stabilizing the Network and Writing it into a New Graph
stabilize_graph(G1)
nx.write_gml(G1,"analysis1.gml")