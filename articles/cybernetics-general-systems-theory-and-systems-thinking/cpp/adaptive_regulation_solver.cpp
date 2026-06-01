#include <algorithm>
#include <iostream>

double adaptive_regulation_score(double regulation, double learning, double accountability, double variety_gap) {
    return std::max(0.0, std::min(100.0, regulation * 0.34 + learning * 0.24 + accountability * 0.28 - variety_gap * 0.14));
}

int main() {
    std::cout << "adaptive_regulation_score=" << adaptive_regulation_score(72.0, 68.0, 74.0, 12.0) << "\n";
    return 0;
}
