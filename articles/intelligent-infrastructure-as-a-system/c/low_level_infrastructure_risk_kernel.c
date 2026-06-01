#include <stdio.h>

static double clamp(double value, double low, double high) {
    if (value < low) return low;
    if (value > high) return high;
    return value;
}

static double risk_score(double condition, double criticality, double redundancy, double cyber_dependency) {
    return clamp((100.0 - condition) * 0.35 + criticality * 0.30 + (100.0 - redundancy) * 0.20 + cyber_dependency * 0.15, 0.0, 100.0);
}

int main(void) {
    printf("asset_id,risk_score\n");
    printf("bridge_north,%.3f\n", risk_score(64.0, 78.0, 35.0, 28.0));
    printf("water_main_east,%.3f\n", risk_score(58.0, 86.0, 25.0, 34.0));
    printf("substation_7,%.3f\n", risk_score(70.0, 92.0, 42.0, 66.0));
    return 0;
}
