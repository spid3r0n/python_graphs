import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# =====================================================================
# Exercise 1: Représenter le graphe non orienté G = (X, U)
# =====================================================================
G1 = nx.Graph()

# Ajout des sommets
G1.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F'])

# Ajout des arêtes
edges_ex1 = [
    ('A', 'B'), ('A', 'D'), ('A', 'E'),
    ('B', 'C'), ('B', 'D'),
    ('C', 'D'), ('C', 'E'),
    ('D', 'E')
]
G1.add_edges_from(edges_ex1)

# Affichage du graphe de l'exercice 1
plt.figure(figsize=(6, 5))
plt.title("Exercice 1")
nx.draw(G1, with_labels=True, node_color='lightblue', node_size=700, font_weight='bold')
plt.show()


