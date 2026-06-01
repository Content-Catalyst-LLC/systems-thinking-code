#include <iostream>
#include <map>
#include <string>
#include <vector>

int main() {
    std::map<std::string, std::vector<std::string>> graph;
    graph["resource_flow"] = {"institutional_capacity"};
    graph["institutional_capacity"] = {"response_delay"};
    graph["response_delay"] = {"public_trust"};
    graph["public_trust"] = {"service_demand"};
    graph["service_demand"] = {"response_delay"};

    for (const auto& pair : graph) {
        std::cout << pair.first << " -> ";
        for (const auto& target : pair.second) {
            std::cout << target << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}
