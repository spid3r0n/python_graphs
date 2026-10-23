import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


G_grid = nx.grid_2d_graph(3, 3)
pos_grid = {(x, y): (x, y) for x, y in G_grid.nodes()}

plt.figure(figsize=(5, 5))
plt.title("Exercice 2 - Figure 1 (Grille 2x2)")
nx.draw(G_grid, pos=pos_grid, with_labels=False, node_size=100, node_color='black', edge_color='black')
plt.show()



G_star = nx.Graph()

# Les 6 sommets de l'étoile
nodes = [1, 2, 3, 4, 5, 6]
G_star.add_nodes_from(nodes)

edges = [
    (1, 3), (3, 5), (5, 1),  # Triangle 1
    (2, 4), (4, 6), (6, 2)   # Triangle 2
]
G_star.add_edges_from(edges)

# Calcul des coordonnées géométriques (espacées régulièrement sur un cercle)
angles = np.linspace(np.pi/2, np.pi/2 + 2*np.pi, 6, endpoint=False)
pos_star = {i+1: (np.cos(angle), np.sin(angle)) for i, angle in enumerate(angles)}

plt.figure(figsize=(5, 5))
plt.title("Exercice 2 - Figure 2 (Étoile)")
nx.draw(G_star, pos=pos_star, with_labels=False, node_size=100, node_color='black', edge_color='black')
plt.show()