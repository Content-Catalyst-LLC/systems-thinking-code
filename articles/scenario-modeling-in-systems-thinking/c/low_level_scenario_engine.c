#include <stdio.h>

int main(void) {
    double capacity = 100.0;
    double demand = 95.0;
    double capacity_growth = 0.03;
    double demand_growth = 0.025;

    for (int year = 0; year <= 10; year++) {
        printf("%d,%.2f,%.2f,%.2f\n", year, capacity, demand, demand - capacity);
        capacity *= (1.0 + capacity_growth);
        demand *= (1.0 + demand_growth);
    }

    return 0;
}
