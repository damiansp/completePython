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

