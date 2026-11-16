# Example A.5.2 (Figure A.4): A mixture sample with its signal bin and side bands, and the on/off estimates read from the three counts
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

# the mixture: weight, peak position and width
w = 0.25
mu = 0
sigma = 1
# the range, the half-width of the signal bin, the size
a = -8
b = 8
half = 4
N = 800

# the sample, event by event: signal or background, then x
z = rng.random(size=N) < w
x = np.where(z, rng.normal(mu, sigma, size=N),
             rng.uniform(a, b, size=N))
# the counts in the signal bin and in the two side bands
x_cnt = np.sum(np.abs(x) < half)
y_cnt = N - x_cnt

# fractions of signal and background in each region
w_lam_x = norm.cdf(half) - norm.cdf(-half)
w_nu_x = 2 * half / (b - a)
w_nu_y = 1 - w_nu_x
# the on/off estimates from the counts
nu_hat = y_cnt / w_nu_y
lam_hat = max(0, x_cnt - nu_hat * w_nu_x) / w_lam_x
print(f"generated: {z.sum()} signal, {N - z.sum()} bkg")
print(f"counts: x = {x_cnt}, y = {y_cnt}")
print(f"estimates: lambda {lam_hat:.0f}, nu {nu_hat:.0f}")

fig, ax = plt.subplots()
ax.hist(x, bins=32, range=(a, b), color=col.hist)
ax.axvspan(a, -half, color="tab:orange", alpha=0.15)
ax.axvspan(half, b, color="tab:orange", alpha=0.15)
ax.axvspan(-half, half, color="tab:blue", alpha=0.10)
ax.set(xlabel="$x$", ylabel="counts per bin")

plt.show()
