# C++ in Quant Finance: From Python Prototype to Fast Pricing Engine

Educational GitHub Pages site explaining where C++ is useful in quantitative finance, how it complements Python, and how the two are commonly used together. Includes small, runnable code examples and a simple benchmark you can run locally.

**No fabricated benchmark numbers** — run the examples on your own machine.

## Quick start

### Prerequisites
- C++ compiler with C++17 support (GCC, Clang, or MSVC)
- CMake 3.14+
- Python 3.8+
- (Optional) NumPy for the vectorized example

### Build the C++ examples

```bash
cd cpp
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release
```

Binaries appear in `cpp/build/` (or `cpp/build/Release/` on some generators).

### Run the Monte Carlo examples

```bash
# C++
./cpp/build/monte_carlo_call 1000000

# Pure Python
python python/monte_carlo_call.py 100000

# Optional NumPy version
python python/monte_carlo_call_numpy.py 1000000

# Order-book teaching example
./cpp/build/order_book
```

### Run the benchmark

```bash
cd python
python benchmark.py 500000
# or point to the binary explicitly
python benchmark.py 500000 ../cpp/build/monte_carlo_call
```

### Call C++ from Python

```bash
cd python
python call_cpp.py 200000
```

## Local preview of the website

The site is pure static HTML/CSS/JS. From the repository root:

```bash
python -m http.server 8000
```

Open http://localhost:8000

## GitHub Pages deployment

A GitHub Actions workflow (`.github/workflows/deploy.yml`) deploys the static site automatically on pushes to `main`.

1. Push this repository to GitHub.
2. Go to Settings → Pages → Build and deployment → Source: **GitHub Actions**.
3. The workflow will publish the site.

## Project structure

```
.
├── index.html          # Main educational page
├── styles.css
├── script.js
├── cpp/
│   ├── CMakeLists.txt
│   ├── monte_carlo_call.cpp
│   └── order_book.cpp
├── python/
│   ├── monte_carlo_call.py
│   ├── monte_carlo_call_numpy.py
│   ├── benchmark.py
│   └── call_cpp.py
├── .github/workflows/deploy.yml
├── README.md
└── LICENSE
```

## What the benchmark does and does not show

It compares equivalent workloads (same model, parameters, and seed where possible) for a European call Monte Carlo estimator:

- pure-Python loop
- NumPy vectorized (if installed)
- compiled C++

It reports wall-clock time of the simulation only. It does **not** claim that C++ is always faster, that a production trading system must be written in C++, or that the observed ratio will hold on your hardware or for more complex models. See the caveats section on the website.

## License

MIT — see [LICENSE](LICENSE).

---

Created by Prakhar Gupta  
[bestofprakhar@gmail.com](mailto:bestofprakhar@gmail.com) · [LinkedIn](https://www.linkedin.com/in/prakhar-gupta-5b7250372) · [X](https://x.com/PrakharQuant) · [GitHub](https://github.com/PrakharQuant)
