#include <stdio.h>

int main(void) {
    double value = 85.0;
    double goal = 50.0;
    double adjustment = 0.22;

    printf("period,value\n");
    for (int period = 1; period <= 20; period++) {
        value = value + adjustment * (goal - value);
        printf("%d,%.2f\n", period, value);
    }

    return 0;
}
