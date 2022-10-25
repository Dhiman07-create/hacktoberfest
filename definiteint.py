import matplotlib.pyplot as plt
import numpy as np


def f(x):
	return x**2


def g(x):
	return x**(1/2)


x = np.linspace(0, 2, 1000)
plt.plot(x, f(x))
plt.plot(x, g(x))
plt.fill_between(x, f(x), g(x), where=[(x > 0) and (x < 2) for x in x])
plt.show()
