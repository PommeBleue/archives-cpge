#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Fonctions utiles pour le TP11 """

import numpy as np
from scipy.integrate import quad


g = 9.81     # accélération de la pesanteur
l = 1        # longueur du pendule


def periode_int(theta0):
    """
    Calcul numérique de la valeur de la période, pour une amplitude theta0
    theta0 doit être une valeur unique"""
    def period(x):
        return -1 / np.sqrt(2 * (np.cos(x) - np.cos(theta0)))
    return 4 * quad(period, theta0, 0)[0] / np.sqrt(g/l)

def euler_deuxieme_ordre(f, V0, t):
    """
    Intègre numériquement une équation du second ordre
    en utilisant la méthode d'euler explicite.
        PARAMÈTRES :
        f : fonction associée à l'équation différentielle
        V0: conditions initiales
        t : tableau des instants auxquels évaluer la solution x(t)
        RENVOIE :
        Tableau contenant les valeurs de x(t) et de sa dérivée
    """
    dt = t[1] - t[0]
    x  = np.zeros(len(t))
    v = np.zeros(len(t))
    x[0] = V0[0]
    v[0] = V0[1]
    V = [np.array([x[0],v[0]])]
    for i in range(len(t)-1):
        dx, dv = f([x[i], v[i]], t[i])
        x[i+1] = x[i] + dt * dx
        v[i+1] = v[i] + dt * dv
        V.append(np.array([x[i+1],v[i+1]]))
    return np.array(V)

