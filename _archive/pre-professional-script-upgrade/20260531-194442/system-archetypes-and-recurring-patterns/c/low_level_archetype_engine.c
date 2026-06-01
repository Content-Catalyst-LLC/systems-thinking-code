#include <stdio.h>

static double limits_to_growth_step(double x, double r, double k) {
    return x + r * x * (1.0 - x / k);
}

int main(void) {
    double x = 8.0;
    double r = 0.32;
    double k = 100.0;

    printf("time,state\n");
    for (int t = 0; t <= 30; ++t) {
        printf("%d,%.4f\n", t, x);
        x = limits_to_growth_step(x, r, k);
    }

    return 0;
}
