#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <iomanip>

// Teaching example: aggregate order quantities by price and find best bid/ask.
// NOT a production exchange matching engine or low-latency gateway.

struct Order {
    double price;
    int quantity;  // positive = buy (bid), negative = sell (ask), or use side flag
    char side;     // 'B' or 'S'
};

int main() {
    // Small hardcoded set of orders for demonstration
    std::vector<Order> orders = {
        {100.50, 100, 'B'},
        {100.50, 50, 'B'},
        {100.25, 200, 'B'},
        {100.75, 80, 'S'},
        {100.75, 120, 'S'},
        {101.00, 300, 'S'},
        {100.00, 150, 'B'}
    };

    // Aggregate quantity by price and side
    std::map<double, int> bids;  // price -> total qty
    std::map<double, int> asks;

    for (const auto& o : orders) {
        if (o.side == 'B') {
            bids[o.price] += o.quantity;
        } else if (o.side == 'S') {
            asks[o.price] += o.quantity;
        }
    }

    // Best bid = highest price with quantity > 0
    double best_bid = 0.0;
    int best_bid_qty = 0;
    for (auto it = bids.rbegin(); it != bids.rend(); ++it) {
        if (it->second > 0) {
            best_bid = it->first;
            best_bid_qty = it->second;
            break;
        }
    }

    // Best ask = lowest price with quantity > 0
    double best_ask = 0.0;
    int best_ask_qty = 0;
    for (const auto& [price, qty] : asks) {
        if (qty > 0) {
            best_ask = price;
            best_ask_qty = qty;
            break;
        }
    }

    std::cout << std::fixed << std::setprecision(2);
    std::cout << "Aggregated Bids:\n";
    for (auto it = bids.rbegin(); it != bids.rend(); ++it) {
        std::cout << "  " << it->first << " : " << it->second << "\n";
    }
    std::cout << "Aggregated Asks:\n";
    for (const auto& [price, qty] : asks) {
        std::cout << "  " << price << " : " << qty << "\n";
    }
    std::cout << "Best Bid: " << best_bid << " (" << best_bid_qty << ")\n";
    std::cout << "Best Ask: " << best_ask << " (" << best_ask_qty << ")\n";
    if (best_bid > 0 && best_ask > 0) {
        std::cout << "Spread: " << (best_ask - best_bid) << "\n";
    }

    return 0;
}
