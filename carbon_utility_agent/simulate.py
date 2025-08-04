def simulate_state(action, state):
    # Simulated effects of actions (placeholder logic)
    if action == 'switch_to_renewables':
        return {'emissions': state['emissions'] - 20, 'cost': state['cost'] + 10, 'compliance': state['compliance'] + 5, 'renewable': state['renewable'] + 30}
    elif action == 'optimize_process':
        return {'emissions': state['emissions'] - 10, 'cost': state['cost'] + 5, 'compliance': state['compliance'] + 2, 'renewable': state['renewable']}
    elif action == 'buy_offsets':
        return {'emissions': state['emissions'] - 15, 'cost': state['cost'] + 20, 'compliance': state['compliance'] + 8, 'renewable': state['renewable']}
    elif action == 'invest_in_capture':
        return {'emissions': state['emissions'] - 30, 'cost': state['cost'] + 30, 'compliance': state['compliance'] + 10, 'renewable': state['renewable']}
    elif action == 'delay_non_critical':
        return {'emissions': state['emissions'] - 5, 'cost': state['cost'] - 2, 'compliance': state['compliance'] - 1, 'renewable': state['renewable']}
    return state
