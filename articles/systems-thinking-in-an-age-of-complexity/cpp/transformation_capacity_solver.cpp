#include <algorithm>
#include <iostream>

double transformation_capacity(double ethical_leverage, double learning_stock, double accountability, double resilience_stock, double boundary_inclusion, double harm_stock) {
    return std::max(0.0, std::min(100.0, 26.0 * ethical_leverage + 0.20 * learning_stock + 0.22 * accountability + 0.16 * resilience_stock + 14.0 * boundary_inclusion - 0.12 * harm_stock));
}

int main() {
    std::cout << "transformation_capacity=" << transformation_capacity(0.84, 76.0, 78.0, 72.0, 0.82, 28.0) << "\n";
    return 0;
}
