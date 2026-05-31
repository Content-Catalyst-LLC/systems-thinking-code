// Overshoot threshold solver scaffold.
#include <iostream>

int main() {
    double scale = 275.0;
    double capacity = 260.0;
    if (scale > capacity) {
        std::cout << "overshoot=true pressure=" << scale / capacity << "\n";
    } else {
        std::cout << "overshoot=false pressure=" << scale / capacity << "\n";
    }
    return 0;
}
