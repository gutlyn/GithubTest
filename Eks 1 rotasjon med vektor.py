# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 12:01:44 2024

@author: gutlyn
"""

import matplotlib.pyplot as plt
import numpy as np

# Definer vektoren
vector = np.array([1, -2])

# Definer rotasjonsmatrisen for XX grader
theta = np.radians(60)
rotation_matrix = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta), np.cos(theta)]
])

# print matrix and vector
print(*['Rotasjonsmatrisen', rotation_matrix], sep="\n")
print(*['vektoen Bx_By', rotation_matrix @ vector], sep="\n")
# Roter vektoren
rotated_vector = rotation_matrix.dot(vector)

# Opprett en figur og akse
fig, ax = plt.subplots()

# Sett grensene for plottet
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

# Plott den originale vektoren
ax.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='r', label='Original Vector')

# Plott den roterte vektoren
ax.quiver(0, 0, rotated_vector[0], rotated_vector[1], angles='xy', scale_units='xy', scale=1, color='b', label='Rotated Vector')

# Legg til rutenett og etiketter
ax.grid()
ax.set_xlabel('X-akse')
ax.set_ylabel('Y-akse')
ax.set_title('Vektorrotasjon i et koordinatsystem')
ax.legend()

# Vis plottet
plt.show()
