#include <stdio.h>

double net_value(double measured_value, double internal_cost, double external_cost, double external_weight) {
    return measured_value - internal_cost - external_weight * external_cost;
}

int main(void) {
    double measured_value = 220000.0;
    double internal_cost = 90000.0;
    double external_cost = 280000.0;

    printf("narrow_boundary_score: %.2f\n", net_value(measured_value, internal_cost, external_cost, 0.25));
    printf("broad_boundary_score: %.2f\n", net_value(measured_value, internal_cost, external_cost, 1.0));

    return 0;
}
