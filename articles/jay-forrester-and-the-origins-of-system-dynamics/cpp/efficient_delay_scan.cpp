#include <algorithm>
#include <iostream>
#include <vector>

double delayed_value(const std::vector<double>& history, int delay) {
    if (static_cast<int>(history.size()) <= delay) {
        return history.front();
    }
    return history[history.size() - delay - 1];
}

int main() {
    std::vector<double> history = {58.0, 57.1, 55.8, 53.4, 51.0, 49.3};
    std::cout << "delay,perceived_backlog\n";
    for (int delay = 1; delay <= 5; delay++) {
        std::cout << delay << "," << delayed_value(history, delay) << "\n";
    }
    return 0;
}
