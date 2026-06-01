#include <stdio.h>

static double clamp(double v) {
    if (v < 0.0) return 0.0;
    if (v > 100.0) return 100.0;
    return v;
}

int main(void) {
    double risk = 30.0;
    double governance = 50.0;
    printf("period,risk,governance\n");
    for (int t = 0; t <= 12; ++t) {
        printf("%d,%.3f,%.3f\n", t, risk, governance);
        risk = clamp(risk + 2.1 - governance * 0.03);
        governance = clamp(governance + 1.0);
    }
    return 0;
}
