#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

struct Asset {
    std::string id;
    double condition;
    double criticality;
    double redundancy;
    double cyber_dependency;
};

double clamp(double value, double low, double high) {
    return std::max(low, std::min(high, value));
}

double risk_score(const Asset& a) {
    return clamp((100.0 - a.condition) * 0.35 + a.criticality * 0.30 + (100.0 - a.redundancy) * 0.20 + a.cyber_dependency * 0.15, 0.0, 100.0);
}

int main() {
    std::vector<Asset> assets = {
        {"bridge_north", 64, 78, 35, 28},
        {"water_main_east", 58, 86, 25, 34},
        {"substation_7", 70, 92, 42, 66}
    };

    std::sort(assets.begin(), assets.end(), [](const Asset& a, const Asset& b) {
        return risk_score(a) > risk_score(b);
    });

    std::cout << "asset_id,risk_score\n";
    for (const auto& asset : assets) {
        std::cout << asset.id << "," << risk_score(asset) << "\n";
    }
    return 0;
}
