# Example 6.2.6 (Figure 6.5): Arrival times of two photons in order of arrival, in a sample of $n=1000$ pairs, with their sample means, variances and correlation coefficient
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

n = 1000

# one realisation of the sample: the two arrival times,
# then the two of each pair in order of arrival
U1 = rng.uniform(0, 1, size=n)
U2 = rng.uniform(0, 1, size=n)
T1 = np.minimum(U1, U2)
T2 = np.maximum(U1, U2)

# sample means
T1_bar = np.sum(T1) / n
T2_bar = np.sum(T2) / n

# sample variances: the sum of squares divided by n - 1
S2_T1 = np.sum((T1 - T1_bar)**2) / (n - 1)
S2_T2 = np.sum((T2 - T2_bar)**2) / (n - 1)

# sample correlation coefficient
r = np.sum((T1 - T1_bar) * (T2 - T2_bar)) \
    / np.sqrt(np.sum((T1 - T1_bar)**2)
              * np.sum((T2 - T2_bar)**2))
print(f"sample means: {T1_bar:.3f}, {T2_bar:.3f}")
print(f"sample variances: {S2_T1:.4f}, {S2_T2:.4f}")
print(f"sample correlation: {r:.3f}")

fig, ax = plt.subplots()
ax.plot(T1, T2, "o", color=col.emp, ms=2, alpha=0.6)
ax.plot([0, 1], [0, 1], **ref)
ax.set_xlabel("$T_1$ (first arrival)")
ax.set_ylabel("$T_2$ (second arrival)")

plt.show()
