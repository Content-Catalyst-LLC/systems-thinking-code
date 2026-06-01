#include <iostream>
#include <vector>

int main() {
    std::vector<double> burden{0.71, 0.68, 0.48, 0.55, 0.51, 0.43};
    for (std::size_t i = 0; i < burden.size(); ++i) {
        std::cout << "scenario " << i + 1 << " burden=" << burden[i] << "\n";
    }
    return 0;
}
