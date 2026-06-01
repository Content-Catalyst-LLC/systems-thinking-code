#include <algorithm>
#include <iostream>

int main() {
    double groundwater = 1000.0;
    const double recharge = 28.0;
    const double withdrawal = 55.0 * 1.18;
    std::cout << "year,groundwater\n";
    for (int year = 0; year <= 30; ++year) {
        groundwater = std::max(0.0, groundwater + recharge - withdrawal);
        std::cout << year << "," << groundwater << "\n";
    }
    return 0;
}
