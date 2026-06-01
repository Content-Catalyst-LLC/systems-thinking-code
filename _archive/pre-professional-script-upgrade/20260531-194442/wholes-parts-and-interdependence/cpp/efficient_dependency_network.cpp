#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

int main() {
    std::unordered_map<std::string, std::vector<std::string>> graph = {
        {"frontline_team", {"data_platform", "public_agency"}},
        {"maintenance_unit", {"funding_stream"}},
        {"regional_infrastructure", {"maintenance_unit", "ecological_context"}},
        {"community_users", {"regional_infrastructure", "public_agency"}}
    };

    std::cout << "Efficient dependency network scaffold\n";
    for (const auto& pair : graph) {
        for (const auto& target : pair.second) {
            std::cout << pair.first << " -> " << target << "\n";
        }
    }

    return 0;
}
