import numpy as np
import hashlib
    
def estimate_probability(event_fn, n_trials=50000):
    results   = [event_fn() for _ in range(n_trials)]
    n_success = sum(results)
    return {
        "probability": n_success / n_trials,
        "n_trials":    n_trials,
        "n_success":   n_success
    }

class BloomFilter:
    def __init__(self, k, m):
        self.k    = k
        self.m    = m
        self.bits = [0] * m
        self.n    = 0

    def _hashes(self, item):
        indices = []
        for i in range(self.k):
            h = hashlib.md5(f"{item}_{i}".encode()).hexdigest()
            indices.append(int(h, 16) % self.m)
        return indices

    def add(self, item):
        for idx in self._hashes(str(item)):
            self.bits[idx] = 1
        self.n += 1

    def contains(self, item):
        return all(self.bits[idx] == 1 for idx in self._hashes(str(item)))

    def theoretical_fpr(self, n=None):
        n = n or self.n
        return (1 - (1 - 1/self.m)**n)**self.k


def mcmc_knapsack(items, capacity, n_iter=100000):
    n = len(items)

    current = [0] * n
    current_weight = 0
    current_value  = 0
    best_value     = 0
    best_state     = current[:]
    accepted       = 0

    for _ in range(n_iter):
        proposal  = current[:]
        flip_idx  = np.random.randint(0, n)
        proposal[flip_idx] = 1 - proposal[flip_idx]

        prop_weight = sum(proposal[i] * items[i]["weight"] for i in range(n))
        prop_value  = sum(proposal[i] * items[i]["value"]  for i in range(n))

        if prop_weight <= capacity:
            if prop_value >= current_value:
                current        = proposal
                current_weight = prop_weight
                current_value  = prop_value
                accepted      += 1
            else:
                ratio = prop_value / max(current_value, 1)
                if np.random.random() < ratio:
                    current        = proposal
                    current_weight = prop_weight
                    current_value  = prop_value
                    accepted      += 1

        if current_value > best_value:
            best_value = current_value
            best_state = current[:]

    best_items = [items[i] for i in range(n) if best_state[i] == 1]

    return {
        "best_value":      best_value,
        "best_items":      best_items,
        "acceptance_rate": accepted / n_iter
    }
