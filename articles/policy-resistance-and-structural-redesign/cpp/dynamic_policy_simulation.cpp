#include <iostream>

int main() {
    double outcome = 50.0;
    double policy = 0.7;
    double compensation = 0.4;
    for (int month = 1; month <= 12; ++month) {
        double offset = compensation * (outcome > 50.0 ? (outcome - 50.0) / 50.0 : 0.0);
        outcome += 3.0 * policy - 2.0 * offset;
        std::cout << month << "," << outcome << "\n";
    }
    return 0;
}
