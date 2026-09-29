# PHAS0083, Statistical Analysis of Data: the scripts

The Python scripts printed in the lecture notes of PHAS0083 (University
College London, Matteo Agostini), one file per figure, grouped by chapter.
Each file is the script as printed, preceded by the preamble that every
script of the notes assumes (`preamble.py`: the imports, the random number
generator with its seed, the colours), so that it runs on its own:

```
pip install -r requirements.txt
python bootstrap/edf-quantiles-margin.py
```

The seed is fixed, so a script produces the numbers quoted in the notes;
change it to see how the results vary from one simulation to the next.
Sizes, fonts and styles of the plots differ from the notes, which draw them
with their own settings.

The scripts are generated from the source of the notes; do not edit them
here.

## Scripts by chapter

## Chapter 2: Probability Theory

- [`probability/pdf_cdf-margin.py`](probability/pdf_cdf-margin.py): Pdf and cdf of the standard normal distribution
- [`probability/pmf_cdf-margin.py`](probability/pmf_cdf-margin.py): Pmf and cdf of the score of a fair die

## Chapter 3: Common Families of Distributions

- [`families/binomial1-margin.py`](families/binomial1-margin.py): Pmf and cdf of the binomial distribution with n=10, p=0.3
- [`families/binomial2-margin.py`](families/binomial2-margin.py): Binomial pmf for n=5,10,20 at p=0.5 (top) and for p=0.1,0.2,0.6 at n=20 (bottom)
- [`families/binomial3-margin.py`](families/binomial3-margin.py): Pmf and cdf of the number of detected gamma-rays, binomial with n=20, p=0.1
- [`families/norm1-margin.py`](families/norm1-margin.py): Pdf and cdf of the normal distribution N(0, 1)
- [`families/norm2-margin.py`](families/norm2-margin.py): Cdf of the detector response X~N(100, 25), with the probabilities read at 10010
- [`families/norm3-margin.py`](families/norm3-margin.py): Binomial pmf with p=0.3 for increasing n, and the normal approximation for n=100
- [`families/norm4-margin.py`](families/norm4-margin.py): Poisson pmf for increasing ν, and the normal approximation for ν=40
- [`families/poisson1-margin.py`](families/poisson1-margin.py): Pmf and cdf of the Poisson distribution with ν=3
- [`families/poisson2-margin.py`](families/poisson2-margin.py): Poisson pmf for ν=0.7,3,10 (top); binomial pmf with p=3/N approaching the Poisson with ν=3 (bottom)
- [`families/poisson3-margin.py`](families/poisson3-margin.py): Cdf of the Poisson distribution with ν=10
- [`families/poisson4-margin.py`](families/poisson4-margin.py): Observed numbers of 10-s intervals with a given number of IMB events, and the Poisson expectation with ν=0.77

## Chapter 4: Data Generation and Samplers

- [`data_generation/edf-convergence-margin.py`](data_generation/edf-convergence-margin.py): EDF of N draws from N(0,1) and the true cdf, for N=20, 200, 2000 (top to bottom)
- [`data_generation/edf-quantiles-margin.py`](data_generation/edf-quantiles-margin.py): EDF of N=500 draws from N(0,1), with its 0.025, 0.5 and 0.975 quantiles and the true ones
- [`data_generation/point-source-kde-margin.py`](data_generation/point-source-kde-margin.py): Distance of simulated photons from a point source: histogram, KDE and the true Rayleigh pdf
- [`data_generation/precision-margin.py`](data_generation/precision-margin.py): Error of the estimated P(-1<X<1) against N in four runs, and the predicted binomial precision
- [`data_generation/qqplot-margin.py`](data_generation/qqplot-margin.py): Q-Q plots of N=10 (top) and N=100 (bottom) draws from N(0,1) against the normal quantiles
- [`data_generation/sampling-margin.py`](data_generation/sampling-margin.py): Draws from f(x)=2x by inverse-transform (top) and rejection (bottom) sampling, with the pdf

