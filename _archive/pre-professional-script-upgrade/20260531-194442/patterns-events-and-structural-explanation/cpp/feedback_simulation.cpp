#include <iostream>
#include <iomanip>

int main() {
    double trust = 62.0;
    double delay = 14.0;
    double pressure = 70.0;

    std::cout << "period,trust,delay,pressure\n";
    for (int period = 1; period <= 12; ++period) {
        delay += (pressure / 100.0) - (trust / 150.0);
        trust -= delay / 30.0;
        pressure += std::max(0.0, (65.0 - trust) / 25.0);

        std::cout << period << ","
                  << std::fixed << std::setprecision(2)
                  << trust << "," << delay << "," << pressure << "\n";
    }

    return 0;
}
