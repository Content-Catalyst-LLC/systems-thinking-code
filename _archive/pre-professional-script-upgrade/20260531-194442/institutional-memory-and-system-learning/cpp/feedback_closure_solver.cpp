#include <iostream>

int main() {
    double received = 120.0;
    double acted = 84.0;
    double closed = 72.0;
    std::cout << "acted_rate=" << acted / received << " closed_rate=" << closed / received << "\n";
    return 0;
}
