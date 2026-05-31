#include <iostream>

int main() {
    double feedback_quality = 0.70;
    double memory_retention = 0.80;
    double authority = 0.75;
    double threshold = 0.40;
    double score = feedback_quality * memory_retention * authority;
    std::cout << "learning_score=" << score << " threshold_met=" << (score > threshold) << "\n";
    return 0;
}
