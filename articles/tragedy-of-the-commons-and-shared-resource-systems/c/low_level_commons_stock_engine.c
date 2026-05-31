#include <stdio.h>

int main(void) {
    double stock = 1000.0;
    double capacity = 1400.0;
    double regen_rate = 0.22;
    double annual_use = 120.0;
    for (int year = 0; year < 25; year++) {
        double limiter = 1.0 - stock / capacity;
        if (limiter < 0.0) limiter = 0.0;
        double regeneration = regen_rate * stock * limiter;
        stock = stock + regeneration - annual_use;
        if (stock < 0.0) stock = 0.0;
    }
    printf("Final synthetic commons stock: %.2f\n", stock);
    return 0;
}
