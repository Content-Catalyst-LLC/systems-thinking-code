#include <stdio.h>

int main(void) {
    double state = 0.35;
    double delayed = 0.35;
    double goal = 1.0;
    double correction = 0.45;
    for (int t = 0; t < 24; ++t) {
        state = state + correction * (goal - delayed);
        delayed = 0.9 * delayed + 0.1 * state;
        printf("%d,%.4f\n", t, state);
    }
    return 0;
}
