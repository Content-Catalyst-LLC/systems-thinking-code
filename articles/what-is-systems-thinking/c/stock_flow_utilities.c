#include <stdio.h>

int main(void) {
    double stock = 100.0;
    double inflow = 12.0;
    double outflow_rate = 0.08;
    double outflow;

    printf("period,stock,inflow,outflow\n");
    for (int period = 1; period <= 24; period++) {
        outflow = stock * outflow_rate;
        stock = stock + inflow - outflow;
        printf("%d,%.2f,%.2f,%.2f\n", period, stock, inflow, outflow);
    }

    return 0;
}
