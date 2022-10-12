`Speedup`:

```
S = T(1) / T(j)
```

T(j): Time to execute a program using j processors


Let:
- `B` fraction of program that is strictly serial
  - `BT(1)`: time to execute serial parts of program
  - `T(1) - BT(1) = T(1)(1 - B)`: time to execute parallelizable parts of program on one processor
  - -> `T(1)(1 - B) / j`: time to execute parallelizable parts with `j` processors
  - -> `BT(1) + T(1)(1 - B) / j`: time to execute whole program with `j` processors.


```
S = T(1) / T(j)
  = T(1) / [BT(1) + T(1)(1 - B)/j]
  = 1 / [B + (1 - B) / j]
```
