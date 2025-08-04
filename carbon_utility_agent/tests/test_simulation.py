from simulate import simulate_state

def test_simulate_state():
    state = {'emissions': 100, 'cost': 50, 'compliance': 5, 'renewable': 10}
    new_state = simulate_state('switch_to_renewables', state)
    assert new_state['emissions'] < state['emissions']
