#include <iostream>
#include <vector>

int main() {
    std::vector<double> pressure = {1.12, 1.28, 1.52, 1.71};
    for (double p : pressure) {
        std::cout << "pressure=" << p << " risk=" << (p > 1.5 ? "high" : "watch") << "\n";
    }
    return 0;
}
