#include <iostream>
#include <string>
#include <tuple>
#include <vector>

int main() {
    std::vector<std::tuple<std::string, std::string, int>> edges = {
        {"Public Trust", "Cooperation", 1},
        {"Cooperation", "Service Performance", 1},
        {"Service Performance", "Public Trust", 1}
    };
    std::cout << "Efficient loop detection scaffold\n";
    for (const auto& [source, target, sign] : edges) {
        std::cout << source << " --" << (sign > 0 ? "+" : "-") << "--> " << target << "\n";
    }
    return 0;
}
