#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::vector<double> drift = {5.0, 8.5, 12.2, 18.4, 22.1, 29.7, 35.4};
    double threshold = 25.0;
    std::cout << "period,drift,alert\n";
    for (size_t i = 0; i < drift.size(); ++i) {
        std::cout << i << "," << drift[i] << "," << (drift[i] >= threshold ? "review" : "monitor") << "\n";
    }
    return 0;
}
