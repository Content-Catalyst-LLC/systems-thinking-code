#include <stdio.h>

static double clamp01(double x) {
    if (x < 0.0) return 0.0;
    if (x > 1.0) return 1.0;
    return x;
}

int main(void) {
    const int agents = 40;
    double states[40], next[40];
    for (int i = 0; i < agents; ++i) states[i] = ((i * 17) % 100) / 100.0;
    for (int t = 0; t < 20; ++t) {
        for (int i = 0; i < agents; ++i) {
            double left = states[(i + agents - 1) % agents];
            double right = states[(i + 1) % agents];
            double local = (left + right) / 2.0;
            next[i] = clamp01(states[i] + 0.18 * (local - states[i]));
        }
        for (int i = 0; i < agents; ++i) states[i] = next[i];
    }
    double sum = 0.0;
    for (int i = 0; i < agents; ++i) sum += states[i];
    printf("C emergence kernel final mean: %.4f\n", sum / agents);
    return 0;
}
