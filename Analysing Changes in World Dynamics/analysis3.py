# Reading the Original Graph, Making the Third Set of Modifications, and Analysing the Resulting Balanced Graph
import networkx as nx
import numpy as np
import random
import itertools
import matplotlib.pyplot as plt

# Importing all the Required Functions from different_relation_predictions.py
from different_relation_predictions import *

# Loading the Original Network
G = nx.read_gml("original_graph.gml",None)

# Analysis 3 - Changing the Russia-Ukraine edge to +4
G3 = G.copy()
nx.set_edge_attributes(G3,{("Russia","Ukraine"):{'weight':"4.0",'sign':'+'}})

# Stabilizing the Network and Writing it into a New Graph
stabilize_graph(G3)
nx.write_gml(G3,"analysis3.gml")