## Chapter 5: Multivariate Models

- [`multivariate/product-margin.py`](multivariate/product-margin.py): Simulated P=VI with small (top) and large (bottom) relative uncertainties, and normal pdfs with the exact and delta-method variances
- [`multivariate/ratio-instability-margin.py`](multivariate/ratio-instability-margin.py): Running variance of R=X/Y for N up to 2×10^6 draws, and the delta-method value
- [`multivariate/resampling-margin.py`](multivariate/resampling-margin.py): Simulated distribution of the velocity V=D/T
- [`multivariate/velocity-methods-margin.py`](multivariate/velocity-methods-margin.py): Simulated velocity V=D/T and the normal pdf predicted by the delta method

## Chapter 6: Random Samples

- [`random_samples/clt-uniform-sim-margin.py`](random_samples/clt-uniform-sim-margin.py): Means of samples of size n=1,2,5,30 from U(0,1) (top to bottom), and the normal pdf of the central limit theorem
- [`random_samples/convergence-margin.py`](random_samples/convergence-margin.py): Sample mean, variance and correlation of the arrival times on the first m observations, with the population values
- [`random_samples/correlation-margin.py`](random_samples/correlation-margin.py): Earliest and latest photon arrival times in a sample of 1000, with their sample correlation
- [`random_samples/sequence-margin.py`](random_samples/sequence-margin.py): Running sample mean of three samples from an exponential distribution with β=1/2

## Chapter 7: Point Estimation

- [`point_estimation/likelihood1-margin.py`](point_estimation/likelihood1-margin.py): Pmfs of the Poisson models with ν=3.0 and ν=5.5
- [`point_estimation/likelihood2-margin.py`](point_estimation/likelihood2-margin.py): Probability of observing x=3 as a function of ν, with its maximum
- [`point_estimation/likelihood3-margin.py`](point_estimation/likelihood3-margin.py): Likelihood of (μ,σ^2) for the sample x of a normal population
- [`point_estimation/likelihood4-margin.py`](point_estimation/likelihood4-margin.py): Negative log-likelihood of (μ,σ^2) and the path of the optimiser to its minimum

## Chapter 8: The Bootstrap

- [`bootstrap/edf-margin.py`](bootstrap/edf-margin.py): EDF of the decay times and cdf of the fitted exponential model
- [`bootstrap/hist-B-margin.py`](bootstrap/hist-B-margin.py): Histograms of the bootstrap replicates t^*_i of the sample mean, for B=99 (top) and B=999 (bottom)
- [`bootstrap/moments-margin.py`](bootstrap/moments-margin.py): Bootstrap estimates of the bias (top) and variance (bottom) of the mean against B, in four runs
- [`bootstrap/nonparam-margin.py`](bootstrap/nonparam-margin.py): Nonparametric bootstrap replicates of the sample mean
- [`bootstrap/quantiles-B-margin.py`](bootstrap/quantiles-B-margin.py): Estimated 0.05 and 0.95 quantiles of t^*-t against B

## Chapter 9: Hypothesis Testing

- [`hypothesis_testing/lrt-bootstrap-margin.py`](hypothesis_testing/lrt-bootstrap-margin.py): Bootstrap distribution of the likelihood-ratio statistic under H_0 (top) and its survival function (bottom), with the level-0.05 threshold
- [`hypothesis_testing/lrt-bootstrap2-margin.py`](hypothesis_testing/lrt-bootstrap2-margin.py): Power of the level-0.05 likelihood-ratio test as a function of the signal λ
- [`hypothesis_testing/lrt1-margin.py`](hypothesis_testing/lrt1-margin.py): Likelihood of θ for the sample x with σ=1, at θ_0=1 and at the MLE θ
- [`hypothesis_testing/lrt2-margin.py`](hypothesis_testing/lrt2-margin.py): Likelihood of μ with σ^2 at its restricted and unrestricted MLEs, and the resulting likelihood ratio
- [`hypothesis_testing/lrt3-margin.py`](hypothesis_testing/lrt3-margin.py): Negative log-likelihood of (μ,σ^2) with the optimiser paths to the unrestricted and restricted (μ1) minima
- [`hypothesis_testing/power-margin.py`](hypothesis_testing/power-margin.py): Power functions of the two tests of H_0:θ≤1/2 based on five Bernoulli trials

