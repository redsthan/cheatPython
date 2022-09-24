import numpy as np              # On importe numpy en choisissant le nom raccourci np
import matplotlib.pyplot as plt   # On importe pyplot en choisissant le nom raccourci plt

A = 0.005        # A amplitude en m
T = 0.002        # T période en s
phi = 0          # phi phase à l'origine en rad

A3 = 0.005 / 3
T3 = T / 3
phi3 = 0

tmin = 0         # valeur minimale de l'intervalle de temps
tmax = 3*T       # valeur maximale
N = 100          # nombre de points

t = np.linspace(tmin,tmax,N)    # création d'un tableau de N valeurs

y = A*np.sin(2*np.pi/T*t + phi)        # y(t)

y3 = A3*np.sin(2*np.pi/T3*t + phi3)                                

# Représentation graphique
plt.close()       # efface la figure courante

plt.plot(t,y,color="red",linestyle="-",label="Fonction sinus")
plt.plot(t,y3,color="blue",linestyle="-",label="Fonction sinus")

plt.title("Représentation de deux fonctions sinusoïdales")
plt.xlabel("t")
plt.ylabel("y et y3")
plt.grid(True)          # affiche une grille
plt.show()
