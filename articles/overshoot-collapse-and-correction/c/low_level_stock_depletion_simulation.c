#include <stdio.h>

static double clamp(double x) {
    if (x < 0.0) return 0.0;
    if (x > 1.0) return 1.0;
    return x;
}

int main(void) {
    double stock = 0.78;
    double pressure = 0.42;
    double limit = 0.60;
    for (int month = 0; month <= 24; month += 6) {
        double overshoot = pressure > limit ? pressure - limit : 0.0;
        stock = clamp(stock - overshoot * 0.08 + 0.015);
        printf("month=%d pressure=%.3f stock=%.3f overshoot=%.3f\n", month, pressure, stock, overshoot);
        pressure = pressure + 0.06 * pressure - overshoot * 0.25;
    }
    return 0;
}
