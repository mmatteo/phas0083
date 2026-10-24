# Example 4.1.1 (Figure 4.3): Q-Q plots of the draws from $f(x)=2x$ by the probability integral transformation (top) and the accept/reject algorithm (bottom), from $N=200$ uniform random numbers and $N=200$ candidates
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

N = 200

# probability integral transformation, x = F^-1(u) = sqrt(u)
u = rng.uniform(0, 1, N)
x_pit = np.sqrt(u)

# accept/reject with the envelope g(x) = 2 on [0, 1]
x_cand = rng.uniform(0, 1, N)
v_cand = rng.uniform(0, 2, N)
x_acc = x_cand[v_cand <= 2 * x_cand]
print(f"accepted {x_acc.size} of {N} candidates"
      f" ({x_acc.size / N:.2f}, expected 0.5)")

# Q-Q plot: the ordered draws against F^{-1}((i - 1/2)/N)
q_pit, q_acc = np.sort(x_pit), np.sort(x_acc)

fig, axes = plt.subplots(2, 1, sharex=True)
for ax, q, title in zip(axes, [q_pit, q_acc],
                        ["probability integral transf.",
                         "accept/reject"]):
    n = q.size
    p = (np.arange(1, n + 1) - 0.5) / n
    ax.plot([0, 1], [0, 1], **ref)
    ax.plot(np.sqrt(p), q, "o", color=col.emp, ms=2)
    ax.set_title(f"{title}, {n} draws")
    ax.set_ylabel("quantile of the draws")
axes[-1].set_xlabel("quantile of $F$")

plt.show()
