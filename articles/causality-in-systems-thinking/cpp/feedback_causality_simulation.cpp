#include <iostream>
#include <iomanip>

int main() {
    double trust = 64.0;
    double capacity = 58.0;
    double demand = 70.0;

    std::cout << "period,trust,capacity,demand,delay\n";
    for (int period = 1; period <= 20; ++period) {
        double delay = (demand / capacity) * 10.0;
        trust += capacity / 140.0 - delay / 18.0;
        capacity += trust / 120.0 - demand / 180.0;
        demand += (65.0 - trust > 0 ? 65.0 - trust : 0.0) * 0.05;
        std::cout << period << "," << std::fixed << std::setprecision(2)
                  << trust << "," << capacity << "," << demand << "," << delay << "\n";
    }

    return 0;
}
