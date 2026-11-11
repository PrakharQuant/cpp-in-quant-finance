#include <iostream>
#include <random>
#include <cmath>
#include <chrono>
#include <string>
#include <cstdlib>
#include <limits>

// Simple Monte Carlo estimator for a European call option under geometric Brownian motion.
// S_T = S_0 * exp((r - 0.5*sigma^2)*T + sigma*sqrt(T)*Z)
// Price = exp(-r*T) * E[max(S_T - K, 0)]

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <num_paths>\n";
        std::cerr << "Example: " << argv[0] << " 1000000\n";
        return 1;
    }

    long long num_paths;
    try {
        num_paths = std::stoll(argv[1]);
    } catch (const std::exception&) {
        std::cerr << "Error: num_paths must be a valid integer.\n";
        return 1;
    }

    if (num_paths <= 0) {
        std::cerr << "Error: num_paths must be positive.\n";
        return 1;
    }

    // Fixed model parameters (same as Python counterpart)
    const double S0 = 100.0;
    const double K = 100.0;
    const double r = 0.05;
    const double sigma = 0.2;
    const double T = 1.0;
    const unsigned seed = 42;

    std::mt19937 gen(seed);
    std::normal_distribution<double> dist(0.0, 1.0);

    const auto start = std::chrono::high_resolution_clock::now();

    double sum_payoff = 0.0;
    for (long long i = 0; i < num_paths; ++i) {
        const double Z = dist(gen);
        const double ST = S0 * std::exp((r - 0.5 * sigma * sigma) * T + sigma * std::sqrt(T) * Z);
        const double payoff = std::max(ST - K, 0.0);
        sum_payoff += payoff;
    }
    const double estimate = std::exp(-r * T) * (sum_payoff / static_cast<double>(num_paths));

    const auto end = std::chrono::high_resolution_clock::now();
    const std::chrono::duration<double> elapsed = end - start;

    std::cout << "Paths: " << num_paths << "\n";
    std::cout << "Estimate: " << estimate << "\n";
    std::cout << "Elapsed simulation time: " << elapsed.count() << " seconds\n";

    return 0;
}
