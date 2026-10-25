# Example A.5.2 (Figure A.4): A mixture sample with its signal bin and side bands, and the on/off estimates read from the three counts
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

# the mixture: weight, peak position and width
w = 0.25
mu = 0
sigma = 1
# the measured range and the sample size
a = -8
b = 8
N = 800

# the sample, event by event: signal or background, then x
z = rng.random(N) < w
x = np.where(z, rng.normal(mu, sigma, N),
             rng.uniform(a, b, N))
# the counts in the signal bin and in the two side bands
x_cnt = np.sum((x > -4) & (x < 4))
y_cnt = N - x_cnt

# the fraction of the signal in the signal bin, and of the
# background in the signal bin and in the side bands
w_lam_x = norm.cdf(4) - norm.cdf(-4)
w_nu_x = 0.5
w_nu_y = 0.5
# the on/off estimates from the counts
nu_hat = y_cnt / w_nu_y
lam_hat = max(0, x_cnt - nu_hat * w_nu_x) / w_lam_x
print(f"generated: {z.sum()} signal, {N - z.sum()} bkg")
print(f"counts: x = {x_cnt}, y = {y_cnt}")
print(f"estimates: lambda {lam_hat:.0f}, nu {nu_hat:.0f}")

fig, ax = plt.subplots()
ax.hist(x, bins=32, range=(a, b), color=col.hist)
ax.axvspan(-8, -4, color=col.cdf, alpha=0.15)
ax.axvspan(4, 8, color=col.cdf, alpha=0.15)
ax.axvspan(-4, 4, color=col.pdf, alpha=0.10)
ax.set_xlabel("$x$")
ax.set_ylabel("counts per bin")

plt.show()
