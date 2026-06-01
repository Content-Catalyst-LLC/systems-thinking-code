#include <algorithm>
#include <iostream>

double resilience(double buffer_depth, double self_organization, double trust, double regeneration) {
    return std::max(0.0, std::min(100.0, 0.30 * buffer_depth + 0.25 * self_organization + 0.20 * trust + 0.25 * regeneration));
}

int main() {
    std::cout << "resilience_score=" << resilience(72.0, 78.0, 66.0, 70.0) << "\n";
    return 0;
}
