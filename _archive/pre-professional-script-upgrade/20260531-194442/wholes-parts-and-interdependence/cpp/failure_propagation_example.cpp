#include <iostream>
#include <iomanip>

int main() {
    double stress = 25.0;
    double damping = 0.65;

    std::cout << "step,stress\n";
    for (int step = 1; step <= 6; ++step) {
        stress *= damping;
        std::cout << step << "," << std::fixed << std::setprecision(2) << stress << "\n";
    }

    return 0;
}
