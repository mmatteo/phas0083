# Example C.3.2 (Figure C.1): Energy calibration of a detector: pulse heights measured at six known line energies, with their errors, and the least-squares line
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

# the line energies in keV, the true offset and gain, and
# the errors on the pulse heights in channels
E = np.array([60, 122, 356, 662, 1173, 1332])
a_true = 20
b_true = 1.5
sigma = np.array([5, 5, 8, 10, 15, 15])
# the measured pulse heights
h = rng.normal(a_true + b_true * E, sigma)

# weighted least squares: the sums of the normal equations
wt = 1 / sigma**2
S = wt.sum()
Sx = (wt * E).sum()
Sy = (wt * h).sum()
Sxx = (wt * E**2).sum()
Sxy = (wt * E * h).sum()
D = S * Sxx - Sx**2
# the estimates, their variances and covariance
a_hat = (Sxx * Sy - Sx * Sxy) / D
b_hat = (S * Sxy - Sx * Sy) / D
var_a = Sxx / D
var_b = S / D
cov_ab = -Sx / D
# the chi-square at the minimum and its p-value
chi2_min = np.sum(((h - a_hat - b_hat * E) / sigma)**2)
print(f"a = {a_hat:.1f} +- {var_a**0.5:.1f}")
print(f"b = {b_hat:.4f} +- {var_b**0.5:.4f}")
print(f"chi2 = {chi2_min:.2f} for {E.size - 2} dof, "
      f"p = {chi2.sf(chi2_min, E.size - 2):.2f}")

t = np.linspace(0, 1400, 2)
fig, ax = plt.subplots()
ax.errorbar(E, h, yerr=sigma, fmt="o", color=col.data,
            ms=3, label="data")
ax.plot(t, a_hat + b_hat * t, color=col.pdf, label="fit")
ax.set_xlabel("energy [keV]")
ax.set_ylabel("pulse height [channels]")
ax.legend()

plt.show()
