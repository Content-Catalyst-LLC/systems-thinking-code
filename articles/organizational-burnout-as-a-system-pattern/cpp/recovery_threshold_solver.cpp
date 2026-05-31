#include <iostream>

int main() {
    double workload = 84.0;
    double capacity = 55.0;
    double target_pressure = 1.0;
    double required_capacity = workload / target_pressure;
    std::cout << "required_capacity=" << required_capacity << " current_capacity=" << capacity << "\n";
    return 0;
}
