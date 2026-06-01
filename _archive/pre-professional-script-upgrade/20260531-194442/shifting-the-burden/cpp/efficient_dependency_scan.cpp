#include <algorithm>
#include <iostream>
#include <vector>

struct Result {
    double relief;
    double repair;
    double dependency;
};

int main() {
    std::vector<Result> results;

    for (double relief = 10.0; relief <= 60.0; relief += 10.0) {
        for (double repair = 5.0; repair <= 50.0; repair += 5.0) {
            double dependency = std::max(0.0, 0.30 + 0.015 * relief - 0.012 * repair);
            results.push_back({relief, repair, dependency});
        }
    }

    std::cout << "relief,repair,dependency\n";
    for (const auto& row : results) {
        if (row.dependency > 0.65) {
            std::cout << row.relief << "," << row.repair << "," << row.dependency << "\n";
        }
    }

    return 0;
}
