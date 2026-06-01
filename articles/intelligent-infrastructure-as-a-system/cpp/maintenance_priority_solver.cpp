#include <iostream>

double priority(double condition, double consequence, double equity, double redundancy) {
    return 0.30 * (100.0 - condition) + 0.35 * consequence + 0.20 * equity + 0.15 * (100.0 - redundancy);
}

int main() {
    std::cout << "priority_score=" << priority(58.0, 86.0, 82.0, 25.0) << "\n";
    return 0;
}
