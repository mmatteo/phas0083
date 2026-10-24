# Example 4.2.3 (Figure 4.7): The chain drawn $2000$ times: the energy released in the detector against the Doppler-shifted energy of each photon, with the diagonal $e'=e$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

E0, sigma0 = 1000, 15   # line energy, Doppler width, keV
sigma = 20               # detector resolution, keV
N = 2000                 # draws of the chain

# vectorised: one call draws the N values, no Python loop
e = rng.normal(E0, sigma0, N)     # Doppler-shifted
# a vector of means: the N conditional draws in one call
e_rel = rng.normal(e, sigma)      # released, given each e
print(f"std of the Doppler-shifted energies: {e.std():.1f}")
print(f"std of the released ones: {e_rel.std():.1f} keV"
      f" (sqrt(15^2 + 20^2) = {np.hypot(15, 20):.1f})")

fig, ax = plt.subplots()
ax.plot(e, e_rel, "o", color=col.emp, ms=2, alpha=0.3)
lims = [E0 - 4 * sigma0, E0 + 4 * sigma0]
ax.plot(lims, lims, **ref, label="$e'=e$")
ax.set_xlabel("Doppler-shifted energy $e$ [keV]")
ax.set_ylabel("released energy $e'$ [keV]")
ax.legend()

plt.show()
