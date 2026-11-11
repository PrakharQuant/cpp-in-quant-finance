#!/usr/bin/env python3
"""
Optional NumPy vectorized version of the same Monte Carlo call estimator.
Clearly distinguished from the pure-Python loop version.
Requires: numpy
"""

import numpy as np
import math
import time
import sys

def monte_carlo_call_numpy(num_paths: int, S0=100.0, K=100.0, r=0.05, sigma=0.2, T=1.0, seed=42):
    if num_paths <= 0:
        raise ValueError("num_paths must be positive")

    rng = np.random.default_rng(seed)
    start = time.perf_counter()

    Z = rng.standard_normal(num_paths)
    ST = S0 * np.exp((r - 0.5 * sigma * sigma) * T + sigma * np.sqrt(T) * Z)
    payoff = np.maximum(ST - K, 0.0)
    estimate = math.exp(-r * T) * np.mean(payoff)

    elapsed = time.perf_counter() - start
    return float(estimate), elapsed

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <num_paths>")
        sys.exit(1)
    try:
        num_paths = int(sys.argv[1])
        est, elapsed = monte_carlo_call_numpy(num_paths)
        print(f"Paths: {num_paths}")
        print(f"Estimate (NumPy): {est}")
        print(f"Elapsed simulation time: {elapsed:.6f} seconds")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
