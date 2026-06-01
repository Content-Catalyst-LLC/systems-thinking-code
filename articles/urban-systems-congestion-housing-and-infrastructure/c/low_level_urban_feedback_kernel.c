#include <stdio.h>

static double clamp(double x) {
    if (x < 0.0) return 0.0;
    if (x > 100.0) return 100.0;
    return x;
}

int main(void) {
    double congestion = 50.0, affordability = 44.0, infrastructure = 60.0, displacement = 42.0;
    for (int year = 0; year <= 30; ++year) {
        congestion = clamp(congestion + 0.60 + displacement * 0.008 - affordability * 0.004);
        affordability = clamp(affordability + 0.35 - congestion * 0.010 - displacement * 0.006);
        infrastructure = clamp(infrastructure + 0.50 - 1.10 - congestion * 0.008);
        displacement = clamp(displacement + congestion * 0.006 - affordability * 0.004);
    }
    double resilience = clamp((100.0 - congestion) * 0.25 + affordability * 0.25 + infrastructure * 0.30 + (100.0 - displacement) * 0.20);
    printf("Urban C kernel: congestion=%.2f affordability=%.2f infrastructure=%.2f displacement=%.2f resilience=%.2f\n", congestion, affordability, infrastructure, displacement, resilience);
    return 0;
}
