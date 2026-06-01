#include <iostream>
#include <deque>
#include <iomanip>

int main() {
    double problem = 60.0;
    std::deque<double> history = {0.0, 0.0, 0.0};

    std::cout << "time,problem,fix,delayed_fix\n";
    for (int t = 0; t < 25; ++t) {
        double fix = 0.35 * problem;
        double delayed = history.front();
        history.pop_front();
        problem = problem - 0.25 * fix + 0.18 * delayed + 4.0;
        history.push_back(fix);
        std::cout << t << "," << std::fixed << std::setprecision(3)
                  << problem << "," << fix << "," << delayed << "\n";
    }
    return 0;
}
