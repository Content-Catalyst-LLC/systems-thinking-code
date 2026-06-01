#include <iostream>
#include <vector>

int main() {
    std::vector<double> loads{0.70, 0.55, 0.30, 0.20};
    double threshold = 0.50;
    int failures = 0;
    for (double load : loads) {
        if (load > threshold) {
            failures++;
        }
    }
    std::cout << "efficient cascade scan failures=" << failures << "\n";
    return 0;
}
