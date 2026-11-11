#!/usr/bin/env python3
"""
Equivalent pure-Python Monte Carlo estimator for a European call option.
Uses the same model, parameters, and fixed seed as the C++ version.

Note: exact numeric matches are not guaranteed across languages or RNG implementations.
"""

import random
import math
import time
import sys

def monte_carlo_call(num_paths: int, S0=100.0, K=100.0, r=0.05, sigma=0.2, T=1.0, seed=42):
    if num_paths <= 0:
        raise ValueError("num_paths must be positive")

    random.seed(seed)
    # Pure Python normal via Box-Muller or just use random.gauss (uses same seed)
    sum_payoff = 0.0
    start = time.perf_counter()

    for _ in range(num_paths):
        Z = random.gauss(0.0, 1.0)
        ST = S0 * math.exp((r - 0.5 * sigma * sigma) * T + sigma * math.sqrt(T) * Z)
        payoff = max(ST - K, 0.0)
        sum_payoff += payoff

    estimate = math.exp(-r * T) * (sum_payoff / num_paths)
    elapsed = time.perf_counter() - start
    return estimate, elapsed

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <num_paths>")
        print(f"Example: {sys.argv[0]} 100000")
        sys.exit(1)

    try:
        num_paths = int(sys.argv[1])
    except ValueError:
        print("Error: num_paths must be an integer")
        sys.exit(1)

    try:
        est, elapsed = monte_carlo_call(num_paths)
        print(f"Paths: {num_paths}")
        print(f"Estimate: {est}")
        print(f"Elapsed simulation time: {elapsed:.6f} seconds")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
