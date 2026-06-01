#include <algorithm>
#include <iostream>

double ethical_leverage(double structural_change, double repair_stock, double power_redistribution, double accountability) {
    return std::max(0.0, std::min(100.0, 25.0 * structural_change + 0.22 * repair_stock + 22.0 * power_redistribution + 0.18 * accountability));
}

int main() {
    std::cout << "ethical_leverage_score=" << ethical_leverage(0.84, 70.0, 0.78, 74.0) << "\n";
    return 0;
}
