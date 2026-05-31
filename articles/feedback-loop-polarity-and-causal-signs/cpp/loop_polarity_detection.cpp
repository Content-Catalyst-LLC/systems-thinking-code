#include <iostream>
#include <vector>
#include <numeric>

int main() {
    std::vector<int> signs = {1, -1, -1};
    int product = std::accumulate(signs.begin(), signs.end(), 1, std::multiplies<int>());
    std::cout << (product > 0 ? "reinforcing" : "balancing") << "\n";
    return 0;
}
