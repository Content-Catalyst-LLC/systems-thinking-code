#include <iostream>

int main() {
    double repair = 0.40;
    double capacity = 0.65;
    for (double fix = 0.1; fix <= 1.2; fix += 0.1) {
        double ratio = fix / (repair + capacity);
        if (ratio >= 1.0) {
            std::cout << "dependency threshold reached near fix=" << fix << " ratio=" << ratio << "\n";
            return 0;
        }
    }
    std::cout << "threshold not reached in scan\n";
    return 0;
}
