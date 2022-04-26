# Reading the Original Graph, Making the Second Set of Modifications, and Analysing the Resulting Balanced Graph
import networkx as nx
import numpy as np
import random
import itertools
import matplotlib.pyplot as plt

# Importing all the Required Functions from different_relation_predictions.py
from different_relation_predictions import *

# Loading the Original Network
G = nx.read_gml("original_graph.gml",None)

# Analysis 2 - Changing the India-Ukraine edge to +2, India-Russia to -4, China-Russia to +4, China-Ukraine to -4
G2 = G.copy()
nx.set_edge_attributes(G2,{("India","Ukraine"):{'weight':"2.0",'sign':"+"}})
nx.set_edge_attributes(G2,{("India","Russia"):{'weight':"-4.0",'sign':"-"}})
nx.set_edge_attributes(G2,{("China","Russia"):{'weight':"4.0",'sign':"+"}})
nx.set_edge_attributes(G2,{("China","Ukraine"):{'weight':"-4.0",'sign':"-"}})

# Stabilizing the Network and Writing it into a New Graph
stabilize_graph(G2)
nx.write_gml(G2,"analysis2.gml")