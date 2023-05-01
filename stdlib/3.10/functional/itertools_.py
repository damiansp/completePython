import itertools as it
import operator


data = [4, 5, 6, 2, 1, 9, 0, 7, 5, 8]
cumprod = list(it.accumulate(data, operator.mul))
print(cumprod)
cummax = list(it.accumulate(data, max))
print(cummax)

# Amortize a 5% loan of 1000 w 4 payments of 90
cashflows = [1000] + 4*[-90]
print(
    list(it.accumulate(cashflows, lambda bal, pmt: round(bal*1.05 + pmt, 2))))

               
