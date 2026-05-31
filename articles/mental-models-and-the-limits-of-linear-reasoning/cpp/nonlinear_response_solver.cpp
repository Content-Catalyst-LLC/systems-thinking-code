#include <iostream>
#include <cmath>
int main() {
    double state = 50.0;
    for (int t = 1; t <= 10; ++t) {
        state += 4.0 - 0.01 * std::pow(state, 1.25);
        std::cout << "period=" << t << ", state=" << state << "\n";
    }
    return 0;
}
