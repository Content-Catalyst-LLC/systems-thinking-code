// Goal feedback solver scaffold.
// Compile with: g++ goal_feedback_solver.cpp -std=c++17 -O2 -o goal_feedback_solver

#include <algorithm>
#include <iostream>

int main() {
    double state = 0.25;
    double goal = 0.80;
    double correction = 0.30;

    for (int t = 0; t < 12; ++t) {
        double error = goal - state;
        state = std::clamp(state + correction * error, 0.0, 1.0);
        std::cout << t << "," << state << "\n";
    }
}
