from bayesblend import MleStacking
from cmdstanpy import CmdStanModel


mod = CmdStanModel(stan_file='./bernoulli.stan')
stan_data = {'N': 10, 'y': [0, 1, 0, 0, 0, 0, 0, 0, 0, 1]}
fit1 = mod.sample(chains=4, data=stan_data, seed=1)
fit2 = mod.sample(chains=4, data=stan_data, seed=2)
mle_stacking = MleStacking.from_cmdstanpy({'fit1': fit1, 'fit2': fit2})
mle_stacking.fit()
mle_stacking_blend = mle_stacking.predict()
print(mle_stacking_blend)
