#include <iostream>

double adjusted_score(double value, double internal_cost, double external_cost, double external_weight) {
    return value - internal_cost - external_weight * external_cost;
}

int main() {
    double value = 220000.0;
    double internal_cost = 90000.0;
    double external_cost = 280000.0;

    std::cout << "Narrow boundary score: "
              << adjusted_score(value, internal_cost, external_cost, 0.25)
              << std::endl;

    std::cout << "Broad boundary score: "
              << adjusted_score(value, internal_cost, external_cost, 1.0)
              << std::endl;

    return 0;
}
