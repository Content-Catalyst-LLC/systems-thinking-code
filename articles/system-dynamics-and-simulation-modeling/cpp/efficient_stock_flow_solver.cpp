#include <algorithm>
#include <iostream>
#include <vector>

struct Row {
    int time;
    double stock;
    double inflow;
    double outflow;
};

int main() {
    double stock = 100.0;
    double inflow = 12.0;
    double outflow_fraction = 0.05;
    std::vector<Row> rows;
    for (int t = 0; t <= 24; ++t) {
        double outflow = outflow_fraction * stock;
        rows.push_back({t, stock, inflow, outflow});
        stock = std::max(0.0, stock + inflow - outflow);
    }
    for (const auto& row : rows) {
        std::cout << row.time << "," << row.stock << "," << row.inflow << "," << row.outflow << "\n";
    }
    return 0;
}