## Chapter 10: Interval Estimation

- [`interval_estimation/coverage-margin.py`](interval_estimation/coverage-margin.py): Thirty 90% confidence intervals for μ from repeated samples of size 10: those that miss μ (dashed line) are in red
- [`interval_estimation/interval-boostrap-margin.py`](interval_estimation/interval-boostrap-margin.py): Test statistic of the observation x_obs=1050 and the bootstrap level-0.10 threshold as functions of λ_0; the shaded region is the confidence interval
- [`interval_estimation/interval-boostrap1-margin.py`](interval_estimation/interval-boostrap1-margin.py): Test statistic of four observations and the bootstrap level-0.10 threshold as functions of λ_0

## Chapter 11: Asymptotic Evaluations

- [`asymptotic_evaluations/chi-square-fit-margin.py`](asymptotic_evaluations/chi-square-fit-margin.py): Sample of 60 values from the peak-over-background model, with μ and its 90% confidence interval
- [`asymptotic_evaluations/wilks1-margin.py`](asymptotic_evaluations/wilks1-margin.py): Bootstrap distribution of the test statistic under H_0, the chi-squared prediction and the level-0.05 threshold
- [`asymptotic_evaluations/wilks3-margin.py`](asymptotic_evaluations/wilks3-margin.py): Test statistic of x_obs=2050 against λ_0, with the bootstrap and chi-squared level-0.05 thresholds
- [`asymptotic_evaluations/wilks5-margin.py`](asymptotic_evaluations/wilks5-margin.py): Test statistic of the sample x over (μ,σ^2), with the 68%, 95% and 99% confidence regions from Wilks' theorem

## Chapter 12: p-values and Goodness of Fit

- [`pvalues_goodness_of_fit/chi2-margin.py`](pvalues_goodness_of_fit/chi2-margin.py): Observed counts of a uniform sample of 40 in seven bins, and the counts expected under N(0,1)
- [`pvalues_goodness_of_fit/k-s-margin.py`](pvalues_goodness_of_fit/k-s-margin.py): Empirical cdf of a uniform sample of 20 and the cdf of the normal model tested by Kolmogorov--Smirnov
- [`pvalues_goodness_of_fit/pvalue-distribution-margin.py`](pvalues_goodness_of_fit/pvalue-distribution-margin.py): Distribution of the p-value of a test of μ=0 over 10000 samples: uniform under H_0 (top), piled up near zero under H_1 (bottom)
- [`pvalues_goodness_of_fit/wilks1-obs3-margin.py`](pvalues_goodness_of_fit/wilks1-obs3-margin.py): Survival function of the test statistic under H_0, with the threshold for α=5% and the observed value
- [`pvalues_goodness_of_fit/wilks1-obs4-margin.py`](pvalues_goodness_of_fit/wilks1-obs4-margin.py): Probability of more than x counts under H_0:ν=2000, and the observed count

## Chapter 13: Bayesian Inference

- [`bayesian_inference/normal-coniugate-margin.py`](bayesian_inference/normal-coniugate-margin.py): Prior N(0,1), likelihood of the observation y=2 with σ=1, and posterior of θ
- [`bayesian_inference/normal-coniugate2-margin.py`](bayesian_inference/normal-coniugate2-margin.py): Four sequential updates of a normal prior (top to bottom), each posterior becoming the next prior
