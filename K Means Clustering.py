# -*- coding: utf-8 -*-
"""Tugas Damin.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12f7wNmBRa9C4HzVfOXjlvD2O4puABAfw
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'x' : [35, 13, 14, 25, 21, 45, 31, 20, 29, 43, 14, 87, 60, 65, 54, 55, 56, 19, 90],
    'y' : [36, 16, 10, 27, 17, 43, 27, 15, 33, 36, 9, 78, 55, 72, 49, 63, 60, 20, 84]
})

np.random.seed(200)
k = 3
centroids = {
    i+1: [np.random.randint(0, 80), np.random.randint(0, 80)]
    for i in range(k)
}

fig = plt.figure(figsize=(5,5))
plt.scatter(df['x'], df['y'], color='k')
colmap = {1: 'r', 2: 'g', 3: 'b'}
for i in centroids.keys():
  plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()

