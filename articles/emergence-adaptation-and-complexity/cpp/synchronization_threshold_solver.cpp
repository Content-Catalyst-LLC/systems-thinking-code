#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

static double clamp01(double x) { return std::max(0.0, std::min(1.0, x)); }

int main() {
    const int agents = 40;
    std::vector<double> states(agents), next(agents);
    for (int i = 0; i < agents; ++i) states[i] = ((i * 17) % 100) / 100.0;
    for (int t = 0; t < 20; ++t) {
        for (int i = 0; i < agents; ++i) {
            double left = states[(i + agents - 1) % agents];
            double right = states[(i + 1) % agents];
            double local = (left + right) / 2.0;
            next[i] = clamp01(states[i] + 0.18 * (local - states[i]));
        }
        states = next;
    }
    double sum = std::accumulate(states.begin(), states.end(), 0.0);
    std::cout << "C++ synchronization solver final mean: " << sum / agents << "\n";
    return 0;
}
