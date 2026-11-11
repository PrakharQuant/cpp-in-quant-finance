#!/usr/bin/env python3
"""
Benchmark runner: compares pure-Python loop, NumPy vectorized, and compiled C++
on the same Monte Carlo European call workload.

Run from the python/ directory after building the C++ binary.
"""

import subprocess
import sys
import os
import time

# Import local modules
from monte_carlo_call import monte_carlo_call
try:
    from monte_carlo_call_numpy import monte_carlo_call_numpy
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False

def run_cpp(num_paths: int, binary_path: str):
    try:
        result = subprocess.run(
            [binary_path, str(num_paths)],
            capture_output=True, text=True, check=True, timeout=60
        )
        # Parse simple output
        lines = result.stdout.strip().splitlines()
        est = float(lines[1].split(": ")[1])
        elapsed = float(lines[2].split(": ")[1].split()[0])
        return est, elapsed
    except Exception as e:
        print(f"C++ run failed: {e}")
        return None, None

def main():
    if len(sys.argv) < 2:
        print("Usage: python benchmark.py <num_paths> [cpp_binary_path]")
        print("Default cpp binary: ../cpp/build/monte_carlo_call")
        sys.exit(1)

    num_paths = int(sys.argv[1])
    cpp_bin = sys.argv[2] if len(sys.argv) > 2 else "../cpp/build/monte_carlo_call"

    print(f"Benchmarking Monte Carlo European call with {num_paths:,} paths\n")
    print("Same algorithm and inputs. Exact numbers may differ due to RNG and floating-point.")
    print("This is a toy benchmark on a single core; not representative of production systems.\n")

    # Pure Python
    print("--- Pure Python loop ---")
    est_py, t_py = monte_carlo_call(num_paths)
    print(f"Estimate: {est_py:.6f}  |  Time: {t_py:.4f} s")

    # NumPy
    if HAS_NUMPY:
        print("\n--- NumPy vectorized ---")
        est_np, t_np = monte_carlo_call_numpy(num_paths)
        print(f"Estimate: {est_np:.6f}  |  Time: {t_np:.4f} s")
    else:
        print("\n--- NumPy skipped (not installed) ---")

    # C++
    if os.path.isfile(cpp_bin) and os.access(cpp_bin, os.X_OK):
        print("\n--- Compiled C++ ---")
        est_cpp, t_cpp = run_cpp(num_paths, cpp_bin)
        if est_cpp is not None:
            print(f"Estimate: {est_cpp:.6f}  |  Time: {t_cpp:.4f} s")
    else:
        print(f"\n--- C++ binary not found or not executable at {cpp_bin} ---")
        print("Build it first (see README).")

    print("\nNotes:")
    print("- Compilation time is excluded from the C++ measurement.")
    print("- Results depend on hardware, compiler flags, and Python version.")
    print("- A larger gap usually appears as path count grows or when the loop is more complex.")

if __name__ == "__main__":
    main()
