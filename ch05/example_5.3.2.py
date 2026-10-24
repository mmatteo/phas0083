# Example 5.3.2 (Figure 5.8): Joint pdf of the Doppler-shifted energy $E$ and the released energy $E'$ estimated from $2000$ draws of the chain of Example 4.2.3, a bivariate normal distribution, with the marginal pdf of each (kernel density estimates)
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from preamble import *  # imports, rng, colours: see preamble.py

import seaborn as sns

E0, sigma0, sigma = 1000, 15, 20   # keV
N = 2000
e = rng.normal(E0, sigma0, N)      # the latent variable
e_rel = rng.normal(e, sigma)       # released, given each e

# the joint pdf as contours, the marginals on the sides
g = sns.jointplot(x=e, y=e_rel, kind="kde", color=col.pdf,
                  marginal_kws={"fill": True})
g.set_axis_labels("Doppler-shifted energy $e$ [keV]",
                  "released energy $e'$ [keV]")

plt.show()
