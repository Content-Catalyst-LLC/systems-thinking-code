#include <iostream>

int main() {
    double demand_growths[] = {0.02, 0.03, 0.04, 0.05};
    double capacity_growths[] = {0.01, 0.03, 0.05};

    for (double d : demand_growths) {
        for (double c : capacity_growths) {
            std::cout << "demand=" << d << " capacity=" << c
                      << " margin=" << c - d << std::endl;
        }
    }
    return 0;
}
