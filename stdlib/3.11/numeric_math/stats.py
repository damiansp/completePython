from decimal import Decimal as D
from fractions import Fraction as F
from itertools import filterfalse
from math import isnan
import statistics as st


data = [20.7, float('NaN'), 19.2, 18.3, float('NaN'), 14.4]
print(sorted(data))  # !!
print(st.median(data))  # !!

print(sum(map(isnan, data)))
clean = list(filterfalse(isnan, data))
print(clean)
print(sorted(clean))
print(st.median(clean))

print(st.mean([1, 2, 3, 4, 4]))
print(st.mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)]))
print(st.mean([D('0.5'), D('0.75'), D('0.625'), D('0.375')]))

print(st.fmean([3.5, 4., 5.25]))  # faster mean
grades = [85, 92, 83, 91]
weights = [0.2, 0.2, 0.3, 0.3]
#print(st.fmean(grades, weights))  # 3.11+

print(round(st.geometric_mean([54, 24, 36])))
#print(round(st.harmonic_mean([40, 60], weights=[5, 30)))  # 3.11+

print(st.median([1, 3, 5]))
print(st.median([1, 3, 5, 7]))
print(st.median_low([1, 3, 5, 7]))  # 3
print(st.median_high([1, 3, 5, 7]))  # 5

print(st.mode([1, 1, 2, 3, 3, 3, 3, 4]))
print(st.mode('rbbrgrr'))

print(st.multimode('aabbbbbccddddeefffffgg'))

print(st.pstdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]))

data = [0., 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25]
print(st.pvariance(data))

mu = st.mean(data)
print(st.pvariance(data, mu))

print(st.stdev(data))
print(st.stdev(data, xbar=mu))

print(st.variance(data))
print(st.variance(data, xbar=mu))

data = [
    105, 129, 87, 86, 111, 111, 89, 81, 108, 92, 110, 100, 75, 105, 103, 109,
    76, 119, 99, 91, 103, 129, 106, 101, 84, 111, 74, 87, 86, 103, 103, 106,
    86, 111, 75, 87, 102, 121, 111, 88, 89, 101, 106, 95, 103, 107, 101, 81,
    109, 104]
print([round(q, 1) for q in st.quantiles(data, n=10)])


x = range(1, 10)
y = [1, 2, 3] * 3
print(st.covariance(x, y))
z = range(9, 0, -1)
print(st.covariance(x, z))

print(st.correlation(x, x))
print(st.correlation(x, y))

year = [1971, 1975, 1979, 1982, 1983]
films_cum = [1, 2, 3, 4, 5]
slope, intercept = st.linear_regression(year, films_cum)
preds_2023 = round(intercept + slope*2023)
print(preds_2023)


normd = st.NormalDist(mu=35, sigma=7)
print(normd.mean)
print(normd.median)
print(normd.mode)
print(normd.stdev)
print(normd.variance)


norm_sample = st.NormalDist.from_samples(data)
print(norm_sample.mean)
print(norm_sample.median)
print(norm_sample.mode)
print(norm_sample.stdev)
print(norm_sample.variance)
print(norm_sample.samples(5, seed=1234))
print(norm_sample.pdf(130))      # prob(130 | norm_sample)
print(1 - norm_sample.cdf(130))  # prob(>=130 | norm_sample)

print(normd.overlap(norm_sample))

print(normd.quantiles(n=4))

print(normd.zscore(45))


