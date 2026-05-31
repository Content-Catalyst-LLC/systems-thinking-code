#include <iostream>
#include <vector>
int main() {
    std::vector<double> advantage {82, 28, 24, 90};
    double max_v = advantage[0], min_v = advantage[0];
    for (double v : advantage) { if (v > max_v) max_v = v; if (v < min_v) min_v = v; }
    std::cout << "advantage_gap=" << (max_v - min_v) << "\n";
    return 0;
}
