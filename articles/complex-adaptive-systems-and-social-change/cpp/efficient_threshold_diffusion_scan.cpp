#include <algorithm>
#include <iostream>
#include <vector>

struct Agent {
    int id;
    double exposure;
    double threshold;
    double trust;
};

double adoption_signal(const Agent& a) {
    double signal = 0.5 + (a.exposure - a.threshold) + 0.25 * a.trust;
    return std::max(0.0, std::min(1.0, signal));
}

int main() {
    std::vector<Agent> agents = {
        {1, 0.42, 0.50, 0.60},
        {2, 0.64, 0.48, 0.55},
        {3, 0.78, 0.34, 0.72},
        {4, 0.30, 0.58, 0.40}
    };

    std::cout << "agent_id,adoption_signal\n";
    for (const auto& agent : agents) {
        std::cout << agent.id << "," << adoption_signal(agent) << "\n";
    }
    return 0;
}
