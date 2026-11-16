# Example 4.2.3 (Figure 4.7): The chain drawn $2000$ times: the energy released in the detector against the Doppler-shifted energy of each photon, with the diagonal $e'=e$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

E0 = 1000
sigma0 = 15
sigma = 20
N = 2000

e = rng.normal(E0, sigma0, size=N)
e_rel = rng.normal(e, sigma)
s = np.sqrt(sigma0**2 + sigma**2)
print(f"std of Doppler-shifted energy: {e.std():.1f}")
print(f"std of released energies: {e_rel.std():.1f}")
print(f"sqrt({sigma0}^2 + {sigma}^2) = {s:.1f}")

lims = [E0 - 4 * sigma0, E0 + 4 * sigma0]
fig, ax = plt.subplots()
ax.plot(e, e_rel, "o", color=col.draws, ms=2, alpha=0.3)
ax.plot(lims, lims, color=col.ref, ls="--", label="$e'=e$")
ax.set_xlabel("Doppler-shifted energy $e$ [keV]")
ax.set_ylabel("released energy $e'$ [keV]")
ax.legend()

plt.show()
