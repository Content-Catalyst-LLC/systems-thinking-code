#include <stdio.h>

int main(void) {
    double loads[] = {0.70, 0.55, 0.30, 0.20};
    double threshold = 0.50;
    int failures = 0;
    for (int i = 0; i < 4; i++) {
        if (loads[i] > threshold) {
            failures++;
        }
    }
    printf("low-level cascade kernel failures=%d\n", failures);
    return 0;
}
