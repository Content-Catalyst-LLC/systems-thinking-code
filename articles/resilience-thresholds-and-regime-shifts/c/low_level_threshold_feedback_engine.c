#include <stdio.h>

static double clamp(double v, double low, double high) {
    if (v < low) return low;
    if (v > high) return high;
    return v;
}

int main(void) {
    double resilience = 78.0;
    double pressure = 35.0;
    for (int year = 0; year <= 20; year++) {
        pressure += 2.3;
        resilience = clamp(resilience + 1.2 - 2.0 - pressure * 0.02, 0.0, 100.0);
        double margin = resilience - pressure;
        const char *regime = margin <= 0.0 ? "shifted" : (margin <= 10.0 ? "near_threshold" : "recoverable");
        printf("%02d resilience=%.2f pressure=%.2f margin=%.2f regime=%s\n", year, resilience, pressure, margin, regime);
    }
    return 0;
}
