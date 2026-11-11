#!/usr/bin/env python3
"""
Minimal demonstration of calling a compiled C++ program from Python
via subprocess (command-line interface).

This keeps dependencies to zero beyond the standard library.
For tighter integration (in-process calls, shared memory, etc.) consider pybind11
or a C API, but that adds build complexity.
"""

import subprocess
import sys
import os

def call_monte_carlo(num_paths: int, binary: str = "../cpp/build/monte_carlo_call"):
    if not os.path.isfile(binary):
        raise FileNotFoundError(f"C++ binary not found: {binary}. Build it first.")

    result = subprocess.run(
        [binary, str(num_paths)],
        capture_output=True, text=True, check=True
    )
    print("C++ output:")
    print(result.stdout)
    return result.stdout

if __name__ == "__main__":
    paths = int(sys.argv[1]) if len(sys.argv) > 1 else 100_000
    try:
        call_monte_carlo(paths)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
