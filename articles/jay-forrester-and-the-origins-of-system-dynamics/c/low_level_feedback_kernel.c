#include <stdio.h>

static double clamp(double value, double low, double high) {
    if (value < low) return low;
    if (value > high) return high;
    return value;
}

int main(void) {
    double backlog = 58.0;
    double capacity = 46.0;

    printf("period,backlog\n");
    for (int period = 0; period <= 24; period++) {
        printf("%d,%.3f\n", period, backlog);
        double service = capacity * 0.42;
        backlog = clamp(backlog + 3.2 - service, 0.0, 200.0);
    }
    return 0;
}
