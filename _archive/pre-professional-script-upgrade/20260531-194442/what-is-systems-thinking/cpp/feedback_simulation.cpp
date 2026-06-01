#include <iostream>
#include <iomanip>

int main() {
    double reinforcing = 10.0;
    double balancing = 80.0;
    double target = 50.0;

    std::cout << "period,reinforcing,balancing\n";
    for (int period = 1; period <= 20; ++period) {
        reinforcing += 0.12 * reinforcing;
        balancing += 0.20 * (target - balancing);
        std::cout << period << "," << std::fixed << std::setprecision(2)
                  << reinforcing << "," << balancing << "\n";
    }

    return 0;
}
