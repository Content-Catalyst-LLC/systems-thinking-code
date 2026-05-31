#include <iostream>

int main() {
    double burden = 60.0;
    double capacity = 65.0;
    double institutional_trust = 57.0;

    std::cout << "period,burden,capacity,institutional_trust\n";
    for (int t = 1; t <= 10; ++t) {
        burden += 0.04 * (100.0 - capacity);
        capacity += 0.03 * institutional_trust - 1.5;
        institutional_trust += 0.02 * capacity - 0.03 * burden;
        std::cout << t << "," << burden << "," << capacity << "," << institutional_trust << "\n";
    }
    return 0;
}
