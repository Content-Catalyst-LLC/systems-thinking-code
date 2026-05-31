#include <iostream>
#include <vector>

int main() {
    double stock = 55.0;
    double inflow = 4.0;
    double outflow = 5.0;
    std::vector<double> values;
    for (int t = 0; t < 10; ++t) {
        values.push_back(stock);
        stock += inflow - outflow;
    }
    for (double value : values) {
        std::cout << value << "\n";
    }
    return 0;
}
