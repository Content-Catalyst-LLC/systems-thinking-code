#include <iostream>
int main() {
    for (double delay = 0.1; delay <= 0.9; delay += 0.2) {
        double sensitivity = delay * 0.75 + 0.15;
        std::cout << "delay_strength=" << delay << ", sensitivity=" << sensitivity << "\n";
    }
    return 0;
}
