#include <stdio.h>

int main(void) {
    double groundwater = 1000.0;
    double recharge = 28.0;
    double withdrawal = 55.0 * 1.18;
    printf("year,groundwater\n");
    for (int year = 0; year <= 30; year++) {
        groundwater += recharge - withdrawal;
        if (groundwater < 0.0) groundwater = 0.0;
        printf("%d,%.3f\n", year, groundwater);
    }
    return 0;
}
