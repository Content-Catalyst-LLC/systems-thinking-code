/* Low-level temporal simulation utility in C. */
#include <stdio.h>

int main(void) {
    double stock = 20.0;
    double inflow = 10.0;
    double outflow = 4.0;
    printf("year,stock\n");
    for (int year = 1; year <= 10; year++) {
        stock = stock + inflow - outflow;
        if (stock < 0) stock = 0;
        printf("%d,%.2f\n", year, stock);
    }
    return 0;
}
