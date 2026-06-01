#include <stdio.h>

int main(void) {
    double stock = 42.0;
    double inflow = 3.2;
    double outflow = 2.6;
    for (int month = 0; month <= 24; month++) {
        printf("%d,%.2f\n", month, stock);
        stock = stock + inflow - outflow;
        if (stock < 0.0) stock = 0.0;
        if (stock > 100.0) stock = 100.0;
    }
    return 0;
}
