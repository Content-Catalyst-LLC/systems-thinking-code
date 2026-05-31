#include <algorithm>
#include <iostream>

int main() {
    double pressure = 0.40;
    double stock = 0.78;
    double limit = 0.60;
    for (int month = 0; month <= 24; month += 6) {
        double overshoot = std::max(0.0, pressure - limit);
        stock = std::clamp(stock - overshoot * 0.08 + 0.015, 0.0, 1.0);
        std::cout << "month=" << month << " pressure=" << pressure << " stock=" << stock << "\n";
        pressure = std::clamp(pressure + 0.07 * pressure - overshoot * 0.25, 0.0, 1.2);
    }
    return 0;
}
