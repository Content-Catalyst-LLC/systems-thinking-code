#include <algorithm>
#include <iostream>
#include <vector>
#include <string>

struct Domain {
    std::string name;
    double disturbance_variety;
    double response_variety;
};

double variety_gap(const Domain& domain) {
    return std::max(0.0, domain.disturbance_variety - domain.response_variety);
}

int main() {
    std::vector<Domain> domains = {
        {"ai_platform_governance", 0.88, 0.52},
        {"infrastructure_operations", 0.70, 0.74},
        {"climate_adaptation", 0.92, 0.60}
    };

    std::cout << "domain,variety_gap\n";
    for (const auto& domain : domains) {
        std::cout << domain.name << "," << variety_gap(domain) << "\n";
    }
    return 0;
}
