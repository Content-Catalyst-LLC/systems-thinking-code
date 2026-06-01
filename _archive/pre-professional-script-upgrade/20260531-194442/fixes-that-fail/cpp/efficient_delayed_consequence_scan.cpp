#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    for (double side_effect : {0.10, 0.20, 0.30, 0.40}) {
        double problem = 100.0;
        std::vector<double> delay(3, 0.0);
        for (int t = 0; t < 12; ++t) {
            double fix = std::min(1.0, problem / 140.0);
            double harm = delay.front() * 50.0 * side_effect;
            delay.erase(delay.begin());
            delay.push_back(fix);
            problem = std::max(0.0, problem + 7.0 - 25.0 * fix + harm);
        }
        std::cout << "side_effect=" << side_effect << " final_problem=" << problem << "\n";
    }
    return 0;
}
