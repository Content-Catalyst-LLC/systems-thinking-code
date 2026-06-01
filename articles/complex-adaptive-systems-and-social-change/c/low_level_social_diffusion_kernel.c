#include <stdio.h>

static double clamp(double value, double low, double high) {
    if (value < low) return low;
    if (value > high) return high;
    return value;
}

int main(void) {
    double adoption = 18.0;
    printf("period,adoption\n");
    for (int period = 0; period <= 24; period++) {
        printf("%d,%.3f\n", period, adoption);
        double diffusion = 0.70 * adoption * (100.0 - adoption) / 100.0 * 0.08;
        double learning = 0.82 * 1.5;
        double resistance = 0.34 * adoption * 0.025;
        adoption = clamp(adoption + diffusion + learning - resistance, 0.0, 100.0);
    }
    return 0;
}
