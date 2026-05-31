#include <stdio.h>

int main(void) {
    double trust = 0.48;
    for (int t = 1; t <= 6; ++t) {
        double reliability = 0.45 + 0.04 * t;
        double fairness = 0.42 + 0.035 * t;
        double accountability = 0.38 + 0.035 * t;
        double burden = 0.78 - 0.05 * t;
        trust += 0.06 * ((reliability + fairness + accountability) / 3.0) - 0.05 * burden;
        if (trust > 1.0) trust = 1.0;
        if (trust < 0.0) trust = 0.0;
        printf("period=%d trust=%.3f\n", t, trust);
    }
    return 0;
}
