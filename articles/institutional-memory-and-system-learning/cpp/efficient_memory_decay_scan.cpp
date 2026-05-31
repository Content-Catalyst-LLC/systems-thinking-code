#include <iostream>
#include <vector>

int main() {
    std::vector<double> memory{0.52, 0.56, 0.58, 0.65, 0.72, 0.80};
    for (std::size_t i = 1; i < memory.size(); ++i) {
        std::cout << "period " << i + 1 << " memory_change=" << memory[i] - memory[i - 1] << "\n";
    }
    return 0;
}
