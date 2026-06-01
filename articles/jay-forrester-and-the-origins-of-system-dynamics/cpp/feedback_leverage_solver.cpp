#include <algorithm>
#include <iostream>

double performance(double backlog, double capacity, double trust, double resistance) {
    return std::max(0.0, std::min(100.0, 100.0 - backlog * 0.35 + capacity * 0.18 + trust * 0.16 - resistance * 0.20));
}

int main() {
    std::cout << "performance_score=" << performance(40.0, 70.0, 66.0, 18.0) << "\n";
    return 0;
}
