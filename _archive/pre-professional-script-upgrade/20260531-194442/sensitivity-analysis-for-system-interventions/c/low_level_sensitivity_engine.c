#include <stdio.h>

static double clamp(double x) {
    if (x < 0.0) return 0.0;
    if (x > 1.0) return 1.0;
    return x;
}

int main(void) {
    for (int delay = 1; delay <= 18; ++delay) {
        double score = clamp(0.68 - 0.035 * delay + 1.2 * 0.08 - 1.4 * 0.05);
        printf("delay=%d resilience=%.3f\n", delay, score);
    }
    return 0;
}
