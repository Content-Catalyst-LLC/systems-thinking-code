#include <iostream>

int main() {
    double stock = 40.0;
    double threshold = 60.0;
    for (int period = 0; period < 20; ++period) {
        stock += 3.0 - 1.0;
        if (stock >= threshold) {
            std::cout << "threshold reached at period " << period + 1 << "\n";
            return 0;
        }
    }
    std::cout << "threshold not reached\n";
    return 0;
}
