#include <stdio.h>

int main(void) {
    double burnout = 0.35;
    for (int t = 1; t <= 8; ++t) {
        double pressure = 0.55 + 0.03 * t;
        double recovery = 0.45 - 0.02 * t;
        burnout = burnout + 0.16 * pressure - 0.10 * recovery;
        if (burnout > 1.0) burnout = 1.0;
        printf("period=%d burnout=%.3f\n", t, burnout);
    }
    return 0;
}
