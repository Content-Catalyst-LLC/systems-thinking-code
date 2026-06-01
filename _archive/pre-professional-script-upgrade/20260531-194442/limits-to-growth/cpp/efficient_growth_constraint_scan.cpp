// Efficient growth-constraint scan scaffold.
#include <iostream>
#include <iomanip>

int main() {
    double scale = 100.0;
    double rate = 0.13;
    double capacity = 260.0;
    for (int year = 0; year <= 25; ++year) {
        std::cout << year << "," << std::fixed << std::setprecision(3) << scale << "," << scale / capacity << "\n";
        scale += rate * scale * (1.0 - scale / capacity);
    }
    return 0;
}
