#include <algorithm>
#include <iostream>
#include <vector>
#include <string>

struct Group {
    std::string name;
    double exposure;
    double protection;
};

double harm_gap(const Group& group) {
    return group.exposure - group.protection;
}

int main() {
    std::vector<Group> groups = {
        {"frontline_community", 86, 34},
        {"protected_group", 42, 72},
        {"future_generations", 82, 10}
    };

    std::cout << "group,harm_exposure_gap\n";
    for (const auto& group : groups) {
        std::cout << group.name << "," << harm_gap(group) << "\n";
    }
    return 0;
}
