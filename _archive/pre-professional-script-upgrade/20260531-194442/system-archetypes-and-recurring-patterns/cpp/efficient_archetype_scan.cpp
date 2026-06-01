#include <iostream>
#include <iomanip>

double logistic_step(double x, double r, double k) {
    return x + r * x * (1.0 - x / k);
}

int main() {
    double k = 100.0;
    std::cout << "growth_rate,final_state\n";
    for (double r = 0.10; r <= 0.50; r += 0.05) {
        double x = 8.0;
        for (int t = 0; t < 30; ++t) {
            x = logistic_step(x, r, k);
        }
        std::cout << std::fixed << std::setprecision(3) << r << "," << x << "\n";
    }
    return 0;
}
