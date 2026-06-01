#include <algorithm>
#include <iostream>

double defensive_routine_next(double current, double pressure, double blame, double safety, double inquiry) {
    return std::max(0.0, std::min(100.0, current + pressure * 2.4 + blame * 2.8 - safety * 3.0 - inquiry * 1.8));
}

int main() {
    std::cout << "next_defensive_routine_index=" << defensive_routine_next(42.0, 0.50, 0.34, 0.60, 0.58) << "\n";
    return 0;
}
