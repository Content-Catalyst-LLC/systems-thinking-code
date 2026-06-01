#include <algorithm>
#include <iostream>
#include <vector>
#include <string>

struct Scenario {
    std::string name;
    double feedback;
    double inquiry;
    double memory;
    double defensiveness;
};

double learning_capacity(const Scenario& s) {
    return std::max(0.0, std::min(100.0, 0.30 * s.feedback + 0.25 * s.inquiry + 0.25 * s.memory - 0.20 * s.defensiveness));
}

int main() {
    std::vector<Scenario> scenarios = {
        {"compliance", 42, 30, 44, 58},
        {"adaptive", 66, 58, 60, 34},
        {"learning_pathway", 78, 76, 70, 22}
    };

    std::cout << "scenario,learning_capacity\n";
    for (const auto& scenario : scenarios) {
        std::cout << scenario.name << "," << learning_capacity(scenario) << "\n";
    }
    return 0;
}
