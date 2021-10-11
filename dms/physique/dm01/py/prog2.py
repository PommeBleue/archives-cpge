import numpy as np
import matplotlib.pyplot as plt

############
# PARAMÈTRES
############
R = 1        # rayon du dioptre sphérique (en mètres)
n = 1.51     # indice de la lentille
hmax = 0.5   # distance maximale du rayon incident (en mètres)
N = 6

##########################
# PRÉPARATION DE LA FIGURE
##########################
plt.figure(figsize=(16,12))
ax1 = plt.subplot2grid((2,1), (0,0))
ax2 = plt.subplot2grid((2,1), (1,0))
ax1.set_title("Configuration initiale")
ax2.set_title("Configuration inversée")
for ax in [ax1, ax2]:
    ax.set_aspect("equal")
    ax.set_xlim(-2*R, 3*R)
    ax.plot([-2*R, 5*R], np.zeros(2), "--k") # axe optique 
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
# Dioptre sphérique (sens ordinaire)
theta = np.linspace(-np.pi/2, np.pi/2, 101)
xd = R * np.cos(theta) - R
yd = R * np.sin(theta)
ax1.plot(xd, yd, "k")
ax1.plot([xd[0], xd[-1]], [yd[0], yd[-1]], "k")
# Dioptre sphérique (sens inversé)
theta = np.linspace(-np.pi/2, np.pi/2, 101)
xd = -R * np.cos(theta)
yd = R * np.sin(theta)
ax2.plot(xd, yd, "k")
ax2.plot([xd[0], xd[-1]], [yd[0], yd[-1]], "k")

#################
# TRACÉ DE RAYONS
#################
# Configuratiuon initiale
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
    y = [yA, yI, yJ, yK, yB]
    ax1.plot(x, y, "red")
# Configuration inversée
for h in np.linspace(-hmax, hmax, N):
    # Coordonnées des différents points
    xA, yA = (-2 * R, h)                 # coordonnées du point A
    xI, yI = (-np.sqrt(R**2 - h**2), h)  # coordonnées du point I
    # Angles au niveau des dioptres
    alpha = np.arctan(h / R)
    i1 = np.arcsin(np.sin(alpha)/n)
    i2 = alpha - i1
    i3 = np.arcsin(n*np.sin(i2))
    x0 = - np.sqrt(R**2 - h**2)
    y0 = h - (R - x0) * np.tan(i2)
    L = y0 / np.tan(i3)
    xJ, yJ = (0, y0)                     # coordonnées du point J
    xK, yK = (L, 0)                      # coordonnées du point K
    xB, yB = (2*L, -y0)                  # coordonnées du point B
    # Tracé de la marche des rayons
    x = [xA, xI, xJ, xK, xB]
    y = [yA, yI, yJ, yK, yB]
    ax2.plot(x, y, "red")
plt.show()
