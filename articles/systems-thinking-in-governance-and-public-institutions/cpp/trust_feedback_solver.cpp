#include <iostream>

int main() {
    double reliability = 0.67;
    double fairness = 0.62;
    double accountability = 0.57;
    double harm = 0.22;
    double burden = 0.35;
    double opacity = 0.41;
    double trust_delta = 0.20 * ((reliability + fairness + accountability) / 3.0) - 0.16 * ((harm + burden + opacity) / 3.0);
    std::cout << "trust_delta=" << trust_delta << "\n";
    return 0;
}
