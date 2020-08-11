def get_value_at_time(value, tdelta, rate):
    return value * (1 + rate) ** tdelta


def get_pv_of_annuity(cashflow, rate, timesteps):
    '''
    Get the present value of an annuity with regular <cashflow>s over 
    <timesteps> time steps, given <rate> of interest.
    Assumes first cashflow arrives one time step from today.
    '''
    annuity_factor = (1 - (1 + rate) ** -timesteps) / rate
    return cashflow * annuity_factor


def get_pv_of_growing_annuity(cashflow, rate, timesteps, growth_rate):
    '''
    Get the present value of an annuity where the first cashflow is <cashflow>,
    and each subsequent CF increases my <growth_rate> (expressed as a decimal 
    fraction):
    [0, CF, CF(1 + g), CF(1 + g)^2, ..., CF(1 + g)^(t - 2), CF(1 + g)^(t - 1)]
    '''
    return ((cashflow / (rate - growth_rate))
            * (1 - ((1 + rate) / (1 + growth_rate)) ** -timesteps))


def get_pv_of_perpetuity(cashflow, rate):
    '''
    Get the present value of a perpetuity with payments of <cashflow> and an
    interest <rate>
    '''
    return cashflow / rate


def get_pv_of_growing_perpetuity(cashflow, rate, growth_rate):
    return cashflow / (rate - growth_rate)


if __name__ == '__main__':
    value = 100.
    rate = 0.2
    print('Value 2 years ago:', get_value_at_time(value, -2, rate))
    print('Value 2 years from now:', get_value_at_time(value, 2, rate))

    # How much must you save today to be able to withdraw $100 at the end of
    # each of the next 20 years, given 5% interest?
    rate = 0.05
    cashflow = 100
    ts = 20
    pv = get_pv_of_annuity(cashflow, rate, ts)
    print(f'Must deposit {pv:.2f} today')

    # How much must you save today to be able to withdraw $100 at the end of
    # this year, $102.50 next year, $105.60, ... (2.5% growth rate) for the next
    # 19 years, given 5% returns?
    growth_rate = 0.025
    ts = 20 # pay attention!
    pv = get_pv_of_growing_annuity(cashflow, rate, ts, growth_rate)
    print(f'Must deposit {pv:.2f} today')

    # How much must you save today to be able to withraw $100 at the end of each
    # following year forever?
    pv = get_pv_of_perpetuity(cashflow, rate)
    print(f'Must deposit {pv:.2f} today')

    # How much must you save today to be able to withdraw $100 in a year from
    # now, $102.50 the next year, $105.06 the next, etc, forever and ever given
    # 5% returns?
    pv = get_pv_of_growing_perpetuity(cashflow, rate, growth_rate)
    print(f'Must deposit {pv:.2f} today')
