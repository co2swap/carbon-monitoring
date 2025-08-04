from simulate import simulate_state
from utility import compute_utility

actions = ['switch_to_renewables', 'optimize_process', 'buy_offsets', 
           'delay_non_critical', 'invest_in_capture']

def get_best_action(current_state, weights):
    best_action = None
    best_utility = float('-inf')
    for action in actions:
        new_state = simulate_state(action, current_state)
        util = compute_utility(new_state, weights)
        if util > best_utility:
            best_utility = util
            best_action = action
    return best_action, best_utility
