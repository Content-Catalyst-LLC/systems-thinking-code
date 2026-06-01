#include <algorithm>
#include <iostream>
#include <vector>
#include <string>

struct Scenario {
    std::string name;
    double interdependence;
    double feedback;
    double delay;
    double adaptation;
    double uncertainty;
};

double complexity_pressure(const Scenario& s) {
    double base = 22.0 * s.interdependence + 22.0 * s.feedback + 18.0 * s.delay + 16.0 * s.adaptation + 22.0 * s.uncertainty;
    double nonlinear_boost = 12.0 * s.interdependence * s.feedback * s.delay;
    return std::max(0.0, std::min(120.0, base + nonlinear_boost));
}

int main() {
    std::vector<Scenario> scenarios = {
        {"fragmented_reaction", 0.82, 0.76, 0.74, 0.34, 0.80},
        {"adaptive_learning", 0.70, 0.62, 0.52, 0.66, 0.60},
        {"accountable_transformation", 0.68, 0.58, 0.46, 0.78, 0.56}
    };

    std::cout << "scenario,complexity_pressure\n";
    for (const auto& scenario : scenarios) {
        std::cout << scenario.name << "," << complexity_pressure(scenario) << "\n";
    }
    return 0;
}
