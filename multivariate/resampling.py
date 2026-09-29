# Simulated distribution of the velocity $V=D/T$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

N = 10_000_000
T = rng.normal(10, 1, N)
D = rng.uniform(99, 101, N)
V = D / T

fig, ax = plt.subplots()
ax.hist(V, bins=100, density=True, color=col.hist)
ax.set_xlabel("$V$ [cm/s]")
ax.set_ylabel("density")

plt.show()
