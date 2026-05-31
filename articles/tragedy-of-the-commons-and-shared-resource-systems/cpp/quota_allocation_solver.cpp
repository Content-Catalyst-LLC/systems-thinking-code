#include <iostream>
#include <vector>

int main() {
    std::vector<double> requested = {95.0, 60.0, 45.0};
    double sustainable_total = 140.0;
    double total_requested = 0.0;
    for (double value : requested) total_requested += value;
    for (double value : requested) {
        double quota = value / total_requested * sustainable_total;
        std::cout << "quota=" << quota << "\n";
    }
    return 0;
}
