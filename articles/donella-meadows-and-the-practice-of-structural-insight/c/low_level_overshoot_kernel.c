#include <stdio.h>

static double clamp(double value, double low, double high) {
    if (value < low) return low;
    if (value > high) return high;
    return value;
}

static double max_value(double a, double b) {
    return a > b ? a : b;
}

int main(void) {
    double resource = 82.0;

    printf("period,resource_stock,consumption,regeneration\n");
    for (int period = 0; period <= 36; period++) {
        double consumption = clamp(0.62 * 9.0 + max_value(0.0, 70.0 - resource) * 0.04, 0.0, 100.0);
        double regeneration = clamp(0.50 * 6.0 + 2.5, 0.0, 100.0);
        printf("%d,%.3f,%.3f,%.3f\n", period, resource, consumption, regeneration);
        resource = clamp(resource - consumption + regeneration, 0.0, 100.0);
    }
    return 0;
}
