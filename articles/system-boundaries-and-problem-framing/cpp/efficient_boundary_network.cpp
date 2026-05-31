#include <iostream>
#include <map>
#include <string>
#include <vector>

int main() {
    std::map<std::string, std::vector<std::string>> boundary_network = {
        {"narrow_boundary", {"hidden_externalities", "excluded_stakeholders"}},
        {"hidden_externalities", {"false_efficiency", "future_risk"}},
        {"excluded_stakeholders", {"low_legitimacy", "missed_harms"}}
    };

    for (const auto& pair : boundary_network) {
        std::cout << pair.first << " -> ";
        for (const auto& target : pair.second) {
            std::cout << target << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}
