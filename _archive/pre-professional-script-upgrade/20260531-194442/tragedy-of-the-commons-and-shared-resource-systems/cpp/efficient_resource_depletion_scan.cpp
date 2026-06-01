#include <algorithm>
#include <iostream>

int main() {
    double stock = 1000.0;
    double capacity = 1400.0;
    double regen_rate = 0.22;
    double annual_use = 120.0;
    for (int year = 0; year < 25; ++year) {
        double regeneration = regen_rate * stock * std::max(0.0, 1.0 - stock / capacity);
        stock = std::max(0.0, stock + regeneration - annual_use);
    }
    std::cout << "Final synthetic commons stock: " << stock << "\n";
    return 0;
}
