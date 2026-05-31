#include <iostream>
#include <vector>

int main() {
    std::vector<double> stock {0.78, 0.73, 0.64, 0.49, 0.41};
    const double critical = 0.35;
    for (std::size_t i = 0; i < stock.size(); ++i) {
        double margin = stock[i] - critical;
        std::cout << "step=" << i << " stock=" << stock[i] << " margin=" << margin << "\n";
    }
    return 0;
}
