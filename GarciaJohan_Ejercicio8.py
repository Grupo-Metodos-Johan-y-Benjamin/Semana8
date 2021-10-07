# -*- coding: utf-8 -*-
import pandas
import numpy as np
import matplotlib.pyplot as plt
df = pandas.read_csv("https://raw.githubusercontent.com/diegour1/CompMetodosComputacionales/main/DataFiles/world_pop.csv")
anios=[]
valores=[]
for i in range(0,len(df["Entity"])):
    if (df["Entity"][i]== "Our World In Data") and (df["Year"][i] in range(700,1900)):
         valores.append(df["World Population"][i])   
         if df["Year"][i] not in anios:
             anios.append(df["Year"][i])
pts = len(valores)
x = np.array(tuple(anios))
y = np.array(tuple(valores))
dimensiones=(pts,5)
P = np.ones(dimensiones).reshape(5,pts).T
for i in range(0,len(valores)):
    P[i][1] = anios[i]
    P[i][2] = anios[i]**2
    P[i][3] = anios[i]**3
    P[i][4] = anios[i]**4
v = (np.linalg.inv(P.T @ P) @ P.T) @ y
b = v[0]
plt.plot(x, y, 'o')
plt.plot(x[::], (v[-1]*(x[::]**4))+(v[3]*(x[::]**3))+(v[2]*(x[::]**2))+(v[1]*x[::])+b, 'r', linewidth=3)
plt.savefig('GarciaJohan_grafica.png')
coeffs=(v[4],v[3],v[2],v[1])
print(f"coeffs 4to grado = {coeffs}")
