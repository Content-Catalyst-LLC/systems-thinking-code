#include <stdio.h>

int main(void) {
    double x = 80.0;
    double goal = 50.0;
    double k = 0.25;
    for (int t = 1; t <= 20; ++t) {
        x = x + k * (goal - x);
        printf("%d,%.3f\n", t, x);
    }
    return 0;
}
