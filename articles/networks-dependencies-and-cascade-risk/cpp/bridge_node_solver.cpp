#include <iostream>
#include <vector>
#include <numeric>

int main() {
    std::vector<double> bridge_scores{0.10, 0.35, 0.20, 0.05};
    double total = std::accumulate(bridge_scores.begin(), bridge_scores.end(), 0.0);
    std::cout << "average bridge score=" << total / bridge_scores.size() << "\n";
    return 0;
}
