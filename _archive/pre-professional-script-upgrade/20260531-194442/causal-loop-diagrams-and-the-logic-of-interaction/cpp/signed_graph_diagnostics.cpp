#include <iostream>
#include <vector>

int main() {
    std::vector<int> loop_signs = {1, 1, 1};
    int product = 1;
    for (int sign : loop_signs) product *= sign;
    std::cout << "Loop polarity: " << (product > 0 ? "reinforcing" : "balancing") << "\n";
    return 0;
}
