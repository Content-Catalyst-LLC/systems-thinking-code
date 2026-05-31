#include <iostream>

int main() {
    double x = 80.0;
    double goal = 50.0;
    double k = 0.2;
    for (int t = 0; t < 12; ++t) {
        x = x + k * (goal - x);
        std::cout << t << "," << x << "\n";
    }
    return 0;
}
