#include <stdio.h>

int main(void) {
    double stock = 100.0;
    double inflow = 12.0;
    double outflow_fraction = 0.05;
    printf("time,stock,inflow,outflow\n");
    for (int t = 0; t <= 24; ++t) {
        double outflow = outflow_fraction * stock;
        printf("%d,%.3f,%.3f,%.3f\n", t, stock, inflow, outflow);
        stock = stock + inflow - outflow;
        if (stock < 0.0) stock = 0.0;
    }
    return 0;
}
