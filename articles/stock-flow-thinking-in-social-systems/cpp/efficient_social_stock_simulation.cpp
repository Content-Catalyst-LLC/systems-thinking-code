#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    double stock = 42.0;
    double inflow = 3.2;
    double outflow = 2.6;
    std::vector<double> trajectory;
    for (int month = 0; month <= 24; ++month) {
        trajectory.push_back(stock);
        stock = std::clamp(stock + inflow - outflow, 0.0, 100.0);
    }
    std::cout << "final_stock=" << trajectory.back() << "\n";
    return 0;
}
