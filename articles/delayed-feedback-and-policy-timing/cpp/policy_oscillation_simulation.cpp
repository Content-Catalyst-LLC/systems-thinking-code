#include <iostream>
#include <cmath>

int main() {
    double state = 0.4;
    double previous = 0.4;
    double goal = 1.0;
    double correction = 0.7;
    for (int t = 0; t < 24; ++t) {
        double next = state + correction * (goal - previous);
        previous = state;
        state = next;
        std::cout << t << "," << state << "\n";
    }
    return 0;
}
