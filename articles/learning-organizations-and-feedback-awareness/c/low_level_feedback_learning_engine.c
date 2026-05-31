#include <stdio.h>

int main(void) {
    double learning = 0.20;
    for (int t = 1; t <= 6; ++t) {
        learning = learning + 0.08 * (1.0 - learning);
        printf("period=%d learning=%.4f\n", t, learning);
    }
    return 0;
}
