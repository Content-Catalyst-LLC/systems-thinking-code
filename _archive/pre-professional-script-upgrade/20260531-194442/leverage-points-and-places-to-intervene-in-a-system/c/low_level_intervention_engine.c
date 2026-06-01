#include <stdio.h>

int main(void) {
    double stock = 60.0;
    double inflow = 8.0;
    double outflow = 4.0;
    double intervention = 1.5;
    for (int t = 1; t <= 10; ++t) {
        double adjusted_outflow = outflow - intervention;
        if (adjusted_outflow < 0.0) adjusted_outflow = 0.0;
        stock = stock + inflow - adjusted_outflow;
        printf("%d,%.2f\n", t, stock);
    }
    return 0;
}
