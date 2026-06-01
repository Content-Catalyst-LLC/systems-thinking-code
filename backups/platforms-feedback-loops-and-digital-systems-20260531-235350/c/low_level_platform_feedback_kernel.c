#include <stdio.h>

static double clamp(double x, double low, double high) {
    if (x < low) return low;
    if (x > high) return high;
    return x;
}

int main(void) {
    double engagement = 55.0, risk = 22.0, trust = 72.0;
    for (int t = 0; t < 36; ++t) {
        engagement = clamp(engagement + 3.0 - risk * 0.02, 0.0, 100.0);
        risk = clamp(risk + engagement * 0.035 - trust * 0.025, 0.0, 100.0);
        trust = clamp(trust - risk * 0.05 + 1.1, 0.0, 100.0);
    }
    printf("low-level platform feedback kernel: engagement=%.3f risk=%.3f trust=%.3f\n", engagement, risk, trust);
    return 0;
}
