#include <algorithm>
#include <iostream>

int main() {
    const double critical = 0.50;
    for (double delay = 1.0; delay <= 24.0; delay += 0.5) {
        double score = std::clamp(0.68 - 0.035 * delay + 1.2 * 0.08 - 1.4 * 0.05, 0.0, 1.0);
        if (score < critical) {
            std::cout << "First delay below critical resilience: " << delay << "\n";
            break;
        }
    }
    return 0;
}
