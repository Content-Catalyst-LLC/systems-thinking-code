// Efficient objective scan scaffold.
// Compile with: g++ efficient_objective_scan.cpp -std=c++17 -O2 -o objective_scan

#include <iostream>
#include <vector>
#include <string>

struct Scenario {
    std::string name;
    double throughput;
    double access;
    double dignity;
    double burden;
};

double score(const Scenario& s, double access_weight) {
    double throughput_weight = 1.0 - access_weight;
    return throughput_weight * s.throughput + access_weight * s.access + 0.4 * s.dignity - 0.4 * s.burden;
}

int main() {
    std::vector<Scenario> scenarios = {
        {"throughput", 0.90, 0.45, 0.30, 0.80},
        {"dignity", 0.72, 0.78, 0.82, 0.30},
        {"stewardship", 0.68, 0.70, 0.74, 0.35}
    };

    for (double w : {0.0, 0.25, 0.5, 0.75, 1.0}) {
        std::cout << "access weight " << w << "\n";
        for (const auto& s : scenarios) {
            std::cout << "  " << s.name << ": " << score(s, w) << "\n";
        }
    }
}
