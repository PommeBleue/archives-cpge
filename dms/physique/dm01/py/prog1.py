import numpy as np
import matplotlib.pyplot as plt

############
# PARAMÈTRES
############
R = 1      # rayon du dioptre sphérique (en mètres)
n = 1.51     # indice de la lentille
hmax = 0.3   # distance maximale du rayon incident (en mètres) (initialement c'était 0.7)
N = 10

##########################
# PRÉPARATION DE LA FIGURE
##########################
fig = plt.figure(figsize=(12,8))
plt.plot([-2*R, 5*R], np.zeros(2), "--k") # axe optique
fig.axes[0].set_aspect("equal") # même échelle sur les deux axes
plt.xlim(-2*R, 5*R)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
# Dioptre sphérique
theta = np.linspace(-np.pi/2, np.pi/2, 101)
xd = R * np.cos(theta) - R
yd = R * np.sin(theta)
plt.plot(xd, yd, "k")
plt.plot([xd[0], xd[-1]], [yd[0], yd[-1]], "k")

#################
# TRACÉ DE RAYONS
#################
s = 0
for h in np.linspace(-hmax, hmax, N):
    # Coordonnées des différents points
    xA, yA = (-2 * R, h)                 # coordonnées du point A
    xI, yI = (-R, h)                     # coordonnées du point I
    xJ, yJ = (np.sqrt(R**2 - h**2)-R, h) # coordonnées du point J
    # Angles au niveau du dioptre sphérique
    i = np.arcsin(h / R)     # angle d'incidence
    r = np.arcsin(n * h / R) # angle de réfraction
    xK, yK = (xJ + h / np.tan(r-i), 0)   # coordonnées du point K
    xB, yB = (2*xK-xJ, -h)               # coordonnées du point B
    # Tracé de la marche des rayons
    x = [xA, xI, xJ, xK, xB]
    s += xK
    y = [yA, yI, yJ, yK, yB]
    plt.plot(x, y, "red")
print(s/N)
plt.show()
