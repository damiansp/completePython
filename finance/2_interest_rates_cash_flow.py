def apr_to_ear(k, apr=None, i=None):
    '''
    EAR: effective annual rate
    k: periods of componunding (e.g., monthly -> k = 12)
    i: periodic interest rate, AKA periodic discount rate
    '''
    if apr is not None:
        return (1 + (apr / k)) ** k - 1
    return (1 + i) ** k - 1


def get_value_with_compound_interest(principal, rate, periods):
    value = principal
    #for p in range(periods):
    #    value *= (1 + rate) # same as:
    value *= (1 + rate) ** periods
    return value


if __name__ == '__main__':
    # invest $100 in CD with 5% APR with semi-annual compounding.  How much will
    # you have after 1 year?
    principal = 100
    k = 2
    apr = 0.05
    i = apr / k
    print('i =', i)
    value = get_value_with_compound_interest(principal, i, k)
    print(f'Final value: ${value:.2f}')
    
    ear = apr_to_ear(k=k, i=i)
    print('ear =', ear)
    value = get_value_with_compound_interest(principal, ear, 1)
    print(f'Final value: ${value:.2f}')
