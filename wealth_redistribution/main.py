import matplotlib.pyplot as plt
import numpy as np



TOTAL_WEALTH = 1_000_000
POPULATION = 100
TIME_STEPS = 30
RETURN_DISTRIB = {'name': 't', 'params': {'df': 3}}
WEALTH_DISTRIB = {'name': 'chisq', 'params': {'df': 0.02}}
MIN_RETURN = 0.6
MAX_RETURN = 1.8
#{'name': 'exp', 'params': {'scale': 30.}}


def main():
    wealth = Returns(**WEALTH_DISTRIB).get_returns(TIME_STEPS)
    # returns represented as a fraction: e.g., 1.2 = 20% gain, 0.8 = 20% loss
    returns = (
        Returns(**RETURN_DISTRIB)
        .get_returns(
            TIME_STEPS, adj_params={'min': MIN_RETURN, 'max': MAX_RETURN}))
    plot_distributions(wealth, returns)
    # TODO:
    # create citizen class
    # create population with different investing params
    # distribute initial wealth
    # Run sim


class Returns:
    def __init__(self, name, params):
        self.name = name
        self.params = params
        self.distrib = {
            'chisq': np.random.chisquare,
            'exp': np.random.exponential,
            't': np.random.standard_t
        }[self.name]

    def get_returns(self, size, adj_params=None):
        raw_distrib = self.distrib(size=size, **self.params)
        if adj_params is None:
            return raw_distrib
        return self._adjust(raw_distrib, adj_params)


    def _adjust(self, x, params):
        x = self._rescale(x, params)
        #mean_diff = params['mean'] - t.mean()
        #t += mean_diff
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

    def update_wealth(self, returns):
        self.wealth *= returns

    def get_wealth_as_fraction_of_population(self, total_wealth):
        return self.wealth / total_wealth

    
        

def plot_distributions(wealth, returns):
    plt.subplot(211)
    plt.hist(wealth)
    plt.xlabel('Wealth')
    plt.subplot(212)
    plt.hist(returns)
    plt.xlabel('Returns')
    plt.show()


if __name__ == '__main__':
    main()
