#include <iostream>
#include <iomanip>

int main() {
    double x = 10.0;
    double rate = 0.10;

    std::cout << "period,value\n";
    for (int period = 1; period <= 20; ++period) {
        x = x * (1.0 + rate);
        std::cout << period << "," << std::fixed << std::setprecision(2) << x << "\n";
    }
    return 0;
}
