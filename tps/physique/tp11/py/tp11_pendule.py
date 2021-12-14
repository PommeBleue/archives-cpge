#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from tp11_fonctions import periode_int, euler_deuxieme_ordre

############
# PARAMÈTRES
############
g = 9.81     # accélération de la pesanteur
l = 1        # longueur du pendule
m = 1        # masse 
k = 0.2

###################################################
# FONCTIONS ASSOCIÉES AUX ÉQUATIONS DIFFÉRENTIELLES
###################################################
def oh(V,t):
    """
    Fonction associée au pendule linéarisé (oscillateur harmonique)
    """
    x, y = V
    dx = y
    dy = - g/l * x
    dV = [dx, dy]
    return dV

def pendule(V,t):
    """
    Fonction associée au pendule simple
    """
    x, y = V
    return [y, -(g/l)*np.sin(x)-k*l*y]


###################################################
# FONCTIONS AUXILIARES 
###################################################
def periode(theta_0, t):
    """Fonction permettant de retrouver la période T
    du pendule pour une valeur de theta_0 donnée (et étant donné un tableau de temps t)
    """
    V0 = [theta_0, 0]
    V  = odeint(pendule, V0, t)
    v  = V[:,0]
    first = v[0]
    t1 = 0
    for i, e in enumerate(v):
        if e*first <= 0:
            t1 = t[i] 
            break
    return 4*t1


def borda(theta_0):
    """Fonction calculant la valeur de T(theta_0) selon la formule de Borda
    """
    return 2*np.pi*np.sqrt(l/g)*(1+(theta_0**2)/16)


def energie_cinetique(omega):
    return (1/2)*m*(l**2)*(omega**2)


def energie_potentielle(theta):
    return m*g*l*(1-np.cos(theta))


def energie_mecanique(theta, omega):
    return energie_cinetique(omega) + energie_potentielle(theta)


########################
# SIMULATIONS NUMÉRIQUES
########################
duree  = 10      # duree de la simulation
theta_max = 2*np.pi/3 # angle initial maximum
dtheta = 0.01
dt     = .001     # intervalle de temps entre deux instants successifs
t = np.linspace(0, duree, int(duree/dt))
#V0     = [np.pi, 0.1]  # conditions initiales
V0     = [np.pi, 0.1]  # conditions initiales
V1 = odeint(oh, V0, t) # intégration numérique de l'équation différentielle
V2 = odeint(pendule, V0, t) # intégration nuémrique de l'équation différentielle, sans approximations
#V2 = euler_deuxieme_ordre(pendule, V0, t) # intégration nuémrique de l'équation différentielle, sans approximations, en utilisant euler_deuxieme_ordre
theta_oh = V1[:,0]  # valeurs de theta pour l'oscillateur harmonique
omega_oh = V1[:,1]  # valeurs de omega pour l'oscillateur harmonique
theta = V2[:,0] # valeurs de theta
omega = V2[:,1] # valeurs de omega
thetas = np.linspace(0.1, theta_max, int(theta_max/dtheta))

############################
# REPRÉSENTATIONS GRAPHIQUES
############################
plt.figure(1)
plt.plot(t, theta_oh, label="Oscillateur Harmoniqe")
plt.plot(t, theta, label="Sans approxiamtions")
plt.title("Évolution de l'angle theta en fonction du temps")
plt.xlabel("Temps (s)")
plt.ylabel("Theta (rad)")
plt.legend(loc='upper right')

plt.figure(2)
plt.plot(thetas, [periode(theta, t) for theta in thetas], label="Sans Borda")
plt.plot(thetas, [borda(theta) for theta in thetas], label="Avec Borda")
plt.plot(thetas, [periode_int(theta) for theta in thetas], label="Sans Borda, num")
plt.title("Évolution de la période en fonction de la valeur initiale theta_0")
plt.xlabel("Theta_0 (rad)")
plt.ylabel("T (s)")
plt.legend(loc='upper right')

plt.figure(3)
plt.plot(t, energie_cinetique(omega), label="Énergie cinétique")
plt.plot(t, energie_potentielle(theta), label="Énergie potentielle")
plt.plot(t, energie_mecanique(theta, omega), label="Énergie mécanique")
plt.xlabel("Énergie (J)")
plt.ylabel("Temps (s)")
plt.legend(loc='upper right')

plt.show()
