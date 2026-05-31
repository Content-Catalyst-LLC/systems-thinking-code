#include <iostream>
#include <vector>

int main() {
    std::vector<double> distortion{0.15, 0.25, 0.35, 0.45};
    for (double d : distortion) {
        std::cout << "received_signal_multiplier=" << (1.0 - d) << "\n";
    }
    return 0;
}
