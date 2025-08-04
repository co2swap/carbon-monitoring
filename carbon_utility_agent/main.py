from actions import get_best_action
from config.emission_weights import weights
from simulate import simulate_state

# Current dummy state (example)
state = {'emissions': 100, 'cost': 50, 'compliance': 5, 'renewable': 10}

# Evaluate best action
action, utility = get_best_action(state, weights)
print(f"Best Action: {action} with Utility: {utility}")
