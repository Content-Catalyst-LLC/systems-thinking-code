#include <algorithm>
#include <iostream>

int main() {
    for (double delay = 1.0; delay <= 18.0; delay += 1.0) {
        double score = std::clamp(0.68 - 0.035 * delay + 1.2 * 0.08 - 1.4 * 0.05, 0.0, 1.0);
        std::cout << "delay=" << delay << ", resilience=" << score << "\n";
    }
    return 0;
}
