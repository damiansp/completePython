import matplotlib.pyplot as plt
import numpy as np



TOTAL_WEALTH = 1_000_000
POPULATION = 100
TIME_STEPS = 30
RETURN_DISTRIB = {'name': 't', 'params': {'df': 3}}
WEALTH_DISTRIB = {'name': 'chisq', 'params': {'df': 0.02}}
AMT_INVESTED_DISTRIB = {'name': 'uniform', 'params': {}}
MIN_RETURN = 0.6
MAX_RETURN = 1.8
#{'name': 'exp', 'params': {'scale': 30.}}


def main():
    wealth_distribution = (
        Returns(**WEALTH_DISTRIB).get_returns(POPULATION, normalize=True))
    invested_distribution = Returns(
        **AMT_INVESTED_DISTRIB).get_returns(POPULATION)
    # returns represented as a fraction: e.g., 1.2 = 20% gain, 0.8 = 20% loss
    returns = (
        Returns(**RETURN_DISTRIB)
        .get_returns(
            TIME_STEPS, adj_params={'min': MIN_RETURN, 'max': MAX_RETURN}))
    plot_distributions(wealth, amounts_invested, returns)
    population = Population(wealth_distribution, invested_distribution)
    # track wealth per citizen, and
    # for return in returns:
    #     population.updated_wealth()
    #     track
    # show distribution over time


class Returns:
    def __init__(self, name, params):
        self.name = name
        self.params = params
        self.distrib = {
            'chisq': np.random.chisquare,
            'exp': np.random.exponential,
            't': np.random.standard_t,
            'uniform': np.random.uniform
        }[self.name]

    def get_returns(self, size, adj_params=None, normalize=False):
        raw_distrib = self.distrib(size=size, **self.params)
        if adj_params is not None:
            raw_distrib = self._adjust(raw_distrib, adj_params)
        if normalize:
            return raw_distrib / raw_distrib.sum()
        return raw_distrib

    def _adjust(self, x, params):
        x = self._rescale(x, params)
        return x
    
    @staticmethod
    def _rescale(x, params):
        rng = params['max'] - params['min']
        x -= x.min()
        x /= x.max()
        x *= rng
        x += params['min']
        return x        


class Citizen:
    def __init__(self, wealth, fraction_invested):
        self.wealth = wealth
        self.fraction_invested = fraction_invested

   # def update_wealth(self, returns):
   #     self.wealth *= returns

    def get_wealth_as_fraction_of_population(self, total_wealth):
        return self.wealth / total_wealth


class Population:
    def __init__(self, wealth_distribution, invested_distribution):
        wealth_per_citizen = TOTAL_WEALTH * wealth
        population = [
            Citizen(amt, fraction_invested)
            for amt, fraction_invested in zip(
                    wealth_per_citizen, invested_distribution)]

    def update_wealth(self, returns):
        pass
        

def plot_distributions(wealth, amounts_invested, returns):
    plt.subplot(311)
    plt.hist(wealth)
    plt.xlabel('Wealth')
    plt.subplot(312)
    plt.hist(amounts_invested)
    plt.xlabel('Fractions invested')
    plt.subplot(313)
    plt.hist(returns)
    plt.xlabel('Returns')
    plt.show()


if __name__ == '__main__':
    main()
