#include <iostream>
#include <vector>
#include <string>

int main() {
    std::vector<std::string> variables = {"Trust", "Cooperation", "Performance"};
    std::vector<std::vector<int>> signed_edges = {
        {0, 1, 1},
        {1, 2, 1},
        {2, 0, 1}
    };
    for (const auto& edge : signed_edges) {
        std::cout << variables[edge[0]] << " --" << (edge[2] > 0 ? "+" : "-")
                  << "--> " << variables[edge[1]] << "\n";
    }
    return 0;
}
