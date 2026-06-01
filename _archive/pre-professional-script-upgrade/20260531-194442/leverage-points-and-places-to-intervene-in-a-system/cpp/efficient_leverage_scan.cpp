#include <iostream>
#include <vector>
#include <string>

struct Candidate {
    std::string name;
    double strength;
    double cost;
    double delay;
};

int main() {
    std::vector<Candidate> candidates = {
        {"burden reduction", 0.70, 2.0, 4.0},
        {"community feedback", 0.80, 3.0, 6.0},
        {"metric redesign", 0.85, 2.0, 5.0}
    };
    for (const auto& c : candidates) {
        double score = c.strength * 10.0 - c.cost * 0.5 - c.delay * 0.05;
        std::cout << c.name << " score=" << score << "\n";
    }
    return 0;
}
