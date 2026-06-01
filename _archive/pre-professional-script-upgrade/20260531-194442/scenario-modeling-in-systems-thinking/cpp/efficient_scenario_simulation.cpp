#include <iostream>
#include <vector>
#include <string>

struct Scenario {
    std::string name;
    double capacity_growth;
    double demand_growth;
};

int main() {
    std::vector<Scenario> scenarios = {
        {"baseline", 0.01, 0.03},
        {"early_prevention", 0.03, 0.025},
        {"stress_case", 0.00, 0.05}
    };

    for (const auto& s : scenarios) {
        double capacity = 100.0;
        double demand = 95.0;
        for (int year = 0; year <= 10; ++year) {
            if (year == 10) {
                std::cout << s.name << " year_10_gap " << demand - capacity << std::endl;
            }
            capacity *= (1.0 + s.capacity_growth);
            demand *= (1.0 + s.demand_growth);
        }
    }
    return 0;
}
