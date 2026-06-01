// Professional threshold scan for Systems Thinking Patterns Interdependence Structural Change
#include <algorithm>
#include <iomanip>
#include <iostream>
static double clamp(double x, double lo, double hi) { return std::max(lo, std::min(hi, x)); }
int main() {
    std::cout << "pressure_reduction,capacity_investment,final_stock,final_risk\n";
    for (double pr = 0.0; pr <= 0.5001; pr += 0.1) { for (double ci = 0.0; ci <= 3.0001; ci += 0.5) {
        double stock = 80, capacity = 50, burden = 36;
        for (int year = 0; year <= 30; ++year) {
            double pressure = (4.2 + 1.9 * year * 0.45) * (1.0 - pr);
            burden = clamp(burden + pressure * 0.08 - ci * 0.35, 0.0, 100.0);
            capacity = clamp(capacity + ci - burden * 0.015, 0.0, 100.0);
            stock = clamp(stock + stock * 0.026 - pressure - burden * 0.035 + capacity * 0.025, 0.0, 120.0);
        }
        double risk = clamp(100.0 - (0.45 * stock + 0.35 * capacity - 0.20 * burden), 0.0, 100.0);
        std::cout << std::fixed << std::setprecision(2) << pr << "," << ci << "," << stock << "," << risk << "\n";
    } }
}
