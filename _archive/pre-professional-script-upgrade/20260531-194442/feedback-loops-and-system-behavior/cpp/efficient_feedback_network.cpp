#include <iostream>
#include <string>
#include <vector>

struct Edge {
    std::string source;
    std::string target;
    int polarity; // +1 for positive, -1 for negative
};

int main() {
    std::vector<Edge> edges = {
        {"public_trust", "cooperation", 1},
        {"cooperation", "service_quality", 1},
        {"service_quality", "public_trust", 1}
    };

    int product = 1;
    for (const auto& edge : edges) {
        product *= edge.polarity;
    }

    std::cout << "loop_type," << (product > 0 ? "reinforcing" : "balancing") << "\n";
    return 0;
}
