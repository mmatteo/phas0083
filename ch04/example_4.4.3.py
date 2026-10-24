# Example 4.4.3 (Figure 4.11): The chain of Example 4.2.3 drawn $2000$ times: histogram and KDE of the released energies, and the normal pdf of variance $\sigma_0^2+\sigma^2$
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

E0, sigma0, sigma = 1000, 15, 20
N = 2000

# the chain: Doppler-shifted energy, then the released one
e = rng.normal(E0, sigma0, N)
e_rel = rng.normal(e, sigma)

# kernel density estimate, and the normal pdf to compare
kde = gaussian_kde(e_rel)
s = np.sqrt(sigma0**2 + sigma**2)
u = np.linspace(E0 - 4 * s, E0 + 4 * s, 200)

fig, ax = plt.subplots()
ax.hist(e_rel, bins=40, density=True, color=col.hist,
        label="histogram")
ax.plot(u, kde(u), color=col.emp, label="KDE")
ax.plot(u, norm.pdf(u, E0, s), **ref,
        label=r"$\mathcal{N}(E_0,\sigma_0^2+\sigma^2)$")
ax.set_xlabel("released energy $e'$ [keV]")
ax.set_ylabel("density")
ax.legend()
print(f"bandwidth: {kde.factor * e_rel.std():.1f} keV")

plt.show()
