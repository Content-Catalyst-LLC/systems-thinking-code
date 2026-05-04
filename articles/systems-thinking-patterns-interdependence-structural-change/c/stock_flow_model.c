#include <stdio.h>

int main(void) {
    const int steps = 20;
    double stock[steps];
    double inflow = 5.0;
    double outflow = 3.5;

    stock[0] = 50.0;

    for (int t = 1; t < steps; t++) {
        stock[t] = stock[t - 1] + inflow - outflow;
        if (stock[t] < 0.0) {
            stock[t] = 0.0;
        }
    }

    printf("Stock-flow simulation\n");

    for (int t = 0; t < steps; t++) {
        printf("time=%d, stock=%.2f\n", t, stock[t]);
    }

    return 0;
}
