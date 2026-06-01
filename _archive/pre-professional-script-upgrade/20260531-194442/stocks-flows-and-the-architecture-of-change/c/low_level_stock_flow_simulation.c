#include <stdio.h>

int main(void) {
    double stock = 55.0;
    double inflow = 4.0;
    double outflow = 5.0;
    for (int t = 0; t < 10; t++) {
        printf("%d,%.3f\n", t, stock);
        stock += inflow - outflow;
    }
    return 0;
}
