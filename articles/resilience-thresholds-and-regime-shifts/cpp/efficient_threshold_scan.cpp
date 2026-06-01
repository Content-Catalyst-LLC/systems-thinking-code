#include <algorithm>
#include <iostream>
#include <string>

int main() {
    double resilience = 78.0;
    double pressure = 35.0;
    for (int year = 0; year <= 20; ++year) {
        pressure += 2.3;
        resilience = std::clamp(resilience + 1.5 - 2.2 - pressure * 0.018, 0.0, 100.0);
        double margin = resilience - pressure;
        std::string regime = margin <= 0.0 ? "shifted" : (margin <= 10.0 ? "near_threshold" : "recoverable");
        std::cout << year << "," << resilience << "," << pressure << "," << margin << "," << regime << "\n";
    }
    return 0;
}
