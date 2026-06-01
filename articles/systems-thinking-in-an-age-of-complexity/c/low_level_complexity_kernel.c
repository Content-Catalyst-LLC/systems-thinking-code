#include <stdio.h>

static double clamp(double value, double low, double high) {
    if (value < low) return low;
    if (value > high) return high;
    return value;
}

int main(void) {
    double readiness = 34.0;
    double harm = 62.0;
    double learning = 36.0;

    printf("period,readiness,harm,learning\n");
    for (int period = 0; period <= 36; period++) {
        printf("%d,%.3f,%.3f,%.3f\n", period, readiness, harm, learning);
        learning = clamp(learning + 2.0 - harm * 0.01, 0.0, 100.0);
        readiness = clamp(readiness + learning * 0.05 - harm * 0.03, 0.0, 100.0);
        harm = clamp(harm - readiness * 0.04 + 0.8, 0.0, 100.0);
    }

    return 0;
}
