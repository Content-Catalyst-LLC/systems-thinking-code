// Simple structural dynamics simulation in C++.
#include <iostream>

int main() {
    double backlog = 40.0;
    double prevention = 6.0;
    double deterioration = 12.0;
    for (int year = 1; year <= 10; ++year) {
        backlog += deterioration - prevention;
        if (backlog < 0) backlog = 0;
        std::cout << year << "," << backlog << "\n";
    }
    return 0;
}
