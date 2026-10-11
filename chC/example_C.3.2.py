# Example C.3.2 (Figure C.1): Energy calibration of a detector: pulse heights measured at six known line energies, with their errors, and the least-squares line
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

E = np.array([60, 122, 356, 662, 1173, 1332])  # keV
a_true, b_true = 20, 1.5          # offset, gain
sigma = np.array([5, 5, 8, 10, 15, 15])        # channels
h = rng.normal(a_true + b_true * E, sigma)     # heights

# weighted least squares: the normal equations
wt = 1 / sigma**2
S, Sx, Sy = wt.sum(), (wt * E).sum(), (wt * h).sum()
Sxx, Sxy = (wt * E**2).sum(), (wt * E * h).sum()
D = S * Sxx - Sx**2
a_hat = (Sxx * Sy - Sx * Sxy) / D
b_hat = (S * Sxy - Sx * Sy) / D
var_a, var_b, cov_ab = Sxx / D, S / D, -Sx / D
chi2_min = np.sum(((h - a_hat - b_hat * E) / sigma)**2)
print(f"a = {a_hat:.1f} +- {var_a**0.5:.1f}, "
      f"b = {b_hat:.4f} +- {var_b**0.5:.4f}")
print(f"chi2 = {chi2_min:.2f} for {E.size - 2} degrees of"
      f" freedom, p = {chi2.sf(chi2_min, E.size - 2):.2f}")

t = np.linspace(0, 1400, 2)
fig, ax = plt.subplots()
ax.errorbar(E, h, yerr=sigma, fmt="o", color=col.data,
            ms=3, label="data")
ax.plot(t, a_hat + b_hat * t, color=col.pdf, label="fit")
ax.set_xlabel("energy [keV]")
ax.set_ylabel("pulse height [channels]")
ax.legend()

plt.show()
