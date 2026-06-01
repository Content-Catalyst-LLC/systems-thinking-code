#include <iostream>
#include <vector>
#include <algorithm>

std::vector<double> simulate_stock(double initial, double inflow, double outflow, int steps) {
    std::vector<double> values;
    values.push_back(initial);

    for (int i = 1; i < steps; ++i) {
        double next = std::max(0.0, values.back() + inflow - outflow);
        values.push_back(next);
    }

    return values;
}

int main() {
    auto values = simulate_stock(50.0, 5.0, 3.5, 20);

    std::cout << "Stock-flow simulation\n";

    for (size_t i = 0; i < values.size(); ++i) {
        std::cout << "time=" << i << ", stock=" << values[i] << "\n";
    }

    return 0;
}
