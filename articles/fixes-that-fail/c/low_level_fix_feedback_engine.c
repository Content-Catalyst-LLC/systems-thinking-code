#include <stdio.h>

int main(void) {
    double problem = 100.0;
    double delay[3] = {0.0, 0.0, 0.0};
    for (int t = 0; t < 12; t++) {
        double fix = problem / 140.0;
        if (fix > 1.0) fix = 1.0;
        double harm = delay[0] * 20.0;
        delay[0] = delay[1];
        delay[1] = delay[2];
        delay[2] = fix;
        problem = problem + 7.0 - 25.0 * fix + harm;
        if (problem < 0.0) problem = 0.0;
        printf("period=%d problem=%.2f fix=%.3f delayed_harm=%.2f\n", t, problem, fix, harm);
    }
    return 0;
}
