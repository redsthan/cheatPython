import numpy as np           # On importe numpy en choisissant le nom raccourci np
import matplotlib.pyplot as plt   # On importe pyplot en choisissant le nom raccourci plt

A = 0.005        # A amplitude en m
T = 0.002        # T période en s
phi = 0          # phi phase à l'origine en rad

A2 = 0.005 / 2
T2 = T
phi2 = 0

tmin = 0         # valeur minimale de l'intervalle de temps
tmax = 3*T       # valeur maximale
N = 100          # nombre de points

t = np.linspace(tmin,tmax,N)    # création d'un tableau de N valeurs

y = A*np.sin(2*np.pi/T*t + phi)        # y(t)

y2 = A2*np.sin(2*np.pi/T2*t + phi2)       # y2(t)   A COMPLETER

# Représentation graphique
plt.clf()           # efface la figure courante
    
plt.plot(t,y,color="red",linestyle="-",label="Fonction sinus")
plt.plot(t,y2,color="blue",linestyle="-",label="Fonction sinus")    

plt.title("Représentation de deux fonctions sinusoïdales")
plt.xlabel("t")
plt.ylabel("y et y2")
plt.grid(True)          # affiche une grille
plt.show()
