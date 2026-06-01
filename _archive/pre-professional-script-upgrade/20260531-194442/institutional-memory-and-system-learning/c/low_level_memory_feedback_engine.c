#include <stdio.h>

int main(void) {
    double memory = 0.52;
    for (int t = 1; t <= 8; ++t) {
        double learning = 0.055 + 0.01 * t;
        double documentation = 0.045 + 0.005 * t;
        double turnover_loss = (t == 2 || t == 5 || t == 7) ? 0.05 : 0.025;
        memory = memory + learning + documentation + 0.035 - turnover_loss - 0.028 - 0.018;
        if (memory > 1.0) memory = 1.0;
        if (memory < 0.0) memory = 0.0;
        printf("period=%d memory=%.3f\n", t, memory);
    }
    return 0;
}
