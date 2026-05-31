#include <iostream>
#include <string>
#include <vector>

struct Edge {
    std::string source;
    std::string target;
    std::string sign;
};

int main() {
    std::vector<Edge> edges = {
        {"maintenance_backlog", "response_delay", "+"},
        {"response_delay", "public_trust", "-"},
        {"workload_pressure", "institutional_capacity", "-"},
        {"institutional_capacity", "response_delay", "-"}
    };

    for (const auto& edge : edges) {
        std::cout << edge.source << " --(" << edge.sign << ")--> " << edge.target << "\n";
    }

    return 0;
}
