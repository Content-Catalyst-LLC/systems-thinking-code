#include <iostream>
#include <vector>

int main() {
    std::vector<double> capacity{74, 68, 61, 55};
    for (std::size_t i = 1; i < capacity.size(); ++i) {
        std::cout << "period " << i + 1 << " capacity_change=" << capacity[i] - capacity[i - 1] << "\n";
    }
    return 0;
}
