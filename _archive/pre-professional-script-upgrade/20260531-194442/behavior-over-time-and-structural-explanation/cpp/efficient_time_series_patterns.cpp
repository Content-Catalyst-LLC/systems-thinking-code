// Efficient time-series pattern scaffold in C++.
#include <iostream>
#include <vector>
#include <numeric>

int main() {
    std::vector<double> values {20, 25, 33, 45, 61, 83, 102};
    double change = values.back() - values.front();
    std::cout << "First value: " << values.front() << "\n";
    std::cout << "Last value: " << values.back() << "\n";
    std::cout << "Change: " << change << "\n";
    std::cout << "Pattern: " << (change > 0 ? "increasing" : change < 0 ? "decreasing" : "flat") << "\n";
    return 0;
}
