#include <iostream>
#include <vector>

int main() {
    std::vector<double> compensation{0.0, 0.25, 0.5, 0.75, 1.0};
    double intended = 100.0;
    for (double c : compensation) {
        std::cout << "compensation=" << c << " net=" << intended * (1.0 - c) << "\n";
    }
    return 0;
}
