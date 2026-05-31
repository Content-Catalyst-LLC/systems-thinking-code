#include <iostream>

int main() {
    double observed = 0.62;
    double distortion = 0.28;
    int delay = 4;
    double actionable = observed * (1.0 - distortion) - delay * 0.04;
    std::cout << "actionable_signal=" << actionable << "\n";
    return 0;
}
