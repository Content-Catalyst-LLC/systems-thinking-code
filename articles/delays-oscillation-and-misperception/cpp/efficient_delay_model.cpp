#include <iostream>
#include <vector>

int main() {
    double goal = 50.0;
    double correction = 0.25;
    int delay = 3;
    std::vector<double> x(delay + 1, 80.0);

    for (int t = 1; t <= 20; ++t) {
        double observed = x[x.size() - delay];
        double next = x.back() + correction * (goal - observed);
        x.push_back(next);
        std::cout << t << "," << next << "," << observed << "\n";
    }
    return 0;
}
