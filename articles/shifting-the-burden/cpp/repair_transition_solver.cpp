#include <iostream>
#include <cmath>

int main() {
    double capacity = 55.0;
    double dependency = 0.80;

    for (int period = 0; period < 10; ++period) {
        double repair = 12.0 + 4.0 * period;
        double relief = std::max(5.0, 35.0 - 3.0 * period);
        capacity = std::max(0.0, capacity + 0.65 * repair - 0.20 * relief);
        dependency = std::max(0.0, dependency + 0.010 * relief - 0.014 * repair);
        std::cout << period << "," << capacity << "," << dependency << "\n";
    }

    return 0;
}
