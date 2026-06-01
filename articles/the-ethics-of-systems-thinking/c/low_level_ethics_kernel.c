#include <stdio.h>

static double clamp(double value, double low, double high) {
    if (value < low) return low;
    if (value > high) return high;
    return value;
}

int main(void) {
    double accountability = 42.0;
    double repair = 28.0;
    double harm = 60.0;

    printf("period,accountability_index,repair_stock,cumulative_harm\n");
    for (int period = 0; period <= 36; period++) {
        printf("%d,%.3f,%.3f,%.3f\n", period, accountability, repair, harm);
        accountability = clamp(accountability + 2.1, 0.0, 100.0);
        repair = clamp(repair + 1.8, 0.0, 100.0);
        harm = clamp(harm - 0.08 * repair + 0.02 * (100.0 - accountability), 0.0, 100.0);
    }

    return 0;
}
