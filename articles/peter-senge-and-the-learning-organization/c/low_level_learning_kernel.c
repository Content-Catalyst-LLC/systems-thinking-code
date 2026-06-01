#include <stdio.h>

static double clamp(double value, double low, double high) {
    if (value < low) return low;
    if (value > high) return high;
    return value;
}

int main(void) {
    double learning = 34.0;
    double defensiveness = 42.0;

    printf("period,learning_stock,defensive_routines\n");
    for (int period = 0; period <= 36; period++) {
        printf("%d,%.3f,%.3f\n", period, learning, defensiveness);
        double learning_flow = 0.70 * 4.5 + 0.68 * 3.8 - defensiveness * 0.035;
        double forgetting = defensiveness * 0.025;
        learning = clamp(learning + learning_flow - forgetting, 0.0, 100.0);
        defensiveness = clamp(defensiveness + 1.0 - 0.68 * 2.4, 0.0, 100.0);
    }

    return 0;
}
