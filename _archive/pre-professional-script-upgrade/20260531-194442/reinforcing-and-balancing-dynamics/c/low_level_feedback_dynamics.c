#include <stdio.h>

int main(void) {
    double x = 10.0;
    double r = 0.12;
    for (int t = 1; t <= 20; t++) {
        x = x + r * x;
        printf("%d,%f\n", t, x);
    }
    return 0;
}
