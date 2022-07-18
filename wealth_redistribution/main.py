import matplotlib.pyplot as plt
import numpy as np



TOTAL_WEALTH = 1_000_000
POPULATION = 100
TIME_STEPS = 30
RETURN_DISTRIB = {'name': 't', 'params': {'df': 3}}
WEALTH_DISTRIB = {'name': 'chisq', 'params': {'df': 0.02}}
#{'name': 'exp', 'params': {'scale': 30.}}


def main():
    wealth = Returns(**WEALTH_DISTRIB).get_returns(TIME_STEPS)
    returns = Returns(**RETURN_DISTRIB).get_returns(TIME_STEPS)
    plot_distributions(wealth, returns)
    # TODO:
    # create citizen class
    # create population with different investing params
    # distribute initial wealth
    # Run sim


class Returns:
    def __init__(self, name, params):
        self.params = params
        self.distrib = {
            'chisq': np.random.chisquare,
            'exp': np.random.exponential,
            't': np.random.standard_t
        }[name]

    def get_returns(self, size):
        return self.distrib(size=size, **self.params)


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
