#include <algorithm>
#include <iostream>

static double clamp(double x) { return std::max(0.0, std::min(100.0, x)); }

int main() {
    double best_resilience = -1.0;
    double best_transit = 0.0;
    for (double transit = 0.0; transit <= 12.0; transit += 1.0) {
        double congestion = 52.0;
        double affordability = 42.0;
        double infrastructure = 58.0;
        double displacement = 44.0;
        for (int year = 0; year <= 30; ++year) {
            congestion = clamp(congestion + 0.7 - transit * 0.10 + displacement * 0.006);
            affordability = clamp(affordability + transit * 0.08 - congestion * 0.012 - displacement * 0.006);
            infrastructure = clamp(infrastructure + 0.55 - 1.05 - congestion * 0.007);
            displacement = clamp(displacement + transit * 0.03 + congestion * 0.004 - affordability * 0.006);
        }
        double resilience = clamp((100 - congestion) * 0.25 + affordability * 0.25 + infrastructure * 0.30 + (100 - displacement) * 0.20);
        if (resilience > best_resilience) {
            best_resilience = resilience;
            best_transit = transit;
        }
    }
    std::cout << "Best transit investment score=" << best_transit << " resilience=" << best_resilience << "\n";
    return 0;
}
