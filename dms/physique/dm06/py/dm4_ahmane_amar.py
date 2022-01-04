"""Programme de résolution numérique d'une équation différentielle d'ordre 2
"""
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

# Defining private constants
_OMEGA_0 = 1.61e+3
_Q = 14
_OMEGA = _OMEGA_0*np.sqrt(1-1/(4*(_Q**2)))
_MU = _OMEGA_0/(2*_Q)
_E = 12.
_R = 6.
_C = 1e-5
_Q0 = _E*_C
_N = 1000


def charge_primaire(V, t):
	"""Fonction demandée à la question 8.
	"""
	x, y = V
	return [y, -y*(_OMEGA_0/_Q) + (_OMEGA_0**2)*(_Q0 - x)]


if __name__ == "__main__":	
	t = np.linspace(0, 0.05, _N)
	result = odeint(charge_primaire, [0, _E/_R], t)
	plt.plot(t, result[:,0], "-r", label="num")
	plt.plot(t, (-_Q0*np.cos(_OMEGA*t)+((_E/_R-_MU*_Q0)/_OMEGA)*np.sin(_OMEGA*t))*np.exp(-_MU*t) + _Q0, "-b", label="anal")
	plt.legend()
	plt.show()

