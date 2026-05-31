#include <iostream>
#include <map>
#include <string>
#include <vector>

int main() {
    std::map<std::string, std::vector<std::string>> graph;
    graph["resource_flow"].push_back("institutional_capacity");
    graph["institutional_capacity"].push_back("response_delay");
    graph["response_delay"].push_back("public_trust");
    graph["maintenance_backlog"].push_back("institutional_capacity");

    for (const auto& pair : graph) {
        std::cout << pair.first << ": ";
        for (const auto& target : pair.second) {
            std::cout << target << " ";
        }
        std::cout << "\n";
    }

    return 0;
}
