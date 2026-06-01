#include <stdio.h>
int main(void) {
    double linear = 0.86, feedback = 0.24, boundary = 0.31, power = 0.28;
    double quality = (feedback + boundary + power + (1.0 - linear)) / 4.0;
    printf("systemic_quality=%.3f\n", quality);
    return 0;
}
