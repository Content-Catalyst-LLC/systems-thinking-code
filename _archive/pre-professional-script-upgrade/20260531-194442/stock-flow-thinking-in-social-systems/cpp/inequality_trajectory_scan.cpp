#include <iostream>

int main() {
    double higher_asset = 80000.0;
    double lower_asset = 4000.0;
    for (int month = 0; month < 36; ++month) {
        higher_asset = higher_asset + 2200.0 - 1100.0 + 0.01 * higher_asset;
        lower_asset = lower_asset + 1200.0 - 1150.0 + 0.01 * lower_asset;
    }
    std::cout << "higher_asset_final=" << higher_asset << "\n";
    std::cout << "lower_asset_final=" << lower_asset << "\n";
    return 0;
}
