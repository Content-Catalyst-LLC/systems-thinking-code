#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    const int months = 36;
    const int delay = 5;
    const double goal = 1.0;
    const double correction = 0.45;
    std::vector<double> x(delay + 1, 0.35);
    for (int t = 0; t < months; ++t) {
        double delayed = x[x.size() - delay];
        double next = x.back() + correction * (goal - delayed);
        next = std::max(0.0, std::min(1.8, next));
        x.push_back(next);
        std::cout << t << "," << next << "\n";
    }
    return 0;
}
