#include <iostream>

int main() {
    double x = 10.0;
    double r = 0.12;
    for (int t = 1; t <= 20; ++t) {
        x = x + r * x;
        std::cout << t << "," << x << std::endl;
    }
    return 0;
}
