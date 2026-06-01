#include <algorithm>
#include <iostream>

double momentum(double adoption, double trust, double institutional_response, double learning, double resistance) {
    return std::max(0.0, std::min(100.0, 0.30 * adoption + 0.22 * trust + 0.20 * institutional_response + 0.18 * learning - 0.20 * resistance));
}

int main() {
    std::cout << "momentum_score=" << momentum(70.0, 65.0, 60.0, 72.0, 32.0) << "\n";
    return 0;
}
