def compute_utility(state, weights):
    return (-weights['emissions'] * state['emissions']
            -weights['cost'] * state['cost']
            +weights['compliance'] * state['compliance']
            +weights['renewable'] * state['renewable'])
