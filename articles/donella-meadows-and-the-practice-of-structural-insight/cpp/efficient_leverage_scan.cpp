#include <algorithm>
#include <iostream>
#include <vector>
#include <string>

struct LeveragePoint {
    std::string name;
    int depth;
};

int main() {
    std::vector<LeveragePoint> points = {
        {"parameters", 2},
        {"information_flows", 5},
        {"rules", 7},
        {"self_organization", 8},
        {"goals", 10},
        {"paradigms", 12}
    };

    std::sort(points.begin(), points.end(), [](const LeveragePoint& a, const LeveragePoint& b) {
        return a.depth > b.depth;
    });

    std::cout << "leverage_name,relative_depth\n";
    for (const auto& point : points) {
        std::cout << point.name << "," << point.depth << "\n";
    }
    return 0;
}
