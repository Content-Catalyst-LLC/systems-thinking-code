#include <math.h>
#include <stdio.h>

static double forcing(double co2) {
    return 5.35 * log(co2 / 280.0);
}

int main(void) {
    double co2 = 420.0, emissions = 40.0, temp = 1.2, heat = 0.0, feedback = 1.28;
    for (int year = 0; year <= 80; year++) {
        emissions *= 0.96;
        co2 += (emissions / 7.8) * 0.55;
        double f = forcing(co2);
        heat += f * 0.035;
        double target = 0.78 * f * feedback;
        temp += 0.10 * (target - temp) + heat * 0.006;
    }
    printf("Final synthetic CO2 ppm: %.2f\n", co2);
    printf("Final synthetic temperature anomaly: %.3f C\n", temp);
    return 0;
}
