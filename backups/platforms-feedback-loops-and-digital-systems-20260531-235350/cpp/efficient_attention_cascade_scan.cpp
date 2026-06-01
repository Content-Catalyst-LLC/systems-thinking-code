#include <algorithm>
#include <iostream>

static double clamp(double x, double low, double high) {
    return std::max(low, std::min(high, x));
}

int main() {
    double attention = 55.0;
    double cascade = 22.0;
    double governance = 45.0;
    for (int t = 0; t < 36; ++t) {
        attention = clamp(attention + 0.07 * attention - 0.02 * governance, 0.0, 100.0);
        cascade = clamp(cascade + 0.05 * attention - 0.035 * governance, 0.0, 100.0);
        governance = clamp(governance + 0.6 - 0.01 * cascade, 0.0, 100.0);
    }
    std::cout << "attention cascade scan: attention=" << attention << " cascade=" << cascade << " governance=" << governance << "\n";
    return 0;
}